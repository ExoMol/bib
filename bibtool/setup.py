from setuptools import setup

setup(
        name='bibtool',
        version='0.1',
        description='Exomol bibtool for formatting bibtex files.',
        url='https://github.com/ExoMol/bib',
        author='Tom Melt',
        author_email='thomas.meltzer1@gmail.com',
        license='MIT',
        entry_points={
            'console_scripts': ['bibtool=bibtool.commandline:exomol_bib_tool'],
            },
        packages=['bibtool'],
        install_requires=[
            'pandas',
            'click',
            'bibtexparser',
            ],
        zip_safe=False,
        )
