#!/usr/bin/python3
"""0-stats module"""
import sys


def print_message(size, status_dict):
    """printing the message well formatted"""
    print(f"File size: {size}")
    for key, value in status_dict.items():
        if value != 0:
            print(f"{key}: {value}")


if __name__ == '__main__':
    try:
        count = 0
        size = 0
        statuses_dict = {
            "200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
            "405": 0, "500": 0
        }
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
                    # statuses_dict = {
                    #     "200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                    # "404": 0, "405": 0, "500": 0
                    # }

    except KeyboardInterrupt:
        print_message(size, statuses_dict)
