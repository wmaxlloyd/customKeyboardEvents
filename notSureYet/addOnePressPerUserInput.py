from pynput import keyboard
import time
controller = keyboard.Controller()
button = keyboard.Key
keyCode = keyboard.KeyCode

def on_press(key):
    global all_keys_pressed
    global virtual_keys_pressed
    try:
        all_keys_pressed += 1
    except:
        all_keys_pressed = 1
        virtual_keys_pressed = 0
    if all_keys_pressed == virtual_keys_pressed * 2:
        all_keys_pressed = 0
        virtual_keys_pressed = 0
    print('Key {} pressed.'.format(key))
    print (all_keys_pressed)
    print (virtual_keys_pressed)
    if all_keys_pressed > virtual_keys_pressed * 2:
        str_to_type = " lol "
        virtual_keys_pressed += len(str_to_type)
        controller.type(str_to_type)

    global loop_break
    try:
        loop_break
    except:
        loop_break = 1
    if loop_break > 100:
        return False
    else:
        loop_break += 1

def on_release(key):
    print('Key {} released.'.format(key))
    if str(key) == 'Key.cmd':
        print('Exiting...')
        return False

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()