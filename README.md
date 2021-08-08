# Basic automation of new coding project

## Description

Credit to KalleHallden for the idea to automate some of the initial steps when setting up a new project. I'm using OhMyZsh on a Mac with vscode so this project is specific to that setup (although as far as I can see if you're using standard bash terminal, adding the contents of the OhMyZsh custom plugin file to your .bash_profile has the same outcome). The project completes the following steps for you:

  1. Navigates to the folder you've specified (that holds all your coding projects)
  2. Creates a new directory with project name you've specified (as long as it doesn't already exist)
  3. Creates a blank .env, .gitignore (with .env included), and a blank README.md in the project folder
  4. Initiates Git in the project folder
  5. Creates a GitHub repository with the project name
  6. Adds the GitHub remote url to the project folder
  7. Completes an initial commit and push to the GitHub repository
  8. Opens up visual studio code form the project folder

## Installation

  1. Copy the .newproject folder to your 'Home' directory (careful of the '.' to make sure you copy the right folder!)
  2. Copy the newproject folder to ~/.oh-my-zsh/custom/plugins/
  3. Edit your ~/.zshrc file to add the new plugin
    - There will be a line somewhere: "plugins=(<some text here>)"
    - Simply add 'new project' to the end: "plugins=(<some text here>, newproject)"
  4. Edit the .env file to tell the script the full path of your preferred project folder, and your GitHub token

## Usage

Simply open up a zsh terminal and type "newproject <project-name>", and your basics should be set up for you!

## To Do List

Some ideas for future enhancement, that I may/may not get around to:

  1. Friendly install (e.g. copying files/folders via script and prompting user for GIT_TOKEN and PROJECT_DIR)
  2. Give user option to install on standard bash, or OhMyZsh, or both...
  3. Options for setting up different project types (e.g. python script, django website etc)

If you've made it this far, thanks for reading, and I hope there may be something useful in here for you!

-Gareth
