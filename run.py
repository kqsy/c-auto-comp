import os, sys, subprocess

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
    filetype = file.split(".")[-1].lower() # gets file extension / filetype from <file> string
    if (filetype not in conversion): # thrown if input file-to-convert is not C or C++
        sys.exit("Invalid file type") # closing script, as to not try to convert other filetypes
    if (not os.path.exists(filepath)): # gets handled by compiler(s), as well
        sys.exit("File does not exist")
    compiler = conversion[filetype]
    if (" " in filepath):
        filepath = f'"{filepath}"' # dir space handeling
    command = subprocess.Popen(f"{compiler} -o {filename}.exe {filepath}", # equivalent to running command in terminal,
        shell=True, stdin=-1, stdout=-1, stderr=-1) # but as a hidden subprocess of this script / process
    execute = f"{filename}.exe" # add "start" to beginning of command if having issues
    returned = str(command.stdout.read() + command.stderr.read())[2:-1] # gets command response from Popen function as a string
    exists = os.path.exists(os.path.join(os.path.curdir, f"{filename}.exe"))
    if (returned == ""):
        if (exists): # checks if file was compiled to current path
            os.system(execute) # runs script after compiling
        else:
            sys.exit("Could not locate compiled file")
    else:
        sys.exit(returned)
except KeyboardInterrupt:
    sys.exit("\n\nA key was pressed") # handles user keystroke inputs like Ctrl+C, Ctrl+X, etc.
except Exception as e:
    sys.exit(str(e)) # displays error message to user as exit code, upon closing
