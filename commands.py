import mivina
import os
import socket
import shlex
import datetime
user = os.getlogin()
version = "0.0.7"
hostname = print(socket.gethostname())
def minit_help(args, stdin):
    print("write = print ur text\n"
        "help = this list\n"
        "bs64 = base64\n"
        "inf = info\n"
        "ld = list\n"
        "cd = cd\n"
        "mt91 = minit91 encode and decode ur text")
def minit_write(args, stdin):
    return ' '.join(args)
def minit_exit(args, stdin):
    print("goodbye!")
    exit()

def minit_b64(args, stdin):
    import base64
    ec = stdin.encode() if stdin else "".join(args).encode()
    if "-d" in args:
        return base64.b64decode(ec).decode(errors="ignore")
    else:
        return base64.b64encode(ec).decode()  
    

def minit_ld(args, stdin):
    dir_list = os.listdir()
    print(dir_list)

def minit_inf(args, stdin):
    print(version)
    print(hostname)

def minit_cd(args, stdin):
    if not args:
        print("Error: missing path")
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
    
    elif "4?_f4|_¼{" in text:
        print("[ATTENTION] if u write it in linux, ur all data will be deleted")
        print("you sure? write 'yes' if u want")
        input()
        if input == "yes":
            exit()




def minit_mota(args, stdin):
    print("press f\n",
    "qdd~6;¼¼6iiN1?cd1=7c?¼2N¼qc?2")

def minit_time(args, stdin):
    time = datetime.datetime.now()
    print(time)

def minit_about(args, stdin):
    print("Mivina", version,
    "by NeneOSdev\n",
    "if u want support project or help with coding,\n",
    "send message to telegram: @Ov3r1n4ik\n",
    "or in matrix: @bomzherez:matrix.org\n",
    "thanks for everything! ^^")




commands = {
    "help" : minit_help, 
    "write": minit_write,
    "bs64" : minit_b64,
    "ld" : minit_ld,
    "exit" : minit_exit,
    "info" : minit_inf,
    "cd" : minit_cd,
    "mt91" : minit_minit91,
    "mota" : minit_mota,
    "time" : minit_time,
    "about" : minit_about
}
#func(args: list[str], stdin: str|None)->str


while True:
    try:
        line = input("<{}@mivina> $ ".format(user).format()).strip()
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


    
    stdin = commands[minit](args, stdin)
    if stdin is not None:
        print(stdin)
