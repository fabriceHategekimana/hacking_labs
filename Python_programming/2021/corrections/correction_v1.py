"""
This program takes a log file as an argument, counts the occurrence of every source IP address and generates a json file with the result.
"""

import sys
import re
import json
from collections import Counter, OrderedDict

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("Specify log file as argument!")
        exit(1)

    try:
        # open log file
        with open(sys.argv[1], "r") as fin:

            # define regex pattern of source IP with terminating ' -'
            ip_paattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} -'
            # read log file
            log = fin.read()
            # create list of all lines with regex pattern
            ipregex = re.findall(ip_paattern, log)
            # create list of stripped IPs from pattern
            iplist = list()
            for i in ipregex:
                iplist.append(i.split(" ")[0])

            # create collection with ip and count per ip
            ipcount1 = Counter(iplist)
            # create ordered collection ordered by value (count)
            ipcount2 = OrderedDict(ipcount1.most_common())

            try:
                # Generating output json file
                with open('results-1.json', 'w+') as fjson:
                    json.dump(ipcount2, fjson, indent=2)

            except IOError:
                print("Could not write result file!")

    except IOError:
        print("Could not read log file!")
