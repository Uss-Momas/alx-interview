#!/usr/bin/python3
"""0-stats module"""
import sys


def print_message(size, status_dict):
    """printing the message well formatted
    """
    print("File size: {}".format(size))
    for key, value in sorted(status_dict.items()):
        if value != 0:
            print("{}: {}".format(key, value))


count = 0
size = 0
statuses_dict = {
        "200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0,
        "500": 0}

try:
    for line in sys.stdin:
        line_split = line.split()

        if len(line_split) > 2:
            count += 1

            if count <= 10:
                # get the size of the current line
                size += int(line_split[-1])
                # get the status code of the current line
                status = line_split[-2]

                if status in statuses_dict.keys():
                    statuses_dict[status] += 1
            if count == 10:
                print_message(size, statuses_dict)
                count = 0

finally:
    print_message(size, statuses_dict)
