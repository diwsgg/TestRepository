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
git status -m "removing file from the repository"

To sum up the steps to delete a file from the repository we can do the following:
1. Remove the file from the working directory using rm <file_name>
2. Check the status of the repository using git status
3. Remove the file from the staging area using git add <file_name>
4. Check the status of the repository using git status
5. Commit the changes using git commit -m "removing file from the repository"

BUT THIS IS NO THE BEST OPTION SO WE CAN USE

******* git rm <file_name> *******
and that will be the best option to remove a file from the repository since it will remove the file from the working directory and the staging area at the same time

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
git diff --staged

'''