# Asynchronous Input Event Auditor

## ⚠️ Educational & Ethical Disclaimer
This repository is hosted strictly for educational purposes, defensive security research, and authorized administrative auditing. Unauthorized deployment against endpoints without explicit management consent is strictly prohibited.

## 🎯 Project Objective
A lightweight Python utility designed to audit local input event handling using asynchronous listeners. This project demonstrates how operating system API hooks intercept user input, providing practical context for how Endpoint Detection and Response (EDR) telemetry monitors system-wide activity.

## 🛠️ Technical Skills Highlighted
* **Asynchronous Event Handling:** Implemented non-blocking background loops via `pynput.keyboard.Listener`.
* **Exception & Edge-Case Handling:** Managed distinct data structures for standard alphanumeric input vs. special system control characters.
* **Persistent I/O Operations:** Managed continuous data streams using standard file append (`a`) operations in Python.
