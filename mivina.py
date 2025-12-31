import base64
import os
import socket
import commands
import curses
import cfonts
import random
import importlib.util
from plugins_loader import load_plugins

load_plugins()

user = os.getlogin()
splash = ["try Extera Next!", "Bingo!", "write Hello {}!".format(user),
"Sore no sakana!"]
random_splash = random.choice(splash)
version = "0.0.8"
cd = os.getcwd()
hostname = print(socket.gethostname())
print(cfonts.render("Mivina", font='block', size=(80, 24), colors=0, background='transparent',
align='left', letter_spacing=None, line_height=1, space=True, max_length=0, gradient=None, independent_gradient=False,
transition=False))
print("Welcome to Mivina", version, "!")
print("write 'help' for info and 'exit' for exit.")
print(random_splash)


