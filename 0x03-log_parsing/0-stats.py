#!/usr/bin/python3
"""0-stats module"""
import random
# from time import sleep
import sys
import datetime


def generator():
    """generates test logs"""
    logs = []
    for i in range(120):
        # sleep(random.random())
        logs.append(
            "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n"
            .format(
                random.randint(1, 255), random.randint(
                    1, 255), random.randint(1, 255), random.randint(1, 255),
                datetime.datetime.now(),
                random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
                random.randint(1, 1024)
            ))
    return logs


def print_message(size, status_dict):
    """printing the message well formatted"""
    print(f"File size: {size}")
    for key, value in statuses_dict.items():
        print(f"{key}: {value}")


if __name__ == '__main__':

    generated_logs = generator()
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
    # for log in generated_logs:
    #     try:
    #         splited = log.split(" ")
    #         size += int(splited[-1])
    #         status = splited[-2]
    #         statuses_dict[status] = statuses_dict.get(status) + 1
    #         if count % 10 == 0:
    #             print(f"File size: {size}")
    #             for key, value in statuses_dict.items():
    #                 print(f"{key}: {value}")
    #             size = 0
    #             statuses_dict = {
    #                 "200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
    # "404": 0,
    #                 "405": 0, "500": 0
    #             }
    #         count += 1
    #     finally:
    #         ...
