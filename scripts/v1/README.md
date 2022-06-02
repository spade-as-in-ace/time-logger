# Time Logger
Simple script for logging events on Windows machines.

## Usage
This was written to run in the restrictive Windows environment common to company-issued boxes.\
Configure via OS settings to launch the scripts on startup/log-in and on desired key-combinations (see [Setup][Setup]).

Saves all logs by default as CSV files named for the date in a `logs` folder in the user's `Documents` folder.\
CSV format:
```
event,time,message
```

## Default Values
Values for logging, found in `logger.py` that can all be modified:
```python
DATE_FORMAT = "%d-%m-%Y" # format to save log files
TIME_FORMAT = "%H:%M:%S" # format for timestamps
DELIMITER = ','          # CSV delimiter

LOG_PATH = f"{expanduser('~')}\\Documents\\logs" # file save location
```

Each trigger also has some options that can be modified:
```python
EVENT: str = "generic event"    # name of event to appear in log
ALLOW_MSG: bool = True          # allow the user to enter a message with the event
NOTIF: bool = True              # show a Win10Toast Notification
NOTIF_DURATION: float = 5       # Duration for notification in seconds
SOUND: bool = True              # Give an audible que
PATH_TO_SOUND: str = None       # Path to sound-file to be played (default will be bell)
```
Of note here, use of the `NOTIF` feature requires having installed [https://pypi.org/project/win10toast/](win10toast).\
Default Windows sounds can be found under`C:\\Windows\\Media`. Should a sound file not be provided (or not exist) the default Windows bell-sound (`C:\\Windows\\Media\\Windows Foreground.wav`) will be played.\
Ensure that the `PATH_TO_LOGGER` variable in each trigger-script refers to `logger.py`.\

The `startup.py` and `shutdown.py` scripts provided do not allow for a user to save a message. `shutdown.py` is set to force the machine to shutdown after 30 seconds (ensure all work is saved).

## Usage
Usage is up to user configuration and setup.\
An example setup might be as follows:
- Windows Task Scheduler to launch `startup.py` on system startup
- `ctrl+alt+m` as key-bind to trigger `message.py` to log a message
- `ctrl+alt+b` as key-bind to trigger `break.py` to log a break (and lock/sleep the machine)
- Windows Task Scheduler to launch `return.py` on waking/signing back into a machine (complex)
- `ctrl+alt+s` as a key-bind to launch `shutdown.py`

## Setup
How to set up the scripts to conveniently run in Windows.\
Before running, make sure to check that all of the configuration variables are appropriate.

### To Start
The script can be run with
```batch
C:\Path\to\python.exe C:\path\to\startup.py
```
(Files may not be on C drive)

To use Windows Task Scheduler to autostart upon login, open Task Scheduler, click `Create New Task`, and name it something appropriate.\
Set the trigger to be `At log on`.\
Make the action `Start a program`. Put the path to `python.exe` in the `Program/script` spot.\
In the `Add arguments` spot add the path to `startup.py`.\
Change `Conditions` so that it executes regardless of whether machine is plugged in or running off battery.

The time-logger console should open on launch.

### Key-binds
This version of the script uses a "trigger" script to log an event. The ideal method to launch a trigger-script would be to bind it to some key-combination (e.g. `ctrl+alt+e` to launch a script for logging a specific kind of event). There is a way to do this, however it is a tad bit convoluted.\
1. Set up desired trigger-scripts (`trigger.py` is provided as a generic example)
2. Create a shortcut for each script (i.e. right-click the script and select "Create shortcut")
3. Apply a key-bind to the shortcut (right-click on the shortcut, click in the field where it says "Shortcut key", enter desired key-combination, and select "Apply"

A this point, pressing the designated key-combination will launch the trigger, which will then log the event.\
An alternative to this might be to pin the scripts to the taskbar or otherwise have them in some easy-to-click location.\
As was alluded to earlier, Windows Task Scheduler can also launch a task based on just about any kind of event, but configuring this takes a good amount of figuring-out.
