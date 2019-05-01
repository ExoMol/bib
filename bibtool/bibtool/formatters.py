from bibtexparser.customization import author as custom_author
import bibtexparser as btp
import re
import textwrap


def format_abstract(entry):
    '''format the abstract field.
    1. remove backslashes (these destroy the syntax highlighting)
    2. remove new lines
    3. remove any special chars (especially escape sequences)
    4. textwrap the string (max. width 70)

    :entry: dict containing fields for this entry
    :returns: formatted entry back as dict
    '''

    try:
        abstract = entry['abstract']
        abstract = re.sub(r'\\', r'', abstract)
        abstract = re.sub(r'\n', r' ', abstract)
        abstract = "".join([i for i in abstract if 31 < ord(i) < 127])
        entry['abstract'] = textwrap.fill(abstract)
    except KeyError as e:
        return entry

    return entry


def format_author(entry):
    '''format the author field.
    1. switch uppercase 'AND' for lowercase 'and'
    2. sort names in correct order (removes the 'and' separator)
    3. join sorted names back with 'and'

    :entry: dict containing fields for this entry
    :returns: formatted entry back as dict
    '''

    authors = entry['author']
    entry['author'] = authors.replace(' AND ', ' and ')
    entry = custom_author(entry)
    authors = entry['author']
    entry['author'] = ' and '.join(authors)

    return entry


def format_doi(entry):
    '''format the doi field.
    1. remove http://dx.doi.org/ from doi if it is present

    :entry: dict containing fields for this entry
    :returns: formatted entry back as dict
    '''

    try:
        doi = entry['doi']
    except KeyError as e:
        return entry

    doi = doi.replace('http://dx.doi.org/', '')

    entry['doi'] = doi

    return entry


def format_journal(entry):
    '''format the journal field.
    1. if journal is a bibdatastring then make it uppercase
    i.e., 'pra' -> 'PRA' but {'Phys. Rev A'} is left unaltered

    :entry: dict containing fields for this entry
    :returns: formatted entry back as dict
    '''

    try:
        expression = btp.bibdatabase.BibDataStringExpression
        if isinstance(entry['journal'], expression):
            journal = entry['journal'].expr[0].name
            entry['journal'].expr[0].name = journal.upper()
    except KeyError as e:
        pass

    return entry


def format_key(entry, molecule=''):
    '''format the ID field (the key)
    1. generate a new ID key for the entry in the Exomol format i.e.,
    15AuAuxx.MOl.
    2. molecular tag (.MOl) will only be added if [molecule] is not
    an empty string.

    :entry: dict containing fields for this entry
    :molecule: string that will become extension
    :returns: formatted entry back as dict
    '''

    if molecule != '':
        molecule = '.' + molecule

    authors = entry['author']    # list of authors for given entry
    year = entry['year']
    year = year[-2:]             # last two digits

    authors = authors.split(' and ')
    authors = [re.sub(r'[^\w ,]', r'', author) for author in authors]
    authors = [a.replace(' ', '').split(',')[0][:2] for a in authors]

    for i in range(3):
        if i > len(authors)-1:
            authors.append('xx')
    authors = ''.join(authors[:3])

    entry['ID'] = year+authors+molecule

    return entry


def format_pages(entry):
    '''format the pages field.
    1. remove additional white space
    2. remove double braces i.e., {{2}} -> {2}

    :entry: dict containing fields for this entry
    :returns: formatted entry back as dict
    '''

    try:
        pages = entry['pages']
    except KeyError as e:
        return entry

    pages = pages.replace(' ', '')

    match = re.match('(^\s*{)(.*)(}\s*$)', pages)

    if match:
        pages = match.group(2)

    entry['pages'] = pages

    return entry


def format_title(entry):
    '''format the title field.
    1. force title to be surrounded by double braces
    e.g. {'title'} -> {{'tile'}}

    :entry: dict containing fields for this entry
    :returns: formatted entry back as dict
    '''

    try:
        title = entry['title']
    except KeyError as e:
        return entry

    match = re.match('(^\s*{)(.*)(}\s*$)', title, flags=re.DOTALL)

    if not match:
        title = '{' + title + '}'

    entry['title'] = title

    return entry


def format_year(entry):
    '''format the yeear field.
    1. remove white space in year
    2. remove double braces
    e.g. {{'year'}} -> {'year'}
    this is required so that the year can be used to sort entries

    :entry: dict containing fields for this entry
    :returns: formatted entry back as dict
    '''

    year = entry['year'].replace(' ', '')
    match = re.match('(^\s*{)(.*)(}\s*$)', year)

    if match:
        year = match.group(2)

    entry['year'] = year

    return entry
