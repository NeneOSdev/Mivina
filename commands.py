import subprocess
import mivina
import os
import socket
import shlex
import sys
import datetime
import random
import string
user = os.getlogin()
 #REPO_URL="https://github.com/NeneOSdev/Mivina.git"
version = "0.0.7_02"
hostname = print(socket.gethostname())

def minit_clear(args, stdin):
    print("\033[2J\033[H")
def minit_help(args, stdin):
    print("write = print ur text\n"
        "help = this list\n"
        "bs64 = base64\n"
        "inf = info\n"
        "ld = list\n"
        "cd = cd\n"
        "mt91 = minit91 encode and decode ur text\n"
        "about = about the project\n"
        "time = when school?")
def minit_write(args, stdin):
    return '" "'.join(args)
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
    


'''def minit_check_repo(args, stdin):
    try:
        subprocess.check_output(
            ["git", "rev_parse", "--is-inside-work-tree"],
            stderr = subprocess.DEVNULL
        )
        return True
    except subprocess.CalledProcessError:
        return False

    def minit_get_update(args, stdin):
        subprocess.run(
            ["git", "fetch"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        local = subprocess.check_output(
            ["git", "rev-parse", "HEAD"] 
        ).decode().strip()

        remote = subprocess.check_output(
            ["git", "rev-parse", "@{u}"]
        ).decode().strip()

        return local, remote

def check_updates(args, stdin):
    if not minit_check_repo(args, stdin):
        print("Mivina: its not a repository.")
        return

    local, remote = minit_get_update()

    if local != remote:
        print("Mivina: Update available!")
        print("Mivina: write update to update Mivina")
    else:
        print("Mivina: already up to date")

def minit_update(args, stdin):
    if not minit_get_update:
        print("Mivina: cannot update (no git repo)")
        return

    subprocess(["git", "pull"])

def init_repo(args, stdin):
    if not minit_check_repo(args, stdin):
        subprocess.run(["git", "init"])
        subprocess.run(["git", "remote", "add", "origin", 
        
        "https://github.com/NeneOSdev/Mivina.git"])
'''
def minit_checkFile(args, stdin):
    if os.patch.exists("lamroN.py"):
        print("[Warning]: accepted")
    else:
        print("[Error]: Permission Denied")

def minit_lamron(args, stdin):
    import lamron
    l = lamron()
    l.start()

def minit_ld(args, stdin):
    dir_list = os.listdir()
    print(dir_list)

def minit_inf(args, stdin):
    print(version)
    print(hostname)

def minit_cd(args, stdin):
    if len(args) ==0:
        os.chdir(os.environ["HOME"])
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
        if input() == "yes":
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
    "=============================================\n",
    "if u want support project or help with coding,\n",
    "send message to telegram: @Ov3r1n4ik\n",
    "or in matrix: @bomzherez:matrix.org\n",
    "=============================================\n",
    "thanks for everything! ^^")

def minit_mkdir(args, stdin):
    path = args[0] 
    os.mkdir(path)

def minit_eqqpsd(args, stdin):
    
    psdg = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    print("Password for eqq:", psdg)
    
    
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
    "about" : minit_about,
    #"update" : minit_update,
    #"check-update" : check_updates,
    "mkdir" : minit_mkdir,
    "eqqpsd" : minit_eqqpsd,
    "ewq" : minit_checkFile,
    "lamron" : minit_lamron,
    "clear" : minit_clear
}
#func(args: list[str], stdin: str|None)->str


while True:
    try:
        line = input("<{}@mivina> $ ".format(user).format()).strip()
        backslash = [x.strip() for x in line.split("|")]

        stdin = None
        minit = None
        for stage in backslash:
            parts = stage.split()
            minit = parts[0]
            args = parts[1:]
        stdin = commands[minit](args, stdin)
        if stdin is not None:
            print(stdin)

    except KeyboardInterrupt:
        print("\nexit")
        break
    if not line:
        continue

 