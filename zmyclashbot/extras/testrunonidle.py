import pyautogui
import time
import keyboard
import random
import win32api, win32con

deck_area = [1069,1163,569,165]

while keyboard.is_pressed('q') == False:
    if pyautogui.locateOnScreen('golemdeck/editbutton.png', confidence = .7) != None:
        print("I can see it")
    else:
        print("I cant see it")
