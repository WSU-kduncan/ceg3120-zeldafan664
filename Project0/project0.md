200~Project 0 - Git Guide

In your repo for this course, create a file named git-guide.md. In this file, write up a quick guide to using git & GitHub. For each command, include a brief definition of what it does, and a sample of how to use it. status has a sample of what a well done filled in entry looks like.

Entries that are currently crossed out we will get to later in the course that you could go back and write some details on later.
Command line git

    status
        Shows status of the local repository. This status includes:
            number of local commits that have not been synced with remote (GitHub)
            list of files in local folder than are NOT being tracked by git
            list of files in local folder that have changes that need to be committed
        git status
    clone
	clones you respoitory from github to your environment in your Ubuntu instance.
    add
	satages specified changes for committing such as new files, files that have been updated, new directories, etc. 
    rm
	removes files and directories along with some other options
    commit
	Create a new commit containing the current contents of the index and the given log message describing the changes
    push
	used to upload local repository content to a remote repository
    fetch
	can fetch from either a single named repository or URL
    merge
	Incorporates changes from the named commits (since the time their histories diverged from the current branch) into the current branch
    pull
	pulls changes from your rremote github respository to the local one.
    branch
	create a new branch that is separate from the main branch
    checkout
	go and "checkout" a different branch. in short, used to switch branches.
    init
	This command creates an empty Git repository

    remote
	Add a remote named <name> for the repository at <URL>

git files & folders

    .git folder
	The . git folder contains all information that is necessary for the 
project and all information relating commits, remote repository address, etc.
    .gitignore file
	A . gitignore file is a plain text file where each line contains a
 pattern for files/directories to ignore.
    .git/hooks
	Hooks are programs you can place in a hooks directory to trigger actions at certain points in git's execution

GitHub

    Pull requests:
Pull requests let you tell others about changes you've pushed to a branch in a
 repository on GitHub
    SSH authentication to repositories
	SSH public key authentication works with an asymmetric pair of generated encryption keys
    Actions

