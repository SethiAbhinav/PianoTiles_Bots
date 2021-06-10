#url : https://www.crazygames.com/game/magic-piano-tiles

#way to use: Make sure your vs code is not covering any part of the game, now, execute code and then click "START"

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

while keyboard.is_pressed('q') == False:
    #press 'q' to quit the program
    if pyautogui.pixel(708,400)[0] == 0:
        click(x=708,y=400)
    if pyautogui.pixel(796,400)[0] == 0:
        click(x=796,y=400)
    if pyautogui.pixel(880,400)[0] == 0:
        click(x=880,y=400)
    if pyautogui.pixel(968,400)[0] == 0:
        click(x=968,y=400)