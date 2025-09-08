# phred/cli/registry.py

COMMAND_REGISTRY = {}

def register_command(name, help_text=""):
    def decorator(func):
        COMMAND_REGISTRY[name] = {"func": func, "help": help_text}
        return func
    return decorator