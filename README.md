# ExoMol .bib Files
## Quick Guide
If you know how gitHub works and you have git installed on your machine, you can follow these simple steps to get the .bib files.
If you have not used gitHub or git before please see below for more detailed instructions.

1. To grab a copy simply type: `git clone git@github.com:ExoMol/bib.git` (**you must have a GitHub account**)
1. This will create a local copy of all the bib files on your machine
1. You can add to the bib files as normal (although please adhere to the naming conventions)
1. To submit your changes back to Github:
	* `git add .` (or `git add <file 1> <file 2> <file 3>`)
	* `git commit -m "<your message here>"`
	* `git pull`
	* `git push`
1. Your changes will now be added to the global gitHub repo

(**Note:** you must be a collbaorator to add directly to the gitHub repo. If you are not a collaborator, the best option is to fork the gitHub repo instead and then submit a pull request)

## Detailed Instructions
### Check Git Installation
If you would like a copy of the .bib files on your local machine please follow the below instructions to download them. If not they can still be found on the shared folder in the usual place.

To **clone** (download) the .bib files from this reposistory you will first need **git** installed on your machine. It is more than likely that you may already have git installed on your machine. To check, type the following command in your terminal:

    $ git --version

If it is installed you will see something like this:

    git version 2.7.4

If it is not installed, see [Install Git](#install-git)

### Make a GitHub account

Please note you will need a GitHub account to collaborate in the ExoMol bib project. GitHub accounts can be created [here](https://github.com/).

### Clone .bib Files From GitHub

First locate to the directory on your local machine where you would like to **clone** the .bib files:

    $ cd Documents/ExampleDirectory/

Then type the following command into the terminal:

    $ git clone git@github.com:ExoMol/bib.git

You should see something like this (if it is successful):

    Cloning into 'bib'...
    remote: Counting objects: 570, done.
    remote: Compressing objects: 100% (77/77), done.
    remote: Total 570 (delta 13), reused 88 (delta 12), pack-reused 481
    Receiving objects: 100% (570/570), 12.64 MiB | 483.00 KiB/s, done.
    Resolving deltas: 100% (188/188), done.
    Checking connectivity... done.

You can check the .bib files with `ls -1 ./bib` and you should see something like this:

    emol
    exomol
    journals_astro.bib
    journals_phys.bib
    jt
    MARVEL
    plasma
    README.md
    rmat
    RmatReact

If so then you have successfully cloned .bib git repository.

### Making Changes

Chances are, if you are making ammendments to a certain .bib file then others will also need this change as well. The process to change a bib file, and upload back to GitHub repo (folder) is as follows:

1. Edit/Create file as normal
1. Make change(s) and save
1. Stage (`git add`) changes locally
1. Commit (`git commit`) changes
1. Push (`git push`) changes back to the server

Once you have sent the request to push, these changes will be merged to the master copy on GitHub and available for others to download!

Now at this point, if you have are not sure about what version control software is, or what the basics of git are then I recommend [this guide](http://rogerdudler.github.io/git-guide/). That said, all the information you will need should be in this guide.

#### Edit/Create File
In this example we will modify an existing file `test.bib`:

First check you are working with the most up-to-date copy (most recent **commit**)

    $ cd Documents/ExampleDirectory/bib/
    $ git pull
    Already up-to-date.
    $ git status
    On branch master
    Your branch is up-to-date with 'origin/master'.
    nothing to commit, working directory clean

Then modify the file (using any program vim/nano/gedit/notepad etc.):

    $ vim test.bib

Make your changes and then save. In this case I add a line to the file "Hello World!". Running the command `git status` will verfiy any changes made to the local version.

    $ git status 
    On branch master
    Your branch is up-to-date with 'origin/master'.
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

    	modified:   test.bib

    no changes added to commit (use "git add" and/or "git commit -a")

The key line here is "Changes not staged for commit". This moves us onto our next point - stage (`git add`) changes locally.

#### Stage Changes

Staging changes means that you are preparing to commit your file. You can stage changes at anytime. They will only be committed when you run `git commit`. This is useful when changing multiple files. You can add them individually or all together at the end. In this example we are only making changes to one file `test.bib`. To stage the changes we can do the following:

    $ git add test.bib
    On branch master
    Your branch is up-to-date with 'origin/master'.
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

    	modified:   test.bib

The key line here is now "Changes to be committed". We can now get ready to commit our changes to local **repo** (folder).

#### Commit Changes

For a change to be added to GitHub it must first be committed. A commit is like a snapshot of a folder and all of its contents. After you the changes have been committed they can then pushed back to GitHub (`git push`). To commit your staged changes use `git commit -m "<your message here>"`. Where `<your message here>` can be a short description of the changes made. See below for an example:

    $ git commit -m "made changes to test.bib"
    [master 34f64ba] made changes to test.bib
     1 file changed, 1 insertion(+)
     create mode 100644 test.bib

#### Push Changes back to GitHub

Before you push changes back to GitHub it is always a good idea to run `git pull` first (this helps to avoid errors on the off chance someone else pushes their changes before you can submit).

    $ git pull
    Already up-to-date.

This will update if changes have been made or simply state that the folder is already up-to-date. You are now ready to push your changes back to the server:

    $ git push
    warning: push.default is unset; its implicit value has changed in
    Git 2.0 from 'matching' to 'simple'. To squelch this message
    and maintain the traditional behaviour, use:

      git config --global push.default matching

    To squelch this message and adopt the new behaviour now, use:

      git config --global push.default simple

    When push.default is set to 'matching', git will push local branches
    to the remote branches that already exist with the same name.

    Since Git 2.0, Git defaults to the more conservative 'simple'
    behaviour, which only pushes the current branch to the corresponding
    remote branch that 'git pull' uses to update the current branch.

    See 'git help config' and search for 'push.default' for further information.
    (the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
    'current' instead of 'simple' if you sometimes use older versions of Git)

    Counting objects: 3, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (3/3), 292 bytes | 0 bytes/s, done.
    Total 3 (delta 1), reused 0 (delta 0)
    remote: Resolving deltas: 100% (1/1), completed with 1 local object.
    To git@github.com:ExoMol/bib.git
       7a9cefd..34f64ba  master -> master

Notice that there is a warning message. This can be ignore or you can run the following command to remove it:

    git config --global push.default simple

The important part is the following:

    Counting objects: 3, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (3/3), 292 bytes | 0 bytes/s, done.
    Total 3 (delta 1), reused 0 (delta 0)
    remote: Resolving deltas: 100% (1/1), completed with 1 local object.
    To git@github.com:ExoMol/bib.git
       7a9cefd..34f64ba  master -> master

Now your changes will be available for everyone to download from the main GitHub repository.

## Install Git

If git is not installed, you can run the following commands in terminal to install.
In Ubuntu this is as simple as:

    sudo apt-get update
    sudo apt-get install git

Or in ScientificLinux it is:

    yum update
    yum install git

On the Windows OS, try the GitHub Desktop App:
[https://desktop.github.com/](https://desktop.github.com/)

