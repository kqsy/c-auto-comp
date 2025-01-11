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
Can type absolute or relative path to file (if in same directory),
paste directories, drag-and-drop a file, or open a c or c++ file
with the script to compile it.

# Prerequisites
* Have Python[3] installed
* Libraries _os_ and _sys_
  
  can be installed via pip, Conda, etc.
  
  `pip3 install os sys`
* GCC and G++ package

  > on Ubuntu, commands already exist
  
  > on Windows, user will need to install
  [w64devkit](https://github.com/skeeto/w64devkit/releases/latest)
  and add **w64devkit\bin** to "Path" in Environment Variables
  
