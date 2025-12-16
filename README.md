# ⌨️ Basic Keylogger Program

## ⚠️ Important Note

This program is created for **educational purposes only**, specifically to understand how input monitoring works at a basic level. Unauthorized use of a keylogger is illegal and unethical. Ensure you have explicit permission to run this program on any computer and strictly adhere to all relevant laws and policies.

## 🌟 Overview

This program fulfills **Task 04** by creating a basic keylogger application. It operates by listening for key press events on the keyboard, logging the corresponding keystrokes, and saving the captured data to a designated log file.

## 🔑 Features

* **Keystroke Capture:** Hooks into the operating system's input stream to capture individual key presses.
* **Logging:** Converts the captured key events (including special keys like Shift, Enter, Space) into readable text.
* **File Output:** Periodically or continuously saves the recorded keystrokes to a local text file for later retrieval.

## 🛠️ Requirements

* **Python 3**
* **Pynput Library:** This cross-platform library is used to control and monitor input devices.
    ```bash
    pip install pynput
    ```
* **Operating System Dependencies:** Depending on your OS (Windows, macOS, or Linux), you may need specific developer headers or permissions for keyboard hooks to function correctly.

## 🚀 How to Run

1.  **Save the Code:** Save the program code (e.g., `basic_keylogger.py`).
2.  **Ensure Permissions:** On some systems (especially Linux/macOS), you may need elevated permissions (`sudo`) or specific privacy settings enabled for the program to monitor input.
3.  **Execute:** Run the program from your terminal:

    ```bash
    python basic_keylogger.py
    ```

4.  **Stop:** The keylogger will run silently in the background until the program is manually stopped (usually by pressing **Ctrl+C** in the terminal where it was launched or by a specific hotkey defined in the code).

## 📄 Log File Output

The keystrokes will be saved to a file named `keylog.txt` (or a similar filename defined in the program).

### Example `keylog.txt` content:
