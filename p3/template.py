#!/usr/bin/env python3
"""
Doc:
    https://docs.pycomm3.dev/en/latest/index.html
Examples:
    https://docs.pycomm3.dev/en/latest/examples/index.html

"""
import pycomm3 as p3
from time import sleep
import json

addresses = {}

tags = {}

def discoveryTags(ip):
    with p3.LogixDriver(ip) as plc:
        tags[ip] = plc.get_tag_list()
        return tags[ip]


def readTags(ip, tags):
    with p3.LogixDriver(ip) as plc:
        for tag in tags:
            print(plc.read(tag))
            sleep(.005)


def writeTag(ip, tag, val):
    with p3.LogixDriver(ip) as plc:
        plc.write(tag, val)
        sleep(.005)


if __name__ == '__main__':
    for ip in addresses.values():
        discoveryTags(ip)

    with open('tags.json', 'w+') as fout:
        json.dump(tags, indent='\t')
