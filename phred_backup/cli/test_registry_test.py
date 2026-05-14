# test_registry_test.py

# Local registry for testing
command_registry = {}

def register_command(name, handler):
    command_registry[name] = handler

def run_command(name, *args, **kwargs):
    if name not in command_registry:
        raise ValueError(f"Command '{name}' not found")
    return command_registry[name](*args, **kwargs)

def list_commands():
    return list(command_registry.keys())

# Command to test
def greet(name):
    return f"Hello, {name}!"

# Register it
register_command("greet", greet)

# Test case
def test_greet():
    result = run_command("greet", "Fred")
    print(f"🔍 Result: {result}")
    print(f"🧪 Asserting result: {repr(result)}")
    assert result == "Hello, Fred!"
    assert "greet" in list_commands()

if __name__ == "__main__":
    test_greet()
    print("✅ CLI registry test passed")
