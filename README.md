# Time Logger
Simple script for logging work hours

## Usage
This was written to run in the restrictive Windows environment common to company-issued boxes.\
Configure via OS settings to launch the script on startup/log-in.\
Key-chars:
- b: break (meant for short breaks)
- l: lunch (lunch breaks)
- r: return (returning from break)
- m: message (log message or note)
- s: shutdown (gives 30 seconds before forcing shutdown)
Any string(s) following the key-char will be logged as a message or note.\
Saves all logs as CSV files named for the date in a `Logs` folder in the user's `Documents` folder.\
CSV format:
```
event, time, message
```
