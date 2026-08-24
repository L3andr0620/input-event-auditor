# Asynchronous Input Event Auditor

## ⚠️ Disclaimer
This tool is created strictly for learning, security research, and authorized system testing. Do not use this on any device without explicit permission.

## What This Tool Does
This Python script monitors and records keyboard inputs in the background without slowing down the system. It helps demonstrate how security tools (like Endpoint Detection and Response systems) monitor background activities to detect potential risks and protect devices.

## Key Features
* **Background Monitoring:** Uses `pynput` to listen for keyboard events continuously without blocking other programs.
* **Smart Key Detection:** Correctly identifies normal letters and numbers as well as special keys (like Shift, Enter, or Ctrl).
* **Automatic Logging:** Saves input activity into a file in real time using smooth file-handling methods.
