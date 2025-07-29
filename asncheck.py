#!/usr/bin/env python3

"""
Retrieves information about the ASN associated with one or more hostnames or IP addresses.

$ cat targets.txt | asncheck
"""

import ipwhois,ipaddress,socket,sys,json

def host_to_ip(host):
	try:
		# Already an IP address?
		ip = ipaddress.ip_address(host)
		return host
	except ValueError:
		pass

	try:
		# Resolves to an IP address?
		return socket.gethostbyname(host)
	except (socket.gaierror, UnicodeError):
		pass

def ip_to_networks(ip):
	try:
		query = ipwhois.IPWhois(ip)
		results = query.lookup_whois()
		return results["nets"]
	except ipwhois.exceptions.IPDefinedError:
		return []


if __name__ == "__main__":
	for host in sys.stdin:
		ip = host_to_ip(host.strip())

		if ip is None:
			continue

		nets = ip_to_networks(ip)
		for net in nets:
			output = {}
			output["host"] = host.strip()
			output["ip"] = ip
			output["asn"] = net["description"]
			output["cidr"] = net["cidr"]
			output["range"] = net["range"]
			output["contacts"] = net["emails"]
			print(json.dumps(output))
