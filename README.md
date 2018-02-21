# ExoMol .bib Files
## Getting Started
---
### Check Git Installation
If you would like a copy of the .bib files on your local machine please follow the below instructions to download them. If not they can still be found on the shared folder in the usual place.

To **clone** (download) the .bib files from this reposistory you will first need **git** installed on your machine. It is more than likely that you may already have git installed on your machine. To check, type the following command in your terminal:

    git --version

If it is installed you will see something like this:

    git version 2.7.4

If it is not installed, see [Install Git](#install-git)

### Quick Guide
1. To grab a copy simply type: `git clone git@github.com:ExoMol/bib.git`
1. Or `git clone https://github.com/ExoMol/bib.git` **if you don't have a GitHub account**
1. This will create a bib folder on your machine
1. You can add this path in your LaTeX config and start writing

## Detailed Instructions
---
### Clone .bib Files From GitHub

First locate to the directory on your local machine where you would like to **clone** the .bib files:

    cd Documents/ExampleDirectory/

Then type the following command into the terminal:

    git clone git@github.com:ExoMol/bib.git

You should see something like this (if it is successful):

    Cloning into 'bib'...
    remote: Counting objects: 570, done.
    remote: Compressing objects: 100% (77/77), done.
    remote: Total 570 (delta 13), reused 88 (delta 12), pack-reused 481
    Receiving objects: 100% (570/570), 12.64 MiB | 483.00 KiB/s, done.
    Resolving deltas: 100% (188/188), done.
    Checking connectivity... done.

You can check the .bib files with `ls ./bib` and you should see something like this:

    15NH3.bib       CaO.bib        eckart.bib               HCCS.bib            MARVEL             O2.bib            ScH.bib
    abinitio.bib    CaOCa.bib      emol                     HCF.bib             MARVEL_unused.bib  O3.bib            ScO.bib
    AbInTM.bib      CaOH.bib       ethyl-methyl-ether.bib   HCl.bib             methods2.bib       OClO.bib          SF6.bib
    additional.bib  CH2.bib        exogen2.bib              HCN_.bib            methods_.bib       OH3+.bib          SH.bib
    AlBr.bib        CH2p.bib       exogen.bib               HCN.bib             methods.bib        OH.bib            SH+.bib
    AlF.bib         CH3.bib        exomol                   HCNO.bib            MgCl.bib           OH+.bib           SiC.bib
    AlH.bib         CH3+.bib       exomolcites.bib          HCS.bib             MgH_.bib           OP.bib            SiH2.bib
    AlO_.bib        CH3Cl_.bib     exoplanets_.bib          HDO_.bib            MgH.bib            ORBYTS.bib        SiH4.bib
    AlO.bib         CH3Cl.bib      exoplanets.bib           HDO.bib             MgNC.bib           P2H2.bib          SiH.bib
    a-models.bib    CH3D.bib       extra2.bib               HF.bib              MgO.bib            PAH.bib           SiHF3.bib
    ap.bib          CH3F.bib       extra.bib                history.bib         MgOMg.bib          partition.bib     SiN.bib

If so then you have successfully cloned .bib git repository.

### Making Changes

Chances are, if you are making ammendments to a certain .bib file then others will also need this change as well. The process to change a bib file, and upload back to GitHub repo (folder) is as follows:

1. Open/create file as normal
1. Make change(s) and save as normal
1. Stage (`git add`) changes locally
1. Commit (`git commit`) changes
1. Push (`git push`) changes back to the server

Once you have sent the request to push, the following will happen:

1. These changes can be accepted or rejected by the administrator
1. If accepted they will be merged to the master copy on GitHub and available for others to download!

Now at this point, if you have are not sure about what version control software is, or what the basics of git are then I recommend [this guide](http://rogerdudler.github.io/git-guide/). That said, all the information you will need should be in this guide.

#### Open/Create File
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

**Commit**s represent different versions of the bib folder and its contents i.e. the .bib files. Using git it is possible to see older versions, changes between versions and even restore deleted/old files if necessary. By committing our changes, we will effectively create a new version of the whole folder (changed and unchanged files).

you have saved a local change that is different to the last **commit**. A Commit it means that it has been added to the version control histroy in git. Git commits are a way of tracking different versions of a file or group of files).

## Install Git
---

If git is not installed, you can run the following commands in terminal to install.
In Ubuntu this is as simple as:

    sudo apt-get update
    sudo apt-get install git

Or in ScientificLinux it is:

    yum update
    yum install git

On the Windows OS, try the GitHub Desktop App:
[https://desktop.github.com/](https://desktop.github.com/)


