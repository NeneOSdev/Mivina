import mivina
import os
import socket
import shlex

#import base64
hostname = print(socket.gethostname())
def minit_help():
    print("write = print ur text\n"
        "help = this list\n"
        "bs64 = base64\n"
        "inf = info\n"
        "ld = list\n"
        "cd = cd\n"
        "mt91 = minit91 encode and decode ur text")
def minit_write(args, stdin):
    return ' '.join(args)
def minit_exit():
    print("goodbye!")
    exit()

def minit_b64(args, stdin):
    import base64
    ec = stdin.encode() if stdin else "".join(args).encode()
    if "-d" in args:
        return base64.b64decode(ec).decode(errors="ignore")
    else:
        return base64.b64encode(ec).decode()  
    

def minit_ld():
    dir_list = os.listdir(cd)
    print(dir_list)

def minit_inf():
    print(version)
    print(hostname)

def minit_cd(args):
    if not args:
        print("{}Error".format(colors.RED), ": missing path")
        return
    try:
        os.chdir(args[0])
    except FileNotFoundError:
        print(f"cd: No such directory: {args[0]}")
    except FileNotFoundError:
        print(f"cd: Its not a directory: {args[0]}")
    except PermissionError:
        print(f"cd: Permission denied: {args[0]}")

def minit_minit91(args, stdin):
    import minit91
    mode, *text = line.split(maxsplit=1)
    text = text[0] if text else ""
    text = text.lower()
    if "-e" in args:
        return minit91.encrypt(text)

    elif "-d" in args:
        return minit91.decrypt(text)

def minit_mota(args, stdin):
    print("press f\n",
    "qdd~6;¼¼6iiN1?cd1=7c?¼2N¼qc?2")



commands = {
    "help" : minit_help, 
    "write": minit_write,
    "bs64" : minit_b64,
    "ld" : minit_ld,
    "exit" : minit_exit,
    "info" : minit_inf,
    "cd" : minit_cd,
    "mt91" : minit_minit91,
    "mota" : minit_mota
}
#func(args: list[str], stdin: str|None)->str


while True:
    try:
        line = input("<{}@mivina> $ ".format(hostname).format()).strip()
    except KeyboardInterrupt:
        print("\nexit")
        break
    if not line:
        continue

    backslash = [x.strip() for x in line.split("|")]

    stdin = None
    for stage in backslash:
        parts = stage.split()
        minit = parts[0]
        args = parts[1:]

    if minit not in commands:
        print(f"Error: command '{minit}' not found.")

    
    stdin = commands[minit](args, stdin)
    if stdin is not None:
        print(stdin)