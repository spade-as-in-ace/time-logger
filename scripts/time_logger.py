#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic Time-Logging Script for Windows
v. 0.0.7
"""
from datetime import datetime as dt
from os import mkdir, system
from os.path import exists, expanduser

DATE_FORMAT = "%d-%m-%Y"
TIME_FORMAT = "%H:%M:%S"
DELIMITER = ','

LOG_PATH = f"{expanduser('~')}\\Documents\\logs"
KEYS = {'b': "break", 'l': "lunch", 'r': "return", 'm': "message", 'q': "quit", 's': "shutdown"}


def main():
    if not exists(LOG_PATH):
        mkdir(LOG_PATH)
    time = dt.now()
    file_path = f"{LOG_PATH}\\{time.strftime(DATE_FORMAT)}.csv"
    log_file = open(file_path, 'a')
    log_file.write(f"startup{DELIMITER}{time.strftime(TIME_FORMAT)}\n")
    log_file.close()

    while True:
        key = input("> ").split(maxsplit=1)
        time = dt.now()
        log_file = open(file_path, 'a')

        if time.strftime("%d-%m-%Y") != log_file.name[-14:-4]:
            log_file.close()
            file_path = f"{LOG_PATH}\\{time.strftime(DATE_FORMAT)}.csv"
            log_file = open(file_path, 'a')

        time = time.strftime(TIME_FORMAT)

        if key[0] in KEYS:
            if key[0] == 's':
                if input("confirm shutdown > ") == 's':
                    system("shutdown /s /t 30")
                else:
                    print("shutdown aborted")
                    continue

            log_file.write(f"{KEYS[key[0]]}{DELIMITER}{time}")
            if len(key) == 2:
                log_file.write(f"{DELIMITER}{key[1]}")
            log_file.write("\n")

            if key[0] == 'q':
                return
            print(f"{KEYS[key[0]]} logged {time}")

        else:
            print(f"Key '{key[0]}' unrecognized")
        log_file.close()

if __name__ == "__main__":
    main()
