import argparse
import time
import psutil
import platform
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.live import Live

console = Console()

# ------------------ CLI Argument ------------------ #
def get_args():
    parser = argparse.ArgumentParser(description="Terminal System Dashboard")
    parser.add_argument("--light", action="store_true", help="Enable light mode theme")
    return parser.parse_args()

# ------------------ Theme Config ------------------ #
def get_theme(light_mode=False):
    if light_mode:
        return {
            "title": "black",
            "border": "bright_white",
            "label": "blue",
            "value": "black",
            "highlight": {
                "low": "green",
                "mid": "yellow",
                "high": "red"
            }
        }
    else:
        return {
            "title": "bold magenta",
            "border": "bright_blue",
            "label": "cyan",
            "value": "green",
            "highlight": {
                "low": "green",
                "mid": "yellow",
                "high": "red"
            }
        }

# ------------------ Usage Colorizer ------------------ #
def colorize_usage(percent, theme):
    percent = float(percent)
    if percent > 80:
        color = theme["highlight"]["high"]
    elif percent > 50:
        color = theme["highlight"]["mid"]
    else:
        color = theme["highlight"]["low"]
    return f"[{color}]{percent:.1f}%[/{color}]"

# ------------------ System Info ------------------ #
def get_system_info():
    return {
        "OS": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor()
    }

def get_cpu_info(theme):
    return {
        "CPU Usage": colorize_usage(psutil.cpu_percent(), theme),
        "Cores": psutil.cpu_count(logical=False),
        "Threads": psutil.cpu_count(logical=True)
    }

def get_memory_info(theme):
    mem = psutil.virtual_memory()
    return {
        "Total": f"{mem.total // (1024**2)} MB",
        "Used": f"{mem.used // (1024**2)} MB",
        "Usage": colorize_usage(mem.percent, theme)
    }

def get_disk_info(theme):
    disk = psutil.disk_usage('/')
    return {
        "Total": f"{disk.total // (1024**3)} GB",
        "Used": f"{disk.used // (1024**3)} GB",
        "Usage": colorize_usage(disk.percent, theme)
    }

def get_top_process(theme):
    processes = [(p.info["cpu_percent"], p.info["name"]) for p in psutil.process_iter(['name', 'cpu_percent'])]
    top = sorted(processes, reverse=True)[0]
    return {
        "Process": top[1],
        "CPU %": colorize_usage(top[0], theme)
    }

# ------------------ Table Builder ------------------ #
def build_table(theme):
    table = Table(title="🖥️ Terminal Dashboard", style=theme["title"])
    table.add_column("Category", style=theme["label"], justify="right")
    table.add_column("Info", style=theme["value"])

    sections = [
        ("🧠", get_system_info()),
        ("⚙️", get_cpu_info(theme)),
        ("💾", get_memory_info(theme)),
        ("📀", get_disk_info(theme)),
        ("🔥 Top CPU Process", get_top_process(theme))
    ]

    for icon, info in sections:
        for label, value in info.items():
            table.add_row(f"{icon} {label}", str(value))

    return table

# ------------------ Dashboard Runner ------------------ #
def run_dashboard():
    args = get_args()
    theme = get_theme(light_mode=args.light)

    with Live(console=console, refresh_per_second=1):
        while True:
            table = build_table(theme)
            panel = Panel(table, title="📊 System Monitor", border_style=theme["border"])
            console.clear()
            console.print(panel)
            time.sleep(1)

# ------------------ Entry Point ------------------ #
if __name__ == "__main__":
    run_dashboard()
