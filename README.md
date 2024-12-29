# Keylogger Linux

**Keylogger Linux** is a simple tool that records all keyboard input on Linux systems and saves it to a text file with timestamps.

## ⚠️ Disclaimer

This project is for **educational purposes only**. Unauthorized use may break laws. Use responsibly and only in controlled environments.

## Features
- Logs all keystrokes with timestamps.
- Automatically installs dependencies (`pynput` and `xdotool`).
- Minimizes the terminal during execution.

## Requirements
- Linux-based system
- Python 3.x
- pip (`python3-pip`)
- `xdotool` (installed automatically)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Ghostalex7/keylogger-linux.git
   cd keylogger-linux
2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
## Usage

Run the keylogger with:

The terminal will minimize, and the keystrokes will be logged in keylogger_output.txt. The script stops automatically after a set time or can be terminated manually.
   ```bash
   python3 keylogger.py

