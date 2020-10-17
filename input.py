from pynput import keyboard

def _start():
     print("HelloWorld")
def on_press(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    else:
        _start()

# Collect events until released
with keyboard.Listener(
        on_press=on_press, suppress=True) as listener:
    listener.join()