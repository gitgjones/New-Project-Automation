function newproject() {
    # Move to folder with project creation files
    cd
    cd .newproject
    # Load environment variables
    source .setenv.sh
    # Run project creation script
    python .newproject.py $1
    # Move to new project directory
    cd "$PROJECT_DIR$1"
    code .
}