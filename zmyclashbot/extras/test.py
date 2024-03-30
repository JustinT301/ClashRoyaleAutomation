import pyautogui
import time
import keyboard
import random
import win32api, win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

pyautogui.useImageNotFoundException()

while keyboard.is_pressed('q') == False:
    try:
        card_level = pyautogui.locateCenterOnScreen('golemdeck/level11.png', confidence = .95, region=[940, 500, 664, 500])
        print(card_level[0], card_level[1])
        click(card_level[0], card_level[1])
    except pyautogui.ImageNotFoundException:
        try:
            card_level = pyautogui.locateCenterOnScreen('golemdeck/level11gold.png', confidence = .95, region=[940, 500, 664, 500])
            print(card_level[0], card_level[1])
            click(card_level[0], card_level[1])
        except pyautogui.ImageNotFoundException:
            pass

