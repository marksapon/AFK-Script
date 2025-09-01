from pynput.keyboard import Key, Controller
from pynput import keyboard
import time
import random
import threading

keyboardInput = Controller()
stopScript = False

randomInput = ['a', 'b', 'c', 'm', 's', 'i']  # Key Inputs
stopKey = 'q'

print("Script Started ✅")

def KeyPressLoop():
    global stopScript
    while not stopScript:
        # Randomize Key Inputs
        randomKey = random.choice(randomInput)

        keyboardInput.press(randomKey)
        keyboardInput.release(randomKey)

        print("Random Key Pressed:", randomKey)
        time.sleep(5)

def alt_tab_timer():
    
    global stopScript
    while not stopScript:
        time.sleep(10)
        if stopScript:
            break
        print("Alt+Tab triggered")
        keyboardInput.press(Key.alt)
        keyboardInput.press(Key.tab)
        keyboardInput.release(Key.tab)
        keyboardInput.release(Key.alt)

def onPress(key):
    global stopScript
    try:
        if key.char == stopKey:
            print("Q key was pressed, stopping script... 🚫")
            stopScript = True
            return False
    except AttributeError:
        pass

# Start listener in the background
listener = keyboard.Listener(on_press=onPress)
listener.start()

# Start Alt+Tab timer thread
threading.Thread(target=alt_tab_timer, daemon=True).start()

# Main Loop
KeyPressLoop()