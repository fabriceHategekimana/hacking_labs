#!/usr/bin/env python3
import sys
import json
import argparse
import re
from datetime import datetime


def process_logs(access_file, forensics_file):
    with open(access_file, 'r') as access_log, open(forensics_file, 'r') as forensics_log:
        forensics = {x['requestId']: x for x in map(
            json.loads, forensics_log.readlines())}
        prog = re.compile(
            r'^(?P<requestId>.*) (?P<remoteAddress>.*) - - \[(?P<timestamp>.*)\] "(?P<verb>[A-Z]+) (?P<url>.*) (?P<version>HTTP/.*)" (?P<status>.*) (?P<responseSize>.*)$')
        for l in access_log:
            try:
                obj = prog.match(l).groupdict()
                obj['timestamp'] = datetime.strptime(
                    obj['timestamp'], '%d/%m/%Y:%H:%M:%S %z').isoformat()
                headers = {}
                req = forensics.get(obj['requestId'])
                if not req:
                    print('Could not find request {} in forensics log.'.format(
                        obj['requestId']), file=sys.stderr)
                else:
                    for h in filter(lambda x: x != '', req['headers'].split('\n')):
                        key, value = h.split(':')
                        headers.setdefault(key, []).append(value.strip())
                obj['headers'] = headers
                write_output_log(obj)
            except Exception as e:
                print("Error {} on line {}".format(e, l), file=sys.stderr)


def write_output_log(obj):
    print(json.dumps(obj))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Process web application log files.')
    parser.add_argument(
        '-a', '--access', help='the acces log file to parse', default='access.log')
    parser.add_argument(
        '-f', '--forensics', help='the forensics log file to parse', default='forensics.json')

    args = parser.parse_args()

    process_logs(args.access, args.forensics)
