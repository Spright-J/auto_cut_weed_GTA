from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import time

cycleTime = 10 # CAN BE CHANGED TO FIT THE TIMMINGS
Weed_Cut_Time = 1 #CHANGE ME BASED ON TYPE OF WEED CUTTING

# Create mouse and keyboard controller objects
mouse = MouseController()
keyboard = KeyboardController()


def CutWeed(e_time):
    keyboard.press(Key.alt_l)
    print('Left Alt key pressed')

    mouse.press(Button.right)
    time.sleep(1)
    mouse.release(Button.right)
    print('Right click')

    mouse.move(75, 0)
    print('Mouse moved by 50 pixels')

    mouse.press(Button.left)
    time.sleep(1)
    mouse.release(Button.left)    
    print('Left click')

    time.sleep(e_time)
    keyboard.tap('e')
    print('First Cut!')

    time.sleep(e_time)
    print('Second Cut!')

    keyboard.release(Key.alt_l)
    print('Left Alt key released')


def main():
    time.sleep(5)
    print('GO!')

    try:
        while True:
            CutWeed(Weed_Cut_Time)
            time.sleep(cycleTime)
    except KeyboardInterrupt:
        print("Script stopped by user")

if __name__ == "__main__":
    main()