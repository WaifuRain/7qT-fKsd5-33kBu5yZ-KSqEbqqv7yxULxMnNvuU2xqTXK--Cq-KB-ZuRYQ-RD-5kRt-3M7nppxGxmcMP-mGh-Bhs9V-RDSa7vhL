import os
import time
import commands


def confirm(args):
    def get_valid_choice(action):
        choice = input(f"Are you sure you want to {action}? (Y/N) >")
        choice = choice.upper()
        print(choice)
        if choice != 'Y' and choice != 'N':
            print("Invalid response. Please enter (Y/N).")
        elif choice == 'Y':
            return True
        else:
            return False

    while True:
        if get_valid_choice(args):
            return True
        else:
            return False


def clear():
    os.system('cls')


def is_root():
    if os.path.dirname(os.getcwd()) == os.getcwd():
        return True
    else:
        return False


def change_directory(path=os.getcwd()):
    if path == os.getcwd():
        print(f"Missing one required arguments for command: 'cd'!")
        return
    if os.path.exists(path):
        os.chdir(path)
    else:
        print(f"Path '{path}' does not exist!")


def calc_process_time(start):
    return f"\nProcess finished in: {(time.time() - start)} seconds."


def max_dir(v):
    max_length = 0
    max_list_name = ''
    if v == 1:
        for dirpath, dirnames, filenames in (os.walk(os.getcwd())):
            print(f"Directory {dirpath}")
            print(f"Directories {dirnames}")
            print(f"Files: {filenames}")
            if len(list(dirnames)) > max_length:
                max_length = len(list(dirnames))
                max_list_name = dirpath
    else:
        for dirpath, dirnames, filenames in (os.walk(os.getcwd())):
            if len(list(dirnames)) > max_length:
                max_length = len(list(dirnames))
                max_list_name = dirpath
    return max_length, max_list_name


def display_max_in_directory(args=''):
    if not args == '':
        print("Command: 'maxdir' does not take any arguments!")
        return
    start_time = time.time()
    end_dir = os.getcwd().split('\\')[-1]
    directory_length, directory_name = max_dir(0)
    directory_name = directory_name.split('\\')
    if not is_root():
        directory_name = directory_name[directory_name.index(end_dir) + 1:]
    directory_name = '\\'.join(directory_name)

    print(f"\nThe largest directory within {os.getcwd()} is {directory_name} , with {directory_length} "
          f"sub folders and files.")
    if not is_root():
        print(f"Full Path: {os.getcwd()}\\{directory_name}")
    else:
        print(f"Full Path: {directory_name}")
    print(calc_process_time(start_time))


def verbose_display_max_in_directory(args=''):
    if not args == '':
        print("Command: 'maxdir' does not take any arguments!")
        return
    start_time = time.time()
    end_dir = os.getcwd().split('\\')[-1]
    directory_length, directory_name = max_dir(1)
    directory_name = directory_name.split('\\')
    if not is_root():
        directory_name = directory_name[directory_name.index(end_dir) + 1:]
    directory_name = '\\'.join(directory_name)

    print(f"\nThe largest directory within {os.getcwd()} is {directory_name} , with {directory_length} "
          f"sub folders and files.")
    if not is_root():
        print(f"Full Path: {os.getcwd()}\\{directory_name}")
    else:
        print(f"Full Path: {directory_name}")
    print(calc_process_time(start_time))


def make_directory(args=''):
    if args == '':
        print(f"Missing required arguments: (folder name) for command: 'make'!")
        return
    if not confirm(f'make directory {args} at location {os.getcwd()}'):
        return
    try:
        os.mkdir(args)
    except OSError:
        print(f"Creation of directory {args} failed.")
    else:
        print(f"Successfully created the directory {args}")
        print(f"Full Path: {os.getcwd()}\\{args}")


def display_files_in_directory(args=''):
    if args == '':
        print(f"Missing required arguments: (path) for command: 'files'!")
        return
    files = [f for f in os.listdir(args) if os.path.isfile(os.path.join(args, f))]
    print(f"Files in {args} : {files}")


def display_directories(args=''):
    if args == '':
        print(f"Missing required arguments: (path) for command: 'dirs'!")
        return
    dirs = [d for d in os.listdir(args) if os.path.isdir(os.path.join(args, d))]
    print(f"Directories in {args} : {print_list(dirs)}")


def print_list(list_to_print):
    count = 0
    for item in list_to_print:
        print(item)
        count += 1
    return count


def display_help():
    print(f"Version Number: {commands.version} Updated '4/15/2019 1:10AM EST'")
    print(f"Commands: {len(commands.command_list)}")
    for key in commands.command_list:
        print(f"{key} {commands.command_descriptions[key]}")


def count(args=''):
    if not args == '':
        print("Count does not take any args!")
