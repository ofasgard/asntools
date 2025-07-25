#!/usr/bin/env python3

"""
A helper tool that expands the CIDR ranges from asncheck or asnexpand into a full list of IP addresses.

$ cat targets.txt | asncheck | jq -r .cidr | cidrexpand
"""

import ipaddress,json,sys

if __name__ == "__main__":
	for cidr in sys.stdin:
		addresses = [str(ip) for ip in ipaddress.IPv4Network(cidr.strip())]
		print("\n".join(addresses))
