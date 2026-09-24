# Python Network Port Scanner

A beginner-friendly Python project that checks selected TCP ports on the local computer.

## Features

- Scans localhost only (`127.0.0.1`)
- Lets the user choose TCP ports to check
- Validates port input
- Identifies standard service names
- Uses multithreading for faster scans
- Includes a one-second connection timeout
- Shows scan duration
- Saves results to `scan_results.txt`
- Uses only Python built-in modules

## Requirements

- Python 3
- No extra packages required

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```powershell
python scanner.py
```

## Example output

```text
Port 80 (http) is closed
Port 443 (https) is closed
Port 135 (epmap) is open
```

The program also saves a report named `scan_results.txt` in the same folder.

## Safety note

This project is intentionally configured to scan `127.0.0.1`, which means the computer running the program. Only scan systems you own or have explicit permission to test.

## Built with

- Python
- socket
- pathlib
- datetime

## Planned improvements
- Improve service detection
- Save reports in more formats
