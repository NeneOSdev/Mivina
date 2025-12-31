import os
import json
import urllib.request
from mivina_api import register_command
PLUGINS_URL = "https://raw.githubusercontent.com/NeneOSdev/mivina-plugin-repo/master/plugins.json"

def fetch_plugins():
    with urllib.request.urlopen(PLUGINS_URL) as r:
        return json.loads(r.read().decode())

PLUGIN_DIR = "plugins"
RAW_BASE = "https://raw.githubusercontent.com/NeneOSdev/mivina-plugin-repo/master/"

def plugin_install(name):
    plugins = fetch_plugins()
    print(plugins)
    print(name)

    if not name in plugins:
        print("Plugin not found")
        return

    url = RAW_BASE + plugins[name]["file"]
    os.makedirs(PLUGIN_DIR, exist_ok=True)

    path = os.path.join(PLUGIN_DIR, f"{name}.py")

    urllib.request.urlretrieve(url, path)
    print(f"Plugin '{name}' installed")

def plugin_remove(name):
    path = f"plugins/{name}.py"
    if os.path.exists(path):
        os.remove(path)
        print("Removed")
    else:
        print("Plugin not installed") 

PLUGIN_COMMANDS = {
    "install": lambda  args: plugin_install(args[0]),
    "remove": lambda  args: plugin_remove(args[0]), 
}

def plugin(args, minit):
    if not args:
        print("Usage: plugin <action> [args]")
        return 

    actions = args[0]
    rest = args[1:]
    func = PLUGIN_COMMANDS.get(actions)
    if not func:
        print("Unknown plugin command")
        return

    #func(args)
    result = func(rest)
    return result or minit


def init():
    register_command("plugin", plugin)

