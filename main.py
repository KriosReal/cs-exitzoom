import time
from pynput.mouse import Listener, Button
from pynput.keyboard import Controller

kb = Controller()
zoom_state = 0

def clicked(x, y, button, pressed):
    global zoom_state
    if pressed: 
        if button == Button.left:
            zoom_state = 0
        elif button == Button.right:
            if zoom_state == 0:
                zoom_state = 1
            elif zoom_state == 1:
                kb.press ('3')
                kb.release('3')
                time.sleep(0.05)
                kb.press ('1')
                kb.release ('1')
                zoom_state = 0

with Listener (on_click=clicked) as listener:
    listener.join()


