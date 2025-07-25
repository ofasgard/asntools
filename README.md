# asntools

Some simple utilities that use the [ipwhois](https://pypi.org/project/ipwhois/) module to look up ASN data associated with a target or targets. I wrote these scripts to help automate some OSINT and validation tasks, making it easier to check the provenance of a host or find associated hosts.

All tools in this repository produce output in JSONL format. Use tools like `jq` to parse the output programmatically. For example, to extract a list of unique ASNs associated with a target list:

```sh
$ cat targets.txt | asncheck | jq .asn | sort -u
```

## asncheck

Retrieves information about the ASN associated with one or more hostnames or IP addresses.

```sh
$ echo "8.8.8.8" | asncheck
$ cat targets.txt | asncheck
```

## asnexpand

Retrieves the AS number for one or more hostnames or IP addresses, then expands it into a list of CIDR ranges associated with that ASN.

```sh
$ echo "8.8.8.8" | asnexpand
$ cat targets.txt | asnexpand
```
