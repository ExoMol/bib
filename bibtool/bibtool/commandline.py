#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import tempfile
import bibtool.utilities as utils


# TODO: Fuzzy match/suggest journal lookup based on journal value


@click.group()
def exomol_bib_tool():
    '''
    \b
     ______           __  __       _   _     _ _     _              _
    |  ____|         |  \/  |     | | | |   (_) |   | |            | |
    | |__  __  _____ | \  / | ___ | | | |__  _| |__ | |_ ___   ___ | |
    |  __| \ \/ / _ \| |\/| |/ _ \| | | '_ \| | '_ \| __/ _ \ / _ \| |
    | |____ >  < (_) | |  | | (_) | | | |_) | | |_) | || (_) | (_) | |
    |______/_/\_\___/|_|  |_|\___/|_| |_.__/|_|_.__/ \__\___/ \___/|_|

    Exomol bibtex manager. Please use this tool to add new bibtex entries
    or format existing files.

    For more information on a specific command please type:

    ./bibtool [Command] --help (commands are listed at the bottom)

    Example:

    ./bibtool add --help

    '''
    pass


@exomol_bib_tool.command(
        help=('''
            Format existing bibtex file(s) to the Exomol format specifications.

            ---------- Example ----------

            Format three existing bibtex files ex{1-3}.bib and add a molecule
            extension (.H2) to the end of each bib key:

            \b
            ./bibtool format -ix -m H2 --sort ex1.bib ex2.bib ex3.bib

            '''),
        )
@click.option(
        '-i',
        '--inplace',
        help=(
            'Overwrite given file(s) with new format. '
            'If the option -i/--inplace is omitted then a modified copy will '
            'be created with a \".fmt.bib" extension. This can be useful '
            'for examining the proposed changes to the file(s)'
            ),
        is_flag=True,
        )
@click.option(
        '-v',
        '--verbose',
        help=(
            'Output additional information including duplicate records and '
            'any duplicate keys.'
            ),
        is_flag=True,
        )
@click.option(
        '--sort/--no-sort',
        help=(
            'Sort records in reverse order on publication year '
            'i.e., most recent first.'
            ),
        default=True,
        )
@click.option(
        '-x',
        '--generate-exomol-key',
        help=(
            'Generate Exomol key for each record in bibtex file. '
            'This follows the rules given in [bibfiles.tex]. '
            'e.g., for a 2018 paper published by authors Townes-Earle, '
            'J. Green, D., the citation key would be 18ToGrxx'
            ),
        is_flag=True,
        )
@click.option(
        '-m',
        '--molecule',
        help=(
            'Add molecule extension to citation key '
            'e.g., --molecule H2 will give 17CaBoxx.H2'
            ),
        default='',
        )
@click.argument(
        'files',
        nargs=-1,
        type=click.Path(exists=True),
        required=True,
        )
def format(
        files,
        inplace,
        verbose,
        sort,
        generate_exomol_key,
        molecule,
        ):
    for filename in files:
        bib_db = utils.read_bibfile(filename=filename)

        bib_db = utils.format_bib_db(
                bib_db=bib_db,
                sort=sort,
                generate_exomol_key=generate_exomol_key,
                molecule=molecule,
                verbose=verbose,
                )

        utils.write_bibfile(
                filename=filename,
                bib_db=bib_db,
                inplace=inplace,
                )

    return


@exomol_bib_tool.command(
        help=('''
            Add one or more, new bibtex entries to new or existing file(s). If
            the option -e/--entries is omitted the program will launch your
            default text editor ($EDITOR) allowing you to add multiple bibtex
            entries with more ease. You MUST save and quit in order for the
            entries to be processed.

            If a file in [FILES] does not exist it will be created.

            ---------- Example ----------

            Add new bibtex reference to an existing file 'example.bib':

            \b
            ./bibtool add -ix example.bib -e '
            @article{ refId0,
                author = {Townes-Earle, J. and Green, D.},
                title = {Best p{A}per Ever},
                DOI= "10.1140/epjd/e2009-00243-1",
                url= "https://doi.org/10.1140/epjd/e2009-00243-1",
                journal = {Random Journo},
                year = 2019,
                volume = 56,
                number = 5,
                pages = "1-66",
                month = "jan",
            }
            '
            '''
            ),
        )
@click.option(
        '-i',
        '--inplace',
        help=(
            'Overwrite given file(s) with new format. '
            'If the option -i/--inplace is omitted then a modified copy will '
            'be created with a \".fmt.bib" extension. This can be useful '
            'for examining the proposed changes to the file(s)'
            ),
        is_flag=True,
        )
@click.option(
        '-v',
        '--verbose',
        help=(
            'Output additional information including duplicate records and '
            'any duplicate keys.'
            ),
        is_flag=True,
        )
@click.option(
        '--sort/--no-sort',
        help=(
            'Sort records in reverse order on publication year '
            'i.e., most recent first.'
            ),
        default=True,
        )
@click.option(
        '-x',
        '--generate-exomol-key',
        help=(
            'Generate Exomol key for each record in bibtex file. '
            'This follows the rules given in [bibfiles.tex]. '
            'e.g., for a 2018 paper published by authors Townes-Earle, '
            'J. Green, D., the citation key would be 18ToGrxx'
            ),
        is_flag=True,
        )
@click.option(
        '-m',
        '--molecule',
        help=(
            'Add molecule extension to citation key '
            'e.g., --molecule H2 will give 17CaBoxx.H2'
            ),
        default='',
        )
@click.option(
        '-e',
        '--entry',
        help=(
            'Add manual entry in between single quotes \'\'. You can '
            'copy/paste from google scholar or web of science for example.'
            'If you do not use this option your default text editor '
            '(see $EDITOR) will open. Paste the text in here then save '
            'and quit.'
            ),
        default=None,
        )
@click.argument(
        'files',
        nargs=-1,
        type=click.Path(),
        required=True,
        )
def add(
        files,
        inplace,
        verbose,
        sort,
        generate_exomol_key,
        molecule,
        entry,
        ):

    '''This command will add one or more bibtex entries given by the
    -e/--entries option or from $EDITOR if -e/--entries if left blank

    '''

    if entry is None:
        marker = '# Everything below this comment is ignored\n'
        close = '# To cancel: quit without saving.'
        entry = click.edit('\n\n' + marker + close)
        if entry is not None:
            entry = entry.split(marker, 1)[0].rstrip('\n')
        else:
            click.echo(
                    'Error: No manual entry received. Please try again.',
                    err=True,
                    )
            exit(1)

    infile = tempfile.TemporaryFile(mode='w+')
    infile.write(entry)
    infile.seek(0)

    new_bib_db = utils.read_bibfile(filename=infile)

    for filename in files:
        try:
            bib_db = utils.read_bibfile(filename=filename)
        except (FileNotFoundError, IndexError) as e:
            # if one of these errors is thrown, it is because
            # the file does not exist or it is empty.
            with open(filename, 'w') as newfile:
                newfile.write(' ')
            bib_db = utils.read_bibfile(filename=filename)
        for key, entry in new_bib_db.entries_dict.items():
            bib_db.entries_dict[entry['ID']] = entry

        bib_db = utils.format_bib_db(
                bib_db=bib_db,
                sort=sort,
                generate_exomol_key=generate_exomol_key,
                molecule=molecule,
                verbose=verbose,
                )

        utils.write_bibfile(
                filename=filename,
                bib_db=bib_db,
                inplace=inplace,
                )

    pass
