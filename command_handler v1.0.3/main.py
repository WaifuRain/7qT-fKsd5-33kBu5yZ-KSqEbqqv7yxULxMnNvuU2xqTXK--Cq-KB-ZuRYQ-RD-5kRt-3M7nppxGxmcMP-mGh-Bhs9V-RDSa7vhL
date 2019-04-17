import commands
import get_cmd as get


def check_cmd_exists(cmd):
    if cmd in commands.command_list:
        return True
    else:
        return False


while True:
    command, args = get.get_cmd()
    # print(f"main() ; cmd = {command} , args = {args}")
    if check_cmd_exists(command):
        if args != '':
            commands.command_list[command](args)
        else:
            commands.command_list[command]()
    else:
        print(f"Command '{command}' does not exist! Type 'help' for a list of available commands.")
