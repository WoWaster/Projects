# import csv
import re
import sys
from typing import Dict, List

import requests
from requests.models import Response


def user_ip() -> str:
    """Get user's ip.

    Returns:
        str: user's ip
    """
    r: Response = requests.get("https://httpbin.org/ip")  # type: ignore
    return r.json()["origin"]  # type: ignore


def check_country(ip: str) -> Dict[str, str]:
    """Finds out from what country given ip originates from.

    Args:
        ip (str): ip to investigate.

    Returns:
        str: Country origin of ip.
    """

    # Check if IP is in correct form.
    if not re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip):
        return {"country": "Incorrect ip, use 'xxx.xxx.xxx.xxx' format.", "city": ""}

    r = requests.get(f"https://www.iplocate.io/api/lookup/{ip}")  # type: ignore
    keys: List[str] = ["country", "city"]
    location: Dict[str, str] = {x: r.json()[x] for x in keys}  # type: ignore
    return location


if __name__ == "__main__":
    info: str = """Country from IP Lookup

USAGE
  country_from_IP_lookup [-c] <ip address>

ARGUMENTS
  <ip address>      IP address to lookup in format 'xxx.xxx.xxx.xxx'

GLOBAL OPTIONS
  -c                Print city in addition

AVAILABLE COMMANDS
  whereami          Checks country based on yours(users) ip"""
    if len(sys.argv) == 1:
        print(info)
    elif len(sys.argv) == 2:
        if sys.argv[1] == "whereami":
            print("Country:", check_country(user_ip()).get("country"))
        else:
            print("Country:", check_country(sys.argv[1]).get("country"))
    elif len(sys.argv) == 3 and sys.argv[1] == "-c":
        if sys.argv[2] == "whereami":
            print("Country:", check_country(user_ip()).get("country"))
            print("City:", check_country(user_ip()).get("city"))
        elif sys.argv[2]:
            print("Country:", check_country(sys.argv[2]).get("country"))
            print("City:", check_country(sys.argv[2]).get("city"))
    else:
        print("Incorrect arguments.")

# TODO: Redo getting city and country
# TODO: Check IP to be correct: check stackoverflow
