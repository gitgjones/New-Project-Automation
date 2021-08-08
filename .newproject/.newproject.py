import os
import sys
import subprocess
from github import Github

# Build project path from Project direcotry and New project name
newProjectPath = os.path.join(os.environ['PROJECT_DIR'],sys.argv[1])

# Check if desired directory name already exists
if os.path.isdir(newProjectPath):
    print ("The directory already exists, please try again.")
    exit
else:
    # Create directory and startup files
    try:
        os.makedirs(newProjectPath)
        os.chdir(newProjectPath)
        f = open("README.md", "w")
        f.close()
        f = open(".env", "w")
        f.close()
        f = open(".gitignore", "w")
        f.write(".env")
        f.close()
    except:
        print ("Something went wrong creating the directory/files.")
        print ("Error: ",sys.exc_info()[0])
        exit

    # Initialise git, create a GitHub repo and initial commit/push
    try:
        output = subprocess.check_output(["git", "init"])
        g = Github(os.environ['GIT_TOKEN'])
        u = g.get_user()
        repo = u.create_repo(sys.argv[1])
        output = subprocess.check_output(["git", "remote", "add", "origin", repo.clone_url]) 
        output = subprocess.check_output(["git", "add", "."])
        output = subprocess.check_output(["git", "commit", "-m", "\"Initial commit\""])
        output = subprocess.check_output(["git", "push", "origin", "master"])
    except:
        print ("Something went wrong initialising git/GitHub.")
        print ("Error: ",sys.exc_info()[0])
        exit