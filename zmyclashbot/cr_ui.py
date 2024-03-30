from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

battle_button_region = [1040,815,300,180]
ok_button_region = [1173,1173,210,110]
elixir10_region = [1518,1318,150,100]
deck_x = [1131,1272,1429,1572]

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



def battle():
    try:
        battle_button_location = pyautogui.locateOnScreen('golemdeck/battlebutton2.png', confidence = .7, region=battle_button_region)
        click(battle_button_location.left+5, battle_button_location.top+5)
        return 1
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: battle button not found')
        return 0


def endgame():
    try:
        ok_button_location = pyautogui.locateOnScreen('golemdeck/ok.png', confidence = .7, region=ok_button_region)
        click(ok_button_location.left+1, ok_button_location.top+1)
        return 1
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: bomber not found')
        return 0

def elixir10():
    try:
        elixir10_location = pyautogui.locateOnScreen('golemdeck/elixir10.png', confidence = .7, region=elixir10_region)
        click(elixir10_location.left+1, elixir10_location.top+1)
        click(random.choice(deck_x),1243)
        click(1251,1051)
        #click(random.randint(956, 1606),random.randint(955, 1061)) #change this
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: not at 10 elixir')
        pass