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

def loadAddresses(filename='addresses.json'):
    global addresses
    with open(filename, 'r') as fin:
        addresses = json.load(fin)

def discoverDevices():
    global addresses
    res = p3.CIPDriver.discover()
    
    with open('raw_discover.json', 'w+') as fout:
        json.dump({'res': res}, indent='\t')

    for element in res:
        addresses[element['serial']] = element['ip_address']

    with open('addresses.json', 'w+') as fout:
        json.dump(addresses, indent='\t')


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

    discoverDevices()

    for ip in addresses.values():
        discoveryTags(ip)

    with open('tags.json', 'w+') as fout:
        json.dump(tags, indent='\t')
