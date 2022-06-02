# Time Logger
Simple script for logging events on Windows machines.

## Usage
This was written to run in the restrictive Windows environment common to company-issued boxes.\
Configure via OS settings to launch the script on startup/log-in.\
Key-chars:
- b: break (meant for short breaks)
- l: lunch (lunch breaks)
- r: return (returning from break)
- m: message (log message or note)
- q: quit (terminate the logger without shutting down)
- s: shutdown (gives 30 seconds before forcing shutdown)

Any string(s) following the key-char will be logged as a message or note.\
Saves all logs by default as CSV files named for the date in a `logs` folder in the user's `Documents` folder.\
CSV format:
```
event,time,message
```

## Default Values
```python
DATE_FORMAT = "%d-%m-%Y" # format to save log files
TIME_FORMAT = "%H:%M:%S" # format for timestamps
DELIMITER = ','          # CSV delimiter

LOG_PATH = f"{expanduser('~')}\\Documents\\logs" # file save location
```
These values can be modified.

## To Start
Before running, make sure to check that all of the configuration variables are appropriate.

The script can be run with
```batch
C:\Path\to\python.exe C:\path\to\time_logger.py
```
(Files may not be on C drive)

To use Windows Task Scheduler to autostart upon login, open Task Scheduler, click `Create New Task`, and name it something appropriate.\
Set the trigger to be `At log on`.\
Make the action `Start a program`. Put the path to `python.exe` in the `Program/script` spot.\
In the `Add arguments` spot add the path to `time-logger.py`.\
Change `Conditions` so that it executes regardless of whether machine is plugged in or running off battery.

The time-logger console should open on launch.
