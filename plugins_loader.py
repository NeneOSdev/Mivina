loaded_plugins = []

def load_plugins():
    import os, importlib.util

    plugins_dir = "plugins"

    if not os.path.exists(plugins_dir):
        os.mkdir(plugins_dir)
        return

    for filename in os.listdir(plugins_dir):
        if not filename.endswith(".py"):
            continue

        name = filename[:-3]
        path = os.path.join(plugins_dir, filename)

        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "init"):
            module.init()
            loaded_plugins.append(name)
