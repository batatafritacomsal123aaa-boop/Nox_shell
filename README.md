# NOX

NOX is a lightweight command-line environment written in Python.

Current version: **0.05**

## What it can do

NOX includes commands for:

- System information
- Current time and date
- Uptime
- Username display
- Directory navigation
- Listing files and folders
- Creating folders
- Creating, reading, writing and deleting files
- Text manipulation
- Changing terminal color
- Changing the terminal title
- Command history
- Running external programs
- Stopwatch
- Custom NOX username

## Main commands

### System
- `version`
- `sysinfo`
- `whoami`
- `time`
- `date`
- `uptime`

### Navigation
- `cwd`
- `cd <path>`
- `ls`

### Files
- `touch <file>`
- `cat <file>`
- `write <file>`
- `append <file>`
- `rm <file>`
- `mkdir <directory>`

### Text
- `echo <text>`
- `upper <text>`
- `lower <text>`
- `length <text>`
- `reverse <text>`

### NOX
- `nexus [name]`
- `color [color]`
- `title <title>`
- `history`
- `run <program>`
- `clear`
- `sleep <seconds>`
- `exit`

### Other
- `ping`
- `stopwatch`

## Persistence

NOX stores the custom username and terminal title so they can be restored when the program is opened again.

## Files

- `Nox_shell0.05.py` — main source code
- `nox.ico` — application icon

## Running from source

Requires Python 3.

```bash
python Nox_shell0.05.py