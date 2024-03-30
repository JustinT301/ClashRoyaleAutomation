from pyautogui import *
import pyautogui
import time
import win32api, win32con


def golem(deck_area, i):
    try:
        golem_location = pyautogui.locateOnScreen('golemdeck/mygolem.png', confidence = .7, region=deck_area)
        nightwitch_location = pyautogui.locateOnScreen('golemdeck/mynightwitch.png', confidence = .6, region=deck_area)
        if golem_location != None and nightwitch_location != None:
            i = 1 #to set up for later to make sure nw doesnt play if golem wasnt just played
            click(golem_location.left+1, golem_location.top+1)
            click(1261,1059)
            time.sleep(11.2)
            return golem_location, i

    except pyautogui.ImageNotFoundException:
        print('ImageNotFoundException: golem not found')