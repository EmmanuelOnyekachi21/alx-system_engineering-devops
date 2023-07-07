#!/bin/bash

# automates directory creation.
echo "Enter Directory Name: "
read -r dir

# Checks if entered string is empty.
# DOuble square bracket is only for functionality.

if [[ -z "$dir" ]]; then	
	echo "Directory name cannot be empty."
	exit 1
fi

# Checks if directory input contains invalid inputs
if [[ "$dir" =~ [^a-zA-Z0-9_-] ]]; then
	echo "Directory name contains invalid characters.  Only alphanumeric, underscore, and hyphen are allowed."
	exit 1
fi

# Create the directory and handles error.
mkdir "$dir" || { echo "Failed to create directory."; exit 1;}

# Copies the script, 'git.sh' to the To-be created dirrectory/
cp git.sh "$dir" || { echo "Failed to copy script to directory!"; exit 1;}

# Change into newly created diretory;
cd "$dir" || { echo "Failed to change into directory."; exit 1; }

# Launch vi for writing the README
echo "Launch vi editor to write the README.  Press Enter to continue. "
read

vi README.md
