from pyautogui import *
import pyautogui
import time
import random
import win32api, win32con

class UI:
    def __init__(self):
        self.battle_button_region = [1040,815,300,180]
        self.ok_button_region = [1173,1173,210,110]
        self.elixir10_region = [1518,1318,150,100]
        self.deck_x = [1131,1272,1429,1572]

    def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    def battle(self): #looks for battle button
        try:
            battle_button_location = pyautogui.locateOnScreen('golemdeck/battlebutton2.png', confidence = .7, region=self.battle_button_region)
            click(battle_button_location.left+5, battle_button_location.top+5)
            return 1
        except pyautogui.ImageNotFoundException:
            return 0

    def endgame(self): #looks for OK button when match ends
        try:
            ok_button_location = pyautogui.locateOnScreen('golemdeck/ok.png', confidence = .7, region=self.ok_button_region)
            click(ok_button_location.left+1, ok_button_location.top+1)
            return 1
        except pyautogui.ImageNotFoundException:
            return 0

    def elixir10(self): #prevents leaking elixir
        try:
            elixir10_location = pyautogui.locateOnScreen('golemdeck/elixir10.png', confidence = .7, region=self.elixir10_region)
            click(elixir10_location.left+1, elixir10_location.top+1)
            click(random.choice(self.deck_x),1243)
            click(1251,1051)
        except pyautogui.ImageNotFoundException:
            pass