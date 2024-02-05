import platform
import socket
import os
import psutil

# Define the color mappings (ANSI escape codes)
COLOR_MAPPINGS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m"
}

color_sequence = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

def get_system_info():
    info = {
        "OS": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "RAM": str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    }
    return info

def print_colored(text, color):
    print(f"{COLOR_MAPPINGS.get(color, COLOR_MAPPINGS['white'])}{text}{COLOR_MAPPINGS['reset']}")

def display_system_info():
    system_info = get_system_info()
    color_index = 0
    for key, value in system_info.items():
        print_colored(f"{key}: {value}", color_sequence[color_index % len(color_sequence)])
        color_index += 1

if __name__ == "__main__":
    display_system_info()
