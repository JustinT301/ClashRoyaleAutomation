from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from zgolem import golem

deck_area = [1069,1163,569,165]

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def main():
    while True:
        golem_location = 0
        i=0
        golem_location, i = golem(deck_area, i)
        if golem_location != None and i == 1:
            print("True")
        time.sleep(1)


if __name__ == '__main__':
    main()