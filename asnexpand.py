#!/usr/bin/env python3

"""
Retrieves the AS number for one or more hostnames or IP addresses, then expands it into a list of CIDR ranges associated with that ASN.

$ cat targets.txt | asnexpand
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

def ip_to_asn(ip):
	try:
		query = ipwhois.IPWhois(ip)
		as_number = query.lookup_whois()["asn"]

		asn_origin = ipwhois.asn.ASNOrigin(query.net)
		asn = asn_origin.lookup(as_number)
		return asn
	except ipwhois.exceptions.IPDefinedError:
		return None

if __name__ == "__main__":
	for host in sys.stdin:
		ip = host_to_ip(host.strip())

		if ip is None:
			continue

		results = ip_to_asn(ip)
		for network in results["nets"]:
			output = {}
			output["as_number"] = results["query"]
			output["asn"] = network["description"]
			output["cidr"] = network["cidr"]
			print(json.dumps(output))
