import os
import socket
import cfonts
import random
from plugins_loader import load_plugins
from commands import command_loop
import update_checker
import time

load_plugins()

user = os.getlogin()
splash = ["try Extera Next!", "Bingo!", "write Hello {}!".format(user),
"Sore no sakana!", "make more plugins!"]
GRAYS = list(range(232, 256)) + list(range(255, 231, -1))
def splashes():
    splashtext = random.choice(splash)

    try:
        while True:
            for c in GRAYS:
                print(f"\033[2K\033[38;5;{c}m{splashtext}\033[0m", end="\r")
                time.sleep(0.04)
    except KeyboardInterrupt:
        print("\033[0m")
    return

version = "0.0.8_02"
cd = os.getcwd()
hostname = print(socket.gethostname())
print(cfonts.render("Mivina", font='block', size=(80, 24), colors=0, background='transparent',
align='left', letter_spacing=None, line_height=1, space=True, max_length=0, gradient=None, independent_gradient=False,
transition=False))

update_checker.check_updates(version)

print("Welcome to Mivina", version, "!")
print("write 'help' for info and 'exit' for exit.")
#

command_loop() # вызываем цикл чтения команд