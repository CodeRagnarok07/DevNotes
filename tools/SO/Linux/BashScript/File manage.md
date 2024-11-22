


file_path=./dir
file_Path_Items=./dir/* # is a iterable echo only take the first
complete_File_Path="$filepath"



### Checks files
`True or False`

Is_Dir= -d $filepath 




### Bash Test Operators[](https://earthly.dev/blog/bash-conditionals/#bash-test-operators)

Now that you, hopefully, understand how Bash’s test commands work, you can learn how to form test expressions. The core of the expressions is _test operators_. If you want to take full advantage of conditionals, you need to have a healthy understanding of them.

Bash has a large variety of test operators that apply to different variable types and situations. These operators are just flags passed to the test commands and include the following:

#### Compounding Comparison Operators[](https://earthly.dev/blog/bash-conditionals/#compounding-comparison-operators)

Compounding comparison operators allow you to combine test expressions. They return a value based on a test performed on multiple expressions:

- **`-a`:** is the _and_ operator. It lets you test multiple conditions and returns true if all conditions are true (_ie_ if `[ $n -gt 10 -a $n -lt 15 ]`).
- **`-o`:** is the _or_ operator. It lets you test multiple conditions and returns true if one or more conditions are true (_ie_ if `[ $n -gt 10 -o $n -lt 15 ]`).

#### Integer Comparison Operators[](https://earthly.dev/blog/bash-conditionals/#integer-comparison-operators)

Integer comparison operators let you build expressions that compare whole numbers in Bash:

- **`-eq`:** tests if two values/variables are equal (`=` or `==`)
- **`-ne`:** checks if two values/variables are not equal (`!=`)
- **`-gt`:** checks if one value is greater than another (`>`)
- **`-ge`:** checks if one value is greater than or equal to another (`>=`)
- **`-lt`:** checks if one value is less than another (`<`)
- **`-le`:** checks if one value is equal or less than another (`<=`)

> You can use the symbols (`<`,`>`,`=`,`!=`, etc.) in place of the above word-based operators when using the `[[` built-in.

#### String Evaluation Operators[](https://earthly.dev/blog/bash-conditionals/#string-evaluation-operators)

String evaluation operators let you compare and evaluate strings of text in Bash:

- **`==` or `=`:** checks if two strings are equal
- **`!=`:** checks if two strings are not equal to each other
- **`<`:** checks if one string is less than another using the ASCII sorting order
- **`>`:** checks if one string is greater than another using the ASCII sorting order
- **`-z`:** returns true if the string is empty or null (has a length of zero)
- **`-n`:** returns true if a string is not null

#### File Evaluating Operators[](https://earthly.dev/blog/bash-conditionals/#file-evaluating-operators)

These advanced operators let you assess and compare files in Bash:

- **`-e`:** validates the existence of a file (returns true if a file exists)
- **`-f`:** validates if the variable is a regular file (not a folder, directory, or device)
- **`-d`:** checks if the variable is a directory
- **`-h` (or `-L`):** validates if the variable is a file that is a symbolic link
- **`-b`:** checks if a variable is a block special file
- **`-c`:** verifies if a variable is a character special file
- **`-p`:** checks if a file is a pipe
- **`-S`:** checks if a file is a socket
- **`-s`:** verifies if the size of the file is above zero (returns true if the file is greater than 0 bytes)
- **`-t`:** validates if the file is associated with a terminal device
- **`-r`:** checks if the file has read permissions
- **`-w`:** verifies if the file has write permissions
- **`-x`:** checks if the file has execute permissions
- **`-g`:** checks if the [SGID](https://www.linux.com/training-tutorials/what-sgid-and-how-set-sgid-linux/) flag is set on a file
- **`-u`:** verifies if the [SUID](https://www.techrepublic.com/article/linux-101-what-is-the-suid-permission/) flag is set on a file
- **`-k`:** checks if the [sticky bit](https://www.thegeekstuff.com/2013/02/sticky-bit/) is set on a file
- **`-O`:** verifies if you’re the owner of a file
- **`-G`:** validates if the group ID is the same as yours
- **`-N`:** validates if a file was modified since it was last read
- **`-nt`:** compares the creation dates of two files to see if one file (file 1) is newer than the other (file 2)
- **`-ot`:** compares the creation dates of two files to verify if one file (file 1) is older than the other (file 2)
- **`-ef`:** checks if two variables are hard links to the same file