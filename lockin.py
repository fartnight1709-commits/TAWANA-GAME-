import os
import sys
import time
import msvcrt
import tkinter as tk
from tkinter import messagebox

def main():
    # Force the script to look for the 'dist' folder relative to WHERE THE SCRIPT IS SAVED
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    full_path = os.path.join(base_dir, "dist", "image.gif")
    
    print(f"Looking for file at: {full_path}")
    
    if not os.path.exists(full_path):
        print(f"ERROR: File not found at {full_path}")
        input("Press Enter to close...")
        return

    # Warning
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("System Alert", "Warning: Spamming initiated. Press ESC to stop.")
    root.destroy()

    print("Spamming started. Press ESC to stop.")

    try:
        while True:
            # Check for ESC key (ASCII 27 is the ESC key)
            if msvcrt.kbhit():
                if ord(msvcrt.getch()) == 27:
                    print("\nStop command received.")
                    break
            
            os.startfile(full_path)
            time.sleep(0.5)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Script exited.")

if __name__ == "__main__":
    main()