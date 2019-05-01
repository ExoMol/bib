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
setup a python virtual environment. This can be done as follows:

    $ pip install --user pipenv

You will need to add the local folder `/home/<USERNAME>/.local/bin` to your bin
path (where `<USERNAME>` is your username):

    $ export PATH=/home/<USERNAME>/.local/bin:$PATH

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

