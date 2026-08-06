'''
Commands to use git in a new project
'''

'''
As we know the first thing to initialize a new project is to create a new repository 
to do this we use 

git init

then we can add files to the repository using
git add <file_name>

to see the changes we have made we can use
git status

now if we want to commit the changes we can use
git commit -m "commit message"

but we need to set our branch name first using
git branch -M main

then we can push our changes to the remote repository using
git push -u origin main

but where do we push our changes to? we need to create a new repository on github and copy the url of the repository and use it in the command
git remote add origin <url_of_repository>

so the steps will be:
1. Create a new repository on github
2. Copy the url of the repository
3. Initialize a new git repository using git init
4. Add files to the repository using git add <file_name> / if we wanted to add all files we can use git add .
5. Check the status of the repository using git status
6. Commit the changes using git commit -m "commit message"
7. Set the branch name using git branch -M main, this is optional since the default branch name is main, but this will be useful if we want to change the branch name to something else
8. Add the remote repository using git remote add origin <url_of_repository>
9. Push the changes to the remote repository using git push -u origin main

With that we have successfully created a new project and pushed it to github

'''


'''
WE have made some changes to the project and we want to push those changes to the remote repository, we can do that using the following steps:
1. Check the status of the repository using git status
2. Add the changes to the repository using git add <file_name>
3. Commit the changes using git commit -m "commit message"
4. Push the changes to the remote repository using git push

'''


'''
To delete a file from the repository we can use the following command
The first thing maybe we wanted to deleate a file using: rm file.txt 

now we check the status 
git status
We remove the workind directory but stills exists in the staing area

To remove it correctly we need to do:
git ls-files

This will show us the files that are being tracked by git, we can see that the file we want to delete is still being tracked by git, so we need to remove it 
from the staging

git add filename.txt

again we run 
git ls-files

Now is in the staging area, we can see that the file is being tracked by git

git status 
we see now the file is in the staging area
we commit this change
git commit -m "removing file from the repository"

To sum up the steps to delete a file from the repository we can do the following:
1. Remove the file from the working directory using rm <file_name>
2. Check the status of the repository using git status
3. Remove the file from the staging area using git add <file_name>
4. Check the status of the repository using git status
5. Commit the changes using git commit -m "removing file from the repository"

BUT THIS IS NO THE BEST OPTION SO WE CAN USE

******* git rm <file_name> *******
and that will be the best option to remove a file from the repository since it will remove the file from the working directory and the staging area at the same time
we need to commit the changes after this command to remove the file from the repository
'''

'''
Now we will change the name of our file, for that we can use:

mv <old_file_name> <new_file_name>
this will delete the old file and create a new one with the new name, but we need to tell git that we have renamed the file, for that we can use:

git add <old_file_name>
git add <new_file_name>

with this we have renamed the file and git will track the changes

AS above is not the best option, we can use the following command to rename a file:
******* git mv <old_file_name> <new_file_name> *******
---- we only need to use after this the commit command to commit the changes

'''


'''
Now we wanted to know how to ignore files in our repository, for that we can use a file called .gitignore, 
this file will contain the names of the files and directories that we want to ignore, 
for example if we want to ignore all the .txt files we can add the following line to the .gitignore file:

we can have a dir for this (this example), called logs
where every file here is a log that we don't want to track, so we can add the following line to the .gitignore file:

create a file called .gitignore in the command line with:
echo "logs/" > .gitignore

in the file we use:
log/
*.log
(Or specify the name of the file to ignore, for example main.log)


In github page there is a section called .gitignore templates, where we can find templates 
for different programming languages and frameworks, we can use those templates to ignore files that are specific to those languages and frameworks

IMPORTANT 

if we have already added a file to the repository and we want to ignore it, 
we need to remove it from the repository first using 

git rm --cached <file_name> and then add it to the .gitignore file, 
otherwise git will still track the file even if it is in the .gitignore file

sometimes we will get an error but we can fix it using the following command:

git rm --cached -r <file_name>, to remove a directory and all its contents from the repository

And now the file will be ignored by git and will not be tracked anymore
'''


'''
To see in a short way the changes we have made to the repository we can use the following command:
git status -s

this will show us the changes in a short way, for example:
M  file1.txt
A  file2.txt
where M means modified and A means added

'''

'''
Viewing the Stage & Unstage Changes

See the exact lines that have been added or removed from a file using the
git diff command.

Example:
git diff
or 
git difftool, 
    this will open the code editor and show us the changes in a more visual way
    (This is configure in the terminal with this commands:
        git config --global diff.tool vscode
        diwsgen@fedora-dev:~$ git config --global difftool.vscode.cmd "code --wait --diff $LOCAL $REMOTE"
        diwsgen@fedora-dev:~$ git config --global -e
    the last command is only to verify that the changes have been made correctly)

IMPORTANT TO USE THIS WE DO NOT NEED TO USE 
git add, because if we do then we will not see the changes in the file, we will only see the changes that have been staged, 
so we need to use git diff before we add the changes to the staging area

also if there are more files that have been modified we can use:
git difftool --staged

'''


'''
See in the history of the changements we have made to the repository using the following command:
git log
or
git log --oneline --reverse (or without --reverse) to see the changes in a more visual way,
'''

'''
Seeing a commit

git show <commit_hash>, this commit_hash is on git log --oneline, this will show us the changes that have been made in that commit,
Also if we do not have this hash or we wanted to do it in another way we can use

git show HEAD~<number_of_commits>,
example: git show HEAD~1, this will show us the changes that have been made in the last commit,
'''


'''
Unstaging Changes

git restore 

this is for restoring the changes that we have made to a file, for example if we have modified a file and we want to restore it to the last commit we can use:
git restore <file_name>

we can use it with --staged to restore the changes that we have staged, 
for example if we have added a file to the staging area and we want to remove it from there we can use:

git restore --staged <file_name>

'''

'''
Discarding local Changes

we can use: git clean 
but this is dangerous because it will delete all the untracked files in the repository, 
so we need to be careful when using this command, 
we can use it with -n to see what files will be deleted without actually deleting them, for example:
git clean -n

and if we canted to deleate the files we can use:
git clean -fd
this will delete all the untracked files and directories in the repository,
we can use it with -x to delete all the untracked files including the ones that are in the .gitignore file, for example:
git clean -fdx

But again this is danguerous 

'''


'''
Restoring a file to a previous commit

After we have deleting a file and we wanted to restore it to a previous commit we can use the following command:
    git restore --source=HEAD~<number_of_commits> <file_name>
or if was the last commit we can use:
    git restore --source=HEAD~1 <file_name>
And with that the file will be restored to the previous commit, we can check the status of the repository using git status and we will see that the file is in the staging area, so we need to commit the changes to restore the file to the repository

other version of git restore is
git restore --source=<commit_hash> <file_name>
'''