#!/usr/bin/env python

import sys
import re
import json
from collections import Counter, OrderedDict

if len(sys.argv) < 2:
    print("Please provide the filename to parse as an argument!")
    exit(1)

try:
    file = open(sys.argv[1], "r")
except:
    print(f"File not found: {sys.argv[1]}")
    exit(1)

# get all ip matches
ips = []
for line in file:
    result = re.match(r"^([0-9]{1,3}(?:\.[0-9]{1,3}){3}) -", line)
    if result:
        ips.append(result.group(1))

# create ordered mapping of counts
orderedIps = OrderedDict(Counter(ips).most_common())

# write json file
with open("./results.json", "w") as jsonFile:
    json.dump(orderedIps, jsonFile, indent=2)

print("Successfully aggregated log and wrote ./results.json")
