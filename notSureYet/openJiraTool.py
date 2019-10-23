from pynput import keyboard
import time
import os

controller = keyboard.Controller()
button = keyboard.Key
keyCode = keyboard.KeyCode

def openJiraTool():
    os.system('sublime ~/Desktop/Implementations/Ops/Jira-Tool/jira-tool/')

def on_press(key):
    global pressedKeys
    try:
        pressedKeys
    except:
        pressedKeys = {}

    pressedKeys[str(key)] = True
    if checkList(["'a'","'b'"]):
        openJiraTool()
    print(pressedKeys)

def on_release(key):
    global pressedKeys
    pressedKeys[str(key)] = False
    if str(key) == 'Key.cmd':
        print('Exiting...')
        return False

def checkList(arrOfKeys):
    global pressedKeys
    for key in arrOfKeys:
        if key not in pressedKeys or not pressedKeys[key]:
            return False
    return True


with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()