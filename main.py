'''
Test for git and github as new proyect
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

'''


'''
WE have made some changes to the project and we want to push those changes to the remote repository, we can do that using the following steps:
1. Check the status of the repository using git status
2. Add the changes to the repository using git add <file_name>
3. Commit the changes using git commit -m "commit message"
4. Push the changes to the remote repository using git push

'''