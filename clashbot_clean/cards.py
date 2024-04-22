from pyautogui import *
import pyautogui
import time
import random
import win32api, win32con

class Cards:
    def __init__(self):
        self.deck_area = [1069,1163,569,165]
        self.dragon_list = ['golemdeck/mybabydragon.png','golemdeck/myelectrodragon.png']


    def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


    def skeletons(self):
        try:
            skeletons_location = pyautogui.locateOnScreen('golemdeck/myskeletons.png', confidence = .9, region=self.deck_area)
            click(skeletons_location.left+1, skeletons_location.top+1)
            click(random.randint(956, 1606),random.randint(655, 1061))
        except pyautogui.ImageNotFoundException:
            pass

   
    def evo_skeletons(self):
        try:
            evo_skeletons_location = pyautogui.locateOnScreen('golemdeck/myevoskeletons.png', confidence = .9, region=self.deck_area)
            cards_found = self.defense()
            click(evo_skeletons_location.left+1, evo_skeletons_location.top+1)
            if cards_found != None:
                click(cards_found[0], cards_found[1])
            else:
                click(random.randint(956, 1606),random.randint(655, 1061)) #change this
        except pyautogui.ImageNotFoundException:
            pass


    def bats(self):
        try:
            bats_location = pyautogui.locateCenterOnScreen('golemdeck/mybats.png', confidence = .9, region=self.deck_area)
            cards_found = self.defense()
            if cards_found != None:
                click(bats_location[0], bats_location[1])
                click(cards_found[0],cards_found[1]+100)
        except pyautogui.ImageNotFoundException:
            pass


    def golem_nightwitch(self, golem_location, nightwitch_location, elixir_single_time):
        golemx = 1261
        nightwitchx = 1151
        try:
            golem_location = pyautogui.locateOnScreen('golemdeck/mygolem.png', confidence = .975, region=self.deck_area)
            nightwitch_location = pyautogui.locateOnScreen('golemdeck/mynightwitch.png', confidence = .9, region=self.deck_area)
            if golem_location != None and nightwitch_location != None:
                try:
                    pyautogui.locateOnScreen('golemdeck/opponents_left_tower.png', confidence = .3, region=[1020, 222, 100, 100])
                except:
                    print("Left tower isnt there")
                    golemx = 1296
                    nightwitchx = 1407
                click(golem_location.left+1, golem_location.top+1)
                click(golemx,1059)
                time.sleep(elixir_single_time*4)
                click(nightwitch_location.left+1, nightwitch_location.top+1)
                click(nightwitchx,932)
        except pyautogui.ImageNotFoundException:
            pass


    def dragon_choice(self):
        dragon_choice = random.choice(self.dragon_list)
        try:
            dragon_choice_location = pyautogui.locateOnScreen(dragon_choice, confidence = .9, region=self.deck_area)
            try:
                push_location = pyautogui.locateOnScreen('golemdeck/golemnwpush.png', confidence = .7)
                if dragon_choice_location and push_location:
                    click(dragon_choice_location.left+3, dragon_choice_location.top+3)
                    click(push_location.left+30, push_location.top+200)
            except pyautogui.ImageNotFoundException:
                pass
        except pyautogui.ImageNotFoundException:
            pass


    def baby_dragon(self):
        try:
            baby_dragon_location = pyautogui.locateCenterOnScreen('golemdeck/mybabydragon.png', confidence = .9, region=self.deck_area)
            cards_found = self.defense()
            if cards_found != None:
                click(baby_dragon_location[0], baby_dragon_location[1])
                click(cards_found[0],cards_found[1]+50)
        except pyautogui.ImageNotFoundException:
  
            pass


    def lumberjack(self):
        try:
            lumberjack_location = pyautogui.locateCenterOnScreen('golemdeck/mylumberjack.png', confidence = .9, region=self.deck_area)
            cards_found = self.defense()
            if cards_found != None:
                click(lumberjack_location[0], lumberjack_location[1])
                click(cards_found[0],cards_found[1])
        except pyautogui.ImageNotFoundException:
            pass


    def knight(self):
        try:
            knight_location = pyautogui.locateCenterOnScreen('golemdeck/myknight.png', confidence = .9, region=self.deck_area)
            cards_found = self.defense()
            if cards_found != None:
                click(knight_location[0], knight_location[1])
                click(cards_found[0],cards_found[1])
        except pyautogui.ImageNotFoundException:
            pass

    def electro_dragon(self):
        try:
            archers_location = pyautogui.locateCenterOnScreen('golemdeck/myelectrodragon.png', confidence = .9, region=self.deck_area)
            cards_found = self.defense()
            if cards_found != None:
                click(archers_location[0], archers_location[1])
                click(cards_found[0],cards_found[1]+100)
        except pyautogui.ImageNotFoundException:
            pass

    #--------------------------------------------------------- DEFENSE -----------------------------------------------------------------------

    def defense(self):
        try:
            card_level = pyautogui.locateCenterOnScreen('golemdeck/level11gold2.png', confidence = .9, region=[940, 475, 664, 525])
            return card_level
        except pyautogui.ImageNotFoundException:
            try:
                card_level = pyautogui.locateCenterOnScreen('golemdeck/level11.png', confidence = .95, region=[940, 475, 664, 525])
                return card_level
            except pyautogui.ImageNotFoundException:
                pass

    #------------------------------------------------------ OFFENSE -----------------------------------------------------------------------

    def offense(): #not in use currently
        try:
            card_level = pyautogui.locateCenterOnScreen('golemdeck/level11gold2.png', confidence = .9, region=[940, 475, 664, 525])
            return card_level
        except pyautogui.ImageNotFoundException:
            try:
                card_level = pyautogui.locateCenterOnScreen('golemdeck/level11.png', confidence = .95, region=[940, 475, 664, 525])
                return card_level
            except pyautogui.ImageNotFoundException:
                pass