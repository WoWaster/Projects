import argparse
import re
from typing import Dict, List

import requests
from requests.models import Response


class IncorrectIP(Exception):
    """Raised when given IP is incorrect."""

    def __init__(self, ip: str) -> None:
        self.ip = ip

    def __str__(self) -> str:
        return (
            f"IP {self.ip} is invalid. Use 'xxx.xxx.xxx.xxx' format "
            "without leading zeroes."
        )


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
    ip_regex = re.compile(r"\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b")
    if not ip_regex.match(ip):
        raise IncorrectIP(ip)

    r = requests.get(f"https://www.iplocate.io/api/lookup/{ip}")  # type: ignore
    keys: List[str] = ["country", "city"]
    location: Dict[str, str] = {x: r.json()[x] for x in keys}  # type: ignore
    return location


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A program to find to what country given IP belongs.",
    )

    parser.add_argument(
        "-c", "--city", action="store_true", help="Print city where IP originates."
    )
    parser.add_argument(
        "ip_address",
        type=str,
        help="IP to investigate. Type 'whereami' to show where you are based on IP.",
    )
    args = parser.parse_args()

    if args.ip_address:
        if args.ip_address == "whereami":
            args.ip_address = user_ip()
        answer = check_country(args.ip_address)
        print(f"Country: {answer['country']}")
        if args.city:
            print(f"City: {answer['city']}")
