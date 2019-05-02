# ExoMol BibTex Manager

Please use this command line application to add new bibtex entries or format
existing bibtex files. In this document the application will be referred to
`bibtool` as this is the command to run it in the terminal.

# Installation Instructions

## Cloning the repo

If you do not already have a copy of the bib files, please follow the detailed
instructions [here](../README.md).

## Setup Python Environment

`bibtool` uses python 3 and so you must check you python version:

    $ python --version

To install you will need `pip`. Please check this is installed like follows:

    $ pip --version

If you do not have `sudo` rights then you can still install but first you must
add the local pip user path to your bin path. That is you will need to add the
local folder `/home/<USERNAME>/.local/bin` to your bin path (where `<USERNAME>`
is your username):

    $ export PATH=/home/<USERNAME>/.local/bin:$PATH

You can add this line to your `.bashrc` to save running this command on every
login.

## Installing `bibtool`

Now that you are setup. Make sure you have the latest copy of bib repo.

1. `cd` to the location where you downloaded the bib repo e.g.,

        $ cd /home/<USERNAME>/bib/

1. Then make sure you have the latest copy:

        $ git pull

1. `cd` to the bibtool folder:

        $ cd bibtool/

1. Install with pip:

        $ pip install --user -e .

This will download required packages and install bibtool to the folder we
specified earlier `/home/<USERNAME>/.local/bin`.

To test the program, just run

    $ bibtool --help

This should display the help page for bibtool. Now you are ready to use this
tool.


# How does it work?

The bibtool comes with a useful `--help` option. This can provide more
information on specific commands.

    $ bibtool --help

Or for help on a specific command, e.g., `add`, type;

    $ bibtool add --help

## Example - Add a new reference to H2S.bib

To add a new bibtex reference to an existing file e.g., CaH.bib we can do the
following.

1. Copy the reference from Web of Science, Google Scholar or otherwise

    ```
        @article{ refId0,
            author = {Townes-Earle, J. and Green, D.},
            title = {Best {CaH} paper Ever},
            doi = "http://dx.doi.org/10.1140/epjd/e2009-00243-1",
            url = "https://doi.org/10.1140/epjd/e2009-00243-1",
            journal = {Random Journal},
            year = 2019,
            volume = 5,
            number = 1,
            article-number = "56",
            month = "jan",
        }
    ```

1. Run the bibtool as follows:

        $ bibtool add -m CaH -ix CaH.bib

1. This will open your default text editor `$EDITOR` (to find out what this is
   run `$ echo $EDITOR` in your terminal).

1. Paste the previously copied text into your text editor, then save and quit.

1. This will create a temporary file that is parsed to the bibtool. You do not
   need to delete it as this is done automatically.

1. The bibtool will then:
    * validate the existing references found in `CaH.bib`
    * check for duplicates
    * format the new entry
    * the `-m` option adds a molecular tag to all the references in the file e.g., .CaH<sup>1</sup>
    * the `-x` option generates an exomol key (e.g., 19ToGrxx.CaH)<sup>1</sup>
    * sort all entries (most recent first)<sup>2</sup>
    * write the new bibtex refs. to `CaH.bib`<sup>3</sup>

[1] Optional.

[2] `--sort` is the default behaviour, `--no-sort` will disable sorting.

[3] If option `-i` is specified then the original CaH.bib file will be
overwritten. Otherwise a new file CaH.fmt.bib will be created which can be
useful to compare changes.

## Example - Format an existing BibTex file

To format an existing file e.g., CaH.bib we can do the following.

1. Run the bibtool as follows:

        $ bibtool format -m CaH -ivx CaH.bib

1. The bibtool will then:
    * validate the references found in `CaH.bib`
    * check for duplicates
    * format the new entry
    * the `-v` option will print detailed information on duplicate records.<sup>1</sup>
    * the `-m` option adds a molecular tag to all the references in the file e.g., .CaH<sup>1</sup>
    * the `-x` option generates an exomol key (e.g., 19ToGrxx.CaH)<sup>1</sup>
    * sort all entries (most recent first)<sup>2</sup>
    * write the formatted bibtex refs. to `CaH.bib`<sup>3</sup>

[1] Optional.

[2] `--sort` is the default behaviour, `--no-sort` will disable sorting.

[3] If option `-i` is specified then the original CaH.bib file will be
overwritten. Otherwise a new file CaH.fmt.bib will be created which can be
useful to compare changes.
