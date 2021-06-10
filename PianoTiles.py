#url : https://www.crazygames.com/game/dont-tap-the-white-tile-piano-tiles

#way to use: 1) Select Classic -> Pro
#            2) Make sure your vs code is not covering any part of the game.
#            3) Execute code whilst keeping mouse on top of the "click to start" area.

from pyautogui import *
import pyautogui
import time
import keyboard
import win32api , win32con

# Use pyautogui.displayMousePosition() to get required X, Y and rgb values
# X:  708 Y:  747 RGB: ( 80,  83, 116)

# X:  796 Y:  747 RGB: (  0,   0,   0)

# X:  880 Y:  747 RGB: ( 77,  81, 116)

# X:  968 Y:  747 RGB: ( 80,  83, 116)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while 1:
    time.sleep(0.01)
    if pyautogui.pixel(700,460)[1]==187 or keyboard.is_pressed('q'):
        #press 'q' to quit the program, or auto-end program at end of run
        exit()
    if pyautogui.pixel(690,540)[0] == 2:
        click(x=690,y=540)
    if pyautogui.pixel(790,540)[0] == 2:
        click(x=790,y=540)
    if pyautogui.pixel(890,540)[0] == 2:
        click(x=890,y=540)
    if pyautogui.pixel(990,540)[0] == 2:
        click(x=990,y=540)
