#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Trigger for Time-Logging Script for Windows
v. 0.1.0
"""
from importlib.machinery import SourceFileLoader
from importlib.util import spec_from_loader, module_from_spec
from os.path import exists, expanduser


EVENT: str = "generic event"
ALLOW_MSG: bool = True
NOTIF: bool = True
NOTIF_DURATION: float = 5
SOUND: bool = True
PATH_TO_SOUND: str = None


PATH_TO_LOGGER: str = f"{expanduser('~')}\\Documents\\time-logger\\scripts\\v1\\logger.py"

loader = SourceFileLoader("module", PATH_TO_LOGGER)
spec = spec_from_loader("module", loader)
module = module_from_spec(spec)
import logger


def __notify(time: str) -> None:
    from win10toast import ToastNotifier
    n = ToastNotifier()
    n.show_toast(EVENT, f"{EVENT} logged {time}", duration=NOTIF_DURATION)


def __play_sound() -> None:
    if PATH_TO_SOUND is None or not exists(PATH_TO_SOUND):
        print('\a')
        return
    from subprocess import Popen
    Popen(f'powershell -c (New-Object Media.SoundPlayer "{PATH_TO_SOUND}").PlaySync();')


if __name__ == "__main__":
    msg = input('> ') if ALLOW_MSG else None
    time = logger.log(EVENT, msg)
    if SOUND: __play_sound()
    if NOTIF: __notify(time)
