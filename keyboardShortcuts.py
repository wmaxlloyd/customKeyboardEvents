from pynput import keyboard
from keyboardActions import executeKeyboardCommand
import keyStrokeLogger

def on_press(key):
    global pressedKeys
    try:
        pressedKeys
    except:
        pressedKeys = {}

    pressedKeys[processKey(key)] = True
    actionReturn = executeKeyboardCommand(pressedKeys)
    if actionReturn == 'kill':
        return False

def on_release(key):
    global pressedKeys
    pKey = processKey(key)
    try:
        pressedKeys.pop(pKey)
    except:
        pressedKeys = {}

def processKey(key):
    try:
        return key.char.lower()
    except:
        return str(key)


with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    print("Ready!")
    listener.join()