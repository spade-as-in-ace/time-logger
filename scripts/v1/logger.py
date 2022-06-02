#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic Time-Logging Script for Windows
v. 0.1.0
"""
from datetime import datetime as dt
from os import mkdir, system
from os.path import exists, expanduser


DATE_FORMAT = "%d-%m-%Y"
TIME_FORMAT = "%H:%M:%S"
DELIMITER = ','
# expanduser('~') gets the path to the user's home directory akin to `realpath ~`
LOG_PATH = f"{expanduser('~')}\\Documents\\logs"


def log(event: str, msg: str = None) -> str:
    if not exists(LOG_PATH):
        mkdir(LOG_PATH)
    time = dt.now()
    file_path = f"{LOG_PATH}\\{time.strftime(DATE_FORMAT)}.csv"
    log_file = open(file_path, 'a')

    time = time.strftime(TIME_FORMAT)
    log_file.write(f"{event}{DELIMITER}{time}")
    if msg.strip() not in [None, '']:
        log_file.write(f"{DELIMITER}{msg}")
    log_file.write('\n')
    log_file.close()

    return time
