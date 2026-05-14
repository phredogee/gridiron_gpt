#gridiron_gpt/provider_guard.py

from importlib.metadata import version, PackageNotFoundError

def detect_installed_providers():
    providers = []
    for name in ["mistral", "openai"]:
        try:
            version(name)
            providers.append(name)
        except PackageNotFoundError:
            pass
    return providers or ["unknown"]
