# 0x02-shell_redirections

This project contains shell scripts that demonstrate the usage of shell redirections in Linux. Shell redirections allow you to control the input and output streams of commands, enabling you to redirect input from files, redirect output to files, and combine commands to achieve powerful operations.

## Scripts

The following scripts are included in this project:

1. **0-hello_world**: This script demonstrates the basic usage of output redirection. It prints "Hello, World!" to the standard output.

2. **1-confused_smiley**: This script redirects the output of a command to a file. It runs a command that generates a confused smiley `"(Ôo)'` and saves it to a file called `confused_smiley`.

3. **2-hellofile**: This script demonstrates input redirection. It reads the contents of a file called `holberton` and displays it on the standard output.

4. **3-twofiles**: This script shows how to combine input and output redirections. It reads the contents of a file called `holberton` and appends it to another file called `holberton`.

5. **4-lastlines**: This script demonstrates the usage of `tail` command with input redirection. It displays the last 10 lines of a file called `iacta`.

6. **5-firstlines**: This script uses the `head` command with input redirection to display the first 10 lines of a file called `iacta`.

7. **6-third_line**: This script extracts and displays the third line of a file called `iacta` using the `head` and `tail` commands with input redirection.

8. **7-file**: This script creates a file called `\*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:)` that contains the text "Holberton School" followed by a new line.

9. **8-cwd_state**: This script writes the result of the command `ls -la` into a file called `ls_cwd_content`. It shows the current directory's contents.

10. **9-duplicate_last_line**: This script duplicates the last line of a file called `iacta` and saves the duplicated line to a new file called `iacta`.

11. **10-no_more_js**: This script deletes all the regular files with a `.js` extension in the current directory and its subdirectories.

12. **11-directories**: This script counts the number of directories and sub-directories in the current directory (excluding the hidden ones).

## Usage

To run any of the scripts, navigate to the project directory and execute the desired script using the following syntax:

```shell
./script_name
Replace script_name with the name of the script you want to run.

Feel free to explore the scripts and experiment with different redirection techniques to deepen your understanding of shell redirections.
