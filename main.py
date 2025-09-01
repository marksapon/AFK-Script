from pynput.keyboard import Key, Controller
from pynput import keyboard
import time
import random
import threading

keyboardInput = Controller()
stopScript = False

randomInput = ['a', 'b', 'c', 'm', 's', 'i']  # Key Inputs
stopKey = 'q' # Stop Key
display = '''
.______    _______    .______        ___       ______  __  ___     __  .__   __.         ___      
|   _  \  |   ____|   |   _  \      /   \     /      ||  |/  /    |  | |  \ |  |        /   \     
|  |_)  | |  |__      |  |_)  |    /  ^  \   |  ,----'|  '  /     |  | |   \|  |       /  ^  \    
|   _  <  |   __|     |   _  <    /  /_\  \  |  |     |    <      |  | |  . `  |      /  /_\  \   
|  |_)  | |  |____    |  |_)  |  /  _____  \ |  `----.|  .  \     |  | |  |\   |     /  _____  \  
|______/  |_______|   |______/  /__/     \__\ \______||__|\__\    |__| |__| \__|    /__/     \__\ 
                                                                                                  
.___  ___.  __  .__   __.  __    __  .___________. _______                                        
|   \/   | |  | |  \ |  | |  |  |  | |           ||   ____|                                       
|  \  /  | |  | |   \|  | |  |  |  | `---|  |----`|  |__                                          
|  |\/|  | |  | |  . `  | |  |  |  |     |  |     |   __|                                         
|  |  |  | |  | |  |\   | |  `--'  |     |  |     |  |____                                        
|__|  |__| |__| |__| \__|  \______/      |__|     |_______|'''

print("Script Started ✅")

def KeyPressLoop():
    global stopScript
    while not stopScript:
        # Randomize Key Inputs
        randomKey = random.choice(randomInput)

        keyboardInput.press(randomKey)
        keyboardInput.release(randomKey)

        # print("Random Key Pressed:", randomKey)
        time.sleep(5)

def alt_tab_timer():
    
    global stopScript
    while not stopScript:
        time.sleep(10)
        if stopScript:
            break
        # print("Alt+Tab triggered")
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
print(display)

# Main Loop
KeyPressLoop()