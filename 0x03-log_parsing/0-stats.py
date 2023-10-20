#!/usr/bin/python3
"""0-stats module"""
import sys


def print_message(size, status_dict):
    """printing the message well formatted"""
    print(f"File size: {size}")
    for key, value in status_dict.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    count = 1
    size = 0
    statuses_dict = {
        "200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0,
        "500": 0
    }
    for line in sys.stdin:
        line_spli = line.split()
        size += int(line_spli[-1])  # get the size of the current line
        status = line_spli[-2]  # get the status code of the current line
        statuses_dict[status] = statuses_dict[status] + 1
        if count == 10:
            print_message(size, statuses_dict)
            size = 0
            count = 0
            statuses_dict = {
                "200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
                "405": 0, "500": 0
            }
        count += 1
