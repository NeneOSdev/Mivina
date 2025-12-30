commands = {}
def register_command(name, stdin):
    commands[name] = stdin

def get_commands():
    return commands

    
