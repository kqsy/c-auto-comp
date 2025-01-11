import os, sys

conversion = {"c": "gcc", "cpp": "g++"} # associating appropriate language w/ compiler
try:
    if (len(sys.argv) > 1): # in the event, user opens c|cpp file with this script
        filepath = sys.argv[1] # can also be ran in the format, "[python] scriptname(.py) filename.c[pp]"
    else:
        filepath = str(input("Type / paste directory, or drag file\n\n >  "))
        print()
    if (filepath.startswith('"') & filepath.endswith('"')):
        filepath = filepath[1:-1] # removing quotes for ease of split text parsing
    filepath = os.path.normpath(filepath) # standardizing how path string is written
    file = filepath.split("\\")[-1] # gets solely filename + extension
    filename = ".".join(str(sect) for sect in file.split(".")[:-1]) # isolates script name & handles reconstructing titles like "ex1.3.c"
    filetype = file.split(".")[-1] # gets file extension / filetype from <file> string
    if (filetype not in conversion): # thrown if input file-to-convert is not C or C++
        sys.exit("Invalid file type") # closing script, as to not try to convert other filetypes
    if (not os.path.exists(filepath)): # gets handled by compiler(s), as well
        sys.exit("File does not exist")
    compiler = conversion[filetype]
    if (" " in filepath):
        filepath = f'"{filepath}"' # dir space handeling
    command = f"{compiler} -o {filename}.exe {filepath}"
    os.system(command) # equivalent to running command in terminal
except KeyboardInterrupt:
    sys.exit("\n\nA key was pressed") # handles user keystroke inputs like Ctrl+C, Ctrl+X, etc.
except Exception as e:
    sys.exit(str(e)) # displays error message to user as exit code, upon closing