from bibtexparser.bparser import BibTexParser
from collections import OrderedDict
import bibtexparser as btp
import click
import bibtool.formatters as fmt
import pandas as pd
import re


def tidy_entry(key, entry):
    '''tidy_entry checks for required_fields and additional_fields. If a
    required_field is not found an error is raised. A cleaned_entry is created
    that contains only the required_fields and any additional_fields that are
    present. Everything else that is not 'required' or 'additional' is not
    kept.

    :key: string which is the key for this entry
    :entry: dict containing fields for this entry
    :returns: clean entry back as dict
    '''

    required_fields = [
            'author',
            'title',
            'journal',
            'year',
            'volume',
            'pages',
            'ENTRYTYPE',
            'ID',
            ]
    additional_fields = [
            'doi',
            'abstract',
            'keywords',
            'keywords-plus',
            'journal-iso',
            'notes',
            ]

    cleaned_entry = {}

    for field in required_fields:

        msg = 'Error: missing a required field [{field}] in ref. [{key}]'

        if field == 'pages':
            try_count = 0
            for alias in ['pages', 'eid', 'article-number']:
                try:
                    cleaned_entry[field] = entry[alias]
                    continue
                except KeyError as e:
                    try_count += 1
                    if try_count == 3:
                        msg = msg.format(key=key, field=field)
                        raise KeyError(msg)
        else:
            try:
                cleaned_entry[field] = entry[field]
            except KeyError as e:
                msg = msg.format(key=key, field=field)
                raise KeyError(msg)

    for field in additional_fields:
        try:
            if entry[field]:
                cleaned_entry[field] = entry[field]
        except KeyError as e:
            pass

    entry = cleaned_entry

    return entry


def format_entry(entry):
    '''format the main fields in a given bib entry.

    :entry: dict containing fields for this entry
    :returns: formatted entry as dict
    '''

    entry = fmt.format_abstract(entry)
    entry = fmt.format_author(entry)
    entry = fmt.format_doi(entry)
    entry = fmt.format_journal(entry=entry)
    entry = fmt.format_pages(entry)
    entry = fmt.format_title(entry)
    entry = fmt.format_year(entry)

    return entry


def sort_bib_entries(bib_entries):
    '''sort the bib entries into alphabetical order on author and
    then on numerical order of year

    :bib_entries: dict or OrderedDict - bib entries to be sorted
    :returns: OrderedDict containing sorted bib entries
    '''

    def key(item):
        return (
                int("-"+re.sub(r'[^\w]', r'', item[1]['year'])),
                item[1]['author'],
                )

    bib_entries = OrderedDict(
        sorted(
            bib_entries.items(),
            key=key
        )
    )

    return bib_entries


def read_bibfile(filename):
    '''this function parses the text contained in 'filename' to the
    BibTexParser library.

    :filename: string or file object
    :returns: bib_db as a BibTexDatabase
    '''

    parser = BibTexParser(interpolate_strings=False)

    if isinstance(filename, str):
        with open(filename) as infile:
            bib_db = btp.load(bibtex_file=infile, parser=parser)
    else:
        with filename as infile:
            bib_db = btp.load(bibtex_file=infile, parser=parser)

    return bib_db


def write_bibfile(filename, bib_db, inplace):
    '''write bib_db to a file. If inplace is True then the file given will be
    overwritten.

    :filename: string path to new or existing file
    :bib_db: BibTexDatabase containing all the bib entries
    :inplace: bool, if True then file 'filename' is overwritten. If False then
    the original file is not altered and a new file 'filename.fmt.bib' is
    created.
    :returns: OrderedDict containing sorted bib entries
    '''

    writer = btp.bwriter.BibTexWriter()
    writer.indent = ''
    writer.order_entries_by = False

    if not inplace:
        filename = filename.replace('.bib', '.fmt.bib')

    with open(filename, 'w') as outfile:
        btp.dump(
                bib_database=bib_db,
                bibtex_file=outfile,
                writer=writer,
                )

    return


def check_duplicate_entries(bib_db, verbose):
    '''check for duplicate entries in the BibTexDatabase bib_db. Duplicate
    entries will be deleted. If verbose is True then the deleted records will
    be shown.
    The duplicate criteria is match on:
    (year AND journal AND volume AND pages)
    Obviously this is not perfect as typos will lead to the lack of a match
    however, this is the most general case that doesn't have false positives.

    :bib_db: BibTexDatabase containing all the bib entries
    :verbose: bool, if True then deleted records are shown
    :returns: BibTexDatabase containing unique records only
    '''

    bib_dict = bib_db.entries_dict
    dup_check = []

    for key, entry in bib_dict.items():
        if entry['ENTRYTYPE'] != 'article':
            continue

        journal = entry['journal']
        if isinstance(journal, str):
            journal = journal
        else:
            journal = journal.expr[0].name

        dup_check.append([
            entry['year'],
            journal,
            entry['volume'],
            entry['pages'],
            entry['title'],
            entry['ID'],
            key,
            ])

    columns = [
            'year',
            'journal',
            'volume',
            'pages',
            'title',
            'ID',
            'key',
            ]

    subset = [
            'year',
            'journal',
            'volume',
            'pages',
            ]

    df = pd.DataFrame(dup_check, columns=columns)
    duplicates = df.loc[df.duplicated(subset=subset, keep=False)]
    if len(duplicates):
        duplicates = duplicates.sort_values(by=subset+['title'])
        duplicates = duplicates.reset_index()
        duplicates['delete'] = duplicates.duplicated(
                subset=subset,
                keep='first',
                )
        duplicates = duplicates.drop(['ID'], axis=1)
        dup_keys = duplicates[duplicates['delete']]['key'].values
        if verbose:
            click.echo('The following records are marked as duplicates:')
            click.echo('(records marked delete = True will be removed)')
            click.echo(duplicates.to_string())
        click.echo(
                '{n} duplicate records deleted'.format(n=len(dup_keys)),
                )
        for key in dup_keys:
            print('deleting', key)
            del bib_db.entries_dict[key]
    else:
        click.echo('No duplicate records found')

    return bib_db


def check_duplicate_tags(bib_db, verbose):
    '''check for duplicate keys/tags in the BibTexDatabase bib_db. Because the
    ExoMol tag format is not unique for all papers, necessarily duplicate keys
    can be created from unique articles. Therefore duplicate keys will be
    appended with a character [a-z] to make them unique. For example,
    2018 Tennyson, J., Yurchenko, SN, ExoJournal (5) 1020
    2018 Tennyson, J., Yurchenko, SN, JPhysExoPlanet (10) 01887
    are two distinct papers published by the same authors in the same year.
    Therefore the keys would be 18TeYuxx and 18TeYuxx. After this function is
    called the keys would become 18TeYuxxa and 18TeYuxxb. The choice to sort
    them is arbitrary and for now uses the page number.

    :bib_db: BibTexDatabase containing all the bib entries
    :verbose: bool, if True then deleted records are shown
    :returns: BibTexDatabase containing unique keys/tags
    '''

    bib_dict = bib_db.entries_dict
    dup_check = []

    for key, entry in bib_dict.items():
        if entry['ENTRYTYPE'] != 'article':
            continue

        journal = entry['journal']
        if isinstance(journal, str):
            journal = journal
        else:
            journal = journal.expr[0].name

        dup_check.append([
            entry['year'],
            journal,
            entry['pages'],
            entry['ID'],
            key,
            ])

    columns = [
            'year',
            'journal',
            'pages',
            'ID',
            'key',
            ]

    subset = [
            'ID',
            'pages',
            ]

    df = pd.DataFrame(dup_check, columns=columns)

    duplicates = df.loc[df.duplicated(subset=subset, keep=False)]

    if len(duplicates):
        duplicates = duplicates.sort_values(by=subset)
        duplicates = duplicates.reset_index()
        count = duplicates.groupby('ID')['ID'].count().values
        ID = duplicates['ID'].values
        uniqueID = [chr(r+97) for c in count for r in range(c)]
        uniqueID = [a + b for a, b in zip(ID, uniqueID)]
        duplicates['ID'] = uniqueID
        if verbose:
            click.echo('The following records have duplicate keys:')
            click.echo('(they have been appended with letters [a-z])')
            click.echo(duplicates.to_string())

        for key, ID in zip(duplicates['key'].values, uniqueID):
            bib_dict[key]['ID'] = ID

        bib_db._entries_dict = bib_dict
        bib_db.entries = [v for k, v in bib_dict.items()]

    return bib_db


def format_bib_db(bib_db, sort, generate_exomol_key, molecule, verbose):
    '''this is the main formatting function. It formats the bib_db read from
    BibTexParser and returns a clean formatted database.

    :bib_db: BibTexDatabase containing all the bib entries
    :sort: bool, True (default) means the fields will be sorted in order of
    year (most recent first) and then by Author surname (a-z)
    :generate_exomol_key: bool, False (default). If true then generate a
    key/tag for each record that follows the ExoMol format.
    :molecule: string that will become extension
    :verbose: bool, if True then additional information is printed e.g.,
    duplicate keys/entries
    :returns: BibTexDatabase containing clean formatted entries
    '''

    formatted_bib_db = {}
    errors_found = False

    for key, entry in bib_db.entries_dict.items():
        if entry['ENTRYTYPE'] != 'article':
            # do not format entry/record unless it is of type 'article'.
            formatted_bib_db[key] = entry
            continue

        try:
            entry = tidy_entry(key, entry)
        except KeyError as e:
            click.echo(e, err=True)
            errors_found = True

        formatted_bib_db[key] = entry

    if errors_found:
        click.echo(
                'Program terminated. Please fix errors above and try again',
                err=True,
                )
        exit(1)

    for key, entry in formatted_bib_db.items():
        if entry['ENTRYTYPE'] != 'article':
            formatted_bib_db[key] = entry
            continue

        entry = format_entry(entry)
        if generate_exomol_key:
            entry = fmt.format_key(entry, molecule)
        formatted_bib_db[key] = entry

    exomol_dict = OrderedDict(formatted_bib_db)

    if sort:
        # first sort authors a-z and then most recent first
        exomol_dict = sort_bib_entries(exomol_dict)

    bib_db._entries_dict = exomol_dict
    bib_db = check_duplicate_entries(bib_db, verbose)
    bib_db = check_duplicate_tags(bib_db, verbose)

    bib_db.entries = [v for k, v in bib_db.entries_dict.items()]

    return bib_db
