from pynput.mouse import Controller
from pynput.keyboard import Controller

# (left to right, top to bottom)
# from top-left of the screen you can imagine the top-left to be (0,0)
def controlMouse():
    mouse = Controller()
    mouse.position = (10,20)

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("\nim handsome")

controlKeyboard()

# controlling your mouse
# listening to your mouse
# controlling your keyboard
# listening to your mkeyboard


