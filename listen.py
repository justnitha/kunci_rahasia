from pynput.mouse import Listener

def writetofile(x, y):
    print(f"Position of current mouse '[{x},{y}]'")

with Listener(on_move=writetofile) as l:
    l.join()