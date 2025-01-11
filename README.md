# C[++] AutoCompiler
An automation of the command line compilation process for C and C++ files.

--------------------------------------------------------------------------

# Function
Script takes an input file,
parses the name, and constructs
the appropriate command to compile
the new file.
File submission is very dynamic
and should be flexible to user input.

# Prerequisites
* Have Python[3] installed
* Libraries _os_ and _sys_
  
can be installed via pip, Conda, etc.
  
`pip3 install os sys`
* GCC and G++ package

  > on Ubuntu, commands already exist
  
  > on Windows, user will need to install
  [w64devkit](https://github.com/skeeto/w64devkit/releases/latest)
  and add <u>w64devkit\bin</u> to "Path" in Environment Variables
  
