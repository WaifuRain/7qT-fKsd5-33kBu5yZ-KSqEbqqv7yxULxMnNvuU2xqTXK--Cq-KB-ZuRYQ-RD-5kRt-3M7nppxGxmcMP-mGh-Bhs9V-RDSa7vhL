import functions

version = '1.0.3'

command_list = {
    "cd": functions.change_directory,
    "maxdir": functions.display_max_in_directory,
    "vmaxdir": functions.verbose_display_max_in_directory,
    "cls": functions.clear,
    "make": functions.make_directory,
    "files": functions.display_files_in_directory,
    "dirs": functions.display_directories,
    "help": functions.display_help,
    "count": functions.count,
}

command_descriptions = {
    "cd": " - Change the current directory",
    "maxdir": " - List the directory with the most subfolders and files, takes one argument; (path)",
    "vmaxdir": " - List the directory with the most subfolders and files verbosely, takes one argument; (path)",
    "cls": " - Clears the console",
    "make": " - Makes a new folder, takes one argument; (folder name)",
    "files": " - Lists all files in a directory, takes one argument; (path)",
    "dirs": " - Lists all directories within a given path, takes one argument; (path)",
    "help": " - Help Command",
}
