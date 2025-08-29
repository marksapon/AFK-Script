from pynput.keyboard import Key, Controller
from pynput import keyboard

import time
import random

keyboardInput = Controller()

stopScript = False

randomInput = ['a', 'b', 'c', 'm', 's', 'i'] # Key Inputs
stopKey = 'q'

print("AFK-Script Started ✅")

def KeyPressLoop():
    global stopScript

    while not stopScript:
        # Randomize Key Inputs
        index = random.randint(0, len(randomInput) - 1)
        randomKey = randomInput[index]

        keyboardInput.press(randomKey)
        keyboardInput.release(randomKey)

        print("Random Key Pressed: ", randomKey, )
        time.sleep(5)

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

# Main Loop
KeyPressLoop()