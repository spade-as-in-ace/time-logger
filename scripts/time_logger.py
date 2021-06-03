#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic Time-Logging Script
v. 0.0.3
"""
from datetime import datetime as dt
from os import system
from os.path import expanduser

LOG_PATH = f"{expanduser('~')}\\Documents\\Logs"
KEYS = {"b": "break", "l": "lunch", "r": "return", "m": "message", "s": "shutdown"}


def main():
    global LOG_PATH
    time = dt.now()
    file_path = f"{LOG_PATH}\\{time.strftime('%d-%m-%Y')}.csv"
    log_file = open(file_path, "a")
    log_file.write(f"startup, {time.strftime('%H:%M:%S')}, \n")
    log_file.close()

    while True:
        key = input("> ").split(maxsplit=1)
        time = dt.now()
        log_file = open(file_path, "a")

        if time.strftime("%d-%m-%Y") != log_file.name[-14:-4]:
            log_file.close()
            file_path = f"{LOG_PATH}\\{time.strftime('%d-%m-%Y')}.csv"
            log_file = open(file_path, "a")

        time = time.strftime("%H:%M:%S")

        if key[0] in KEYS.keys():
            if key[0] == "s":
                if input("confirm shutdown > ") == "s":
                    system("shutdown /s /t 30")
                else:
                    print("shutdown aborted")
                    continue

            log_file.write(f"{KEYS[key[0]]}, {time},")

            if len(key) == 2:
                log_file.write(f" {key[1]}")

            log_file.write("\n")
            print(f"{KEYS[key[0]]} logged {time}")

        else:
            print(f"Key '{key[0]}' unrocognized")
        log_file.close()


main()
