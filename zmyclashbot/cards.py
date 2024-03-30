from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

deck_area = [1069,1163,569,165]
dragon_list = ['golemdeck/mybabydragon.png','golemdeck/myelectrodragon.png']

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def bomber():
    try:
        bomber_location = pyautogui.locateOnScreen('golemdeck/mybomber.png', confidence = .9, region=deck_area)
        click(bomber_location.left+1, bomber_location.top+1)
        click(1151,882)
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: bomber not found')
        pass

def skeletons():
    try:
        skeletons_location = pyautogui.locateOnScreen('golemdeck/myskeletons.png', confidence = .9, region=deck_area)
        click(skeletons_location.left+1, skeletons_location.top+1)
        click(random.randint(956, 1606),random.randint(655, 1061))
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: skeletons not found')
        pass

def bats():
    try:
        bats_location = pyautogui.locateCenterOnScreen('golemdeck/mybats.png', confidence = .9, region=deck_area)
        cards_found = defense()
        if cards_found != None:
            click(bats_location[0], bats_location[1])
            click(cards_found[0],cards_found[1]+100)
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: bats not found')
        pass

def golem_nightwitch(golem_location, nightwitch_location, elixir_single_time):
    golemx = 1261
    nightwitchx = 1151
    try:
        golem_location = pyautogui.locateOnScreen('golemdeck/mygolem.png', confidence = .975, region=deck_area)
        nightwitch_location = pyautogui.locateOnScreen('golemdeck/mynightwitch.png', confidence = .9, region=deck_area)
        #left_tower_screenshot2 = pyautogui.screenshot(region=[1020, 222, 32, 30])
        if golem_location != None and nightwitch_location != None:
            try:
                pyautogui.locateOnScreen('golemdeck/leftower1234.png', confidence = .3, region=[1020, 222, 100, 100])
            #is_left_tower = is_left_tower_up()
            except:
            #if left_tower_screenshot == left_tower_screenshot2:
                print("Left tower isnt there")
                golemx = 1296
                nightwitchx = 1407
            click(golem_location.left+1, golem_location.top+1)
            click(golemx,1059)
            time.sleep(elixir_single_time*4)
            click(nightwitch_location.left+1, nightwitch_location.top+1)
            click(nightwitchx,932)
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: golem not found')
        pass

def is_left_tower_up(): #not in use
    try:
        left_tower_location = pyautogui.locateCenterOnScreen('golemdeck/level11tower.png', confidence = .7, region=[1020, 222, 32, 30])
        if left_tower_location:
            return 1
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: skeletons not found')
        return None

def clone():
    try:
        clone_location = pyautogui.locateOnScreen('golemdeck/myclone.png', confidence = .8, region=deck_area)
        #print("Clone found")
        try:
            push_location = pyautogui.locateOnScreen('golemdeck/golemnwpush.png', confidence = .7)
            if clone_location and push_location:
                click(clone_location.left+3, clone_location.top+3)
                click(push_location.left+30, push_location.top+30)
                print(push_location)
                print('image found')
                #may need to add image of cards being damaged and showing their level, or lower confidence + add region
        except pyautogui.ImageNotFoundException:
            #print("golem nw not found")
            pass
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: clone not found')
        pass


def dragon_choice():
    dragon_choice = random.choice(dragon_list)
    try:
        dragon_choice_location = pyautogui.locateOnScreen(dragon_choice, confidence = .9, region=deck_area)
        try:
            push_location = pyautogui.locateOnScreen('golemdeck/golemnwpush.png', confidence = .7)
            if dragon_choice_location and push_location:
                click(dragon_choice_location.left+3, dragon_choice_location.top+3)
                click(push_location.left+30, push_location.top+200)
        except pyautogui.ImageNotFoundException:
            #print("golem nw not found")
            pass
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: baby dragon not found')
        pass


def baby_dragon():
    try:
        baby_dragon_location = pyautogui.locateCenterOnScreen('golemdeck/mybabydragon.png', confidence = .9, region=deck_area)
        cards_found = defense()
        if cards_found != None:
            click(baby_dragon_location[0], baby_dragon_location[1])
            click(cards_found[0],cards_found[1]+50) #change this
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: skeletons not found')
        pass

def arrows():
    try:
        arrows_location = pyautogui.locateOnScreen('golemdeck/myarrows.png', confidence = .7, region=deck_area)
        print("image found")
        try:
            pyautogui.locateOnScreen('golemdeck/region1.png', confidence = .9, region=[949, 407, 300, 200])
        except pyautogui.ImageNotFoundException:
            click(arrows_location.left+1, arrows_location.top+1)
            click(1065,461) #change this
        #try:
        #    pyautogui.locateOnScreen('golemdeck/region2.png', confidence = .6, region=[1176, 407, 350, 200])   #figure out why region 2 cant be found
        #except pyautogui.ImageNotFoundException:
        #    click(arrows_location.left+1, arrows_location.top+1)
        #    click(1274,461) #change this
        try:
            pyautogui.locateOnScreen('golemdeck/region3.png', confidence = .9, region=[1390, 407, 300, 200])
        except pyautogui.ImageNotFoundException:
            click(arrows_location.left+1, arrows_location.top+1)
            click(1491,461) #change this
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: arrows not found')
        pass

def evo_skeletons():
    try:
        evo_skeletons_location = pyautogui.locateOnScreen('golemdeck/myevoskeletons.png', confidence = .9, region=deck_area)
        click(evo_skeletons_location.left+1, evo_skeletons_location.top+1)
        click(random.randint(956, 1606),random.randint(655, 1061)) #change this
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: skeletons not found')
        pass

def lumberjack():
    try:
        lumberjack_location = pyautogui.locateCenterOnScreen('golemdeck/mylumberjack.png', confidence = .9, region=deck_area)
        cards_found = defense()
        if cards_found != None:
            click(lumberjack_location[0], lumberjack_location[1])
            click(cards_found[0],cards_found[1])
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: skeletons not found')
        pass


def knight():
    try:
        knight_location = pyautogui.locateCenterOnScreen('golemdeck/myknight.png', confidence = .9, region=deck_area)
        cards_found = defense()
        if cards_found != None:
            click(knight_location[0], knight_location[1])
            click(cards_found[0],cards_found[1])
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: skeletons not found')
        pass

def archers():
    try:
        archers_location = pyautogui.locateCenterOnScreen('golemdeck/myarchers.png', confidence = .9, region=deck_area)
        cards_found = defense()
        if cards_found != None:
            click(archers_location[0], archers_location[1])
            click(cards_found[0],cards_found[1]+100)
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: skeletons not found')
        pass

def barb_barrel():
    try:
        archers_location = pyautogui.locateCenterOnScreen('golemdeck/mybarbbarrel.png', confidence = .9, region=deck_area)
        cards_found = defense() #GET A BARB BARREL IMAGE
        if cards_found != None:
            click(archers_location[0], archers_location[1])
            click(cards_found[0],cards_found[1]+100)
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: skeletons not found')
        pass

def electro_dragon():
    try:
        archers_location = pyautogui.locateCenterOnScreen('golemdeck/myelectrodragon.png', confidence = .9, region=deck_area)
        cards_found = defense()
        if cards_found != None:
            click(archers_location[0], archers_location[1])
            click(cards_found[0],cards_found[1]+100)
    except pyautogui.ImageNotFoundException:
        #print('ImageNotFoundException: skeletons not found')
        pass

#--------------------------------------------------------- DEFENSE -----------------------------------------------------------------------

def defense():
    try:
        card_level = pyautogui.locateCenterOnScreen('golemdeck/level11gold2.png', confidence = .9, region=[940, 475, 664, 525])
        return card_level
    except pyautogui.ImageNotFoundException:
        try:
            card_level = pyautogui.locateCenterOnScreen('golemdeck/level11.png', confidence = .95, region=[940, 475, 664, 525])
            return card_level
        except pyautogui.ImageNotFoundException:
            pass