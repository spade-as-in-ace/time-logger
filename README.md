# Time Logger
Simple script for logging events on Windows machines.

## Versions
This project has two versions, `v0` and `v1`.\
`v0` launches a console that remains open/running until closed and requires simple commands to be entered for logging.\
`v1` is based entirely on trigger-scripts that must be launched (e.g. by way of keyboard-shortcut) to log an event.

## Usage
Read the relevant `README.md`s for each version.\
Both versions necessitate using Windows Task Scheduler to varying degrees.

## Dependencies
These scripts were written to run in restrictive Windows environments common to company-issued machines.\
`v0` requires no dependencies outside of those built-in to `Python` (`time` and `os`).\
`v1` requires the same dependencies as `v0`, `importlib.machinery` and `importlib.util` (both of which are built-in to `Python`). It also has two optional features that depend on `subprocess` (built-in to `Python`) and `win10toast` (which must be installed).
