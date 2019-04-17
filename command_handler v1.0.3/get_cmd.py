import os


def get_cmd():
    user_input = input(f"{os.getcwd()}>")
    return separate_command(user_input)


def separate_arguments(args):
    arguments = ' '.join(args)
    return arguments


def separate_command(cmd):
    command = cmd.split(' ')[0]
    arguments = separate_arguments(cmd.split(' ')[1:])
    return command, arguments
