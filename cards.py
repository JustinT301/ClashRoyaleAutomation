import cv2
import numpy as np
import time
import random
import win32api, win32con
import mss

class Cards:
    def __init__(self):
        self.deck_area = {'top': 1163, 'left': 1069, 'width': 569, 'height': 165}  # Convert to dict for mss
        self.dragon_list = ['golemdeck/mybabydragon.png', 'golemdeck/myelectrodragon.png']

    def click(self, x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def capture_screenshot(self, region=None):
        with mss.mss() as sct:
            screenshot = sct.grab(region) if region else sct.grab(sct.monitors[1])
            return np.array(screenshot)

    def find_image(self, template_path, confidence, region=None):
        screenshot = self.capture_screenshot(region)
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template_path, 0)
        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        location = np.where(result >= confidence)
        if location[0].size > 0:
            return (location[1][0] + region['left'], location[0][0] + region['top']) if region else (location[1][0], location[0][0])
        return None

    def skeletons(self): #basic template for majority of cards
        try:
            skeletons_locationation = self.find_image('golemdeck/myskeletons.png', confidence=0.8, region=self.deck_area)
            if skeletons_locationation:
                cards_found = self.defense()
                self.click(skeletons_locationation[0] + 1, skeletons_locationation[1] + 1)
                if cards_found:
                    self.click(cards_found[0], cards_found[1])
                else:
                    self.click(random.randint(956, 1606), random.randint(655, 1061))
        except Exception as e:
            pass
            #print(f"Error finding skeletons: {e}")

    def evo_skeletons(self):
        try:
            evo_skeletons_locationation = self.find_image('golemdeck/myevoskeletons.png', confidence=0.9, region=self.deck_area)
            if evo_skeletons_locationation:
                cards_found = self.defense()
                self.click(evo_skeletons_locationation[0] + 1, evo_skeletons_locationation[1] + 1)
                if cards_found:
                    self.click(cards_found[0], cards_found[1])
        except Exception as e:
            pass
            #print(f"Error finding evo skeletons: {e}")

    def bats(self):
        try:
            bats_locationation = self.find_image('golemdeck/mybats.png', confidence=0.9, region=self.deck_area)
            if bats_locationation:
                cards_found = self.defense()
                if cards_found:
                    self.click(bats_locationation[0], bats_locationation[1])
                    self.click(cards_found[0], cards_found[1] + 100)
        except Exception as e:
            pass
            #print(f"Error finding bats: {e}")

    def golem_nightwitch(self, golem_locationation, nightwitch_locationation, elixir_single_time): #Main offensive push
        golemx = 1261
        nightwitchx = 1151
        try:
            golem_locationation = self.find_image('golemdeck/mygolem.png', confidence=0.95, region=self.deck_area)
            nightwitch_locationation = self.find_image('golemdeck/mynightwitch.png', confidence=0.9, region=self.deck_area)
            if golem_locationation and nightwitch_locationation:
                try:
                    self.find_image('golemdeck/opponents_left_tower.png', confidence=0.3, region={'top': 222, 'left': 1020, 'width': 100, 'height': 100})
                    print("Left tower is there")
                except:
                    print("Left tower isn't there")
                    golemx = 1296
                    nightwitchx = 1407
                self.click(golem_locationation[0] + 1, golem_locationation[1] + 1)
                self.click(golemx, 1059)
                time.sleep(elixir_single_time * 4)
                self.click(nightwitch_locationation[0] + 1, nightwitch_locationation[1] + 1)
                self.click(nightwitchx, 932)
        except Exception as e:
            pass
            #print(f"Error finding golem or nightwitch: {e}")

    def dragon_choice(self):
        dragon_choice = random.choice(self.dragon_list)
        try:
            dragon_choice_locationation = self.find_image(dragon_choice, confidence=0.9, region=self.deck_area)
            if dragon_choice_locationation:
                push_locationation = self.find_image('golemdeck/golemnwpush.png', confidence=0.9)
                if push_locationation:
                    self.click(dragon_choice_locationation[0] + 3, dragon_choice_locationation[1] + 3)
                    self.click(push_locationation[0] + 30, push_locationation[1] + 200)
        except Exception as e:
            pass
            #print(f"Error finding dragon or push locationation: {e}")

    def baby_dragon(self):
        try:
            baby_dragon_locationation = self.find_image('golemdeck/mybabydragon.png', confidence=0.9, region=self.deck_area)
            if baby_dragon_locationation:
                cards_found = self.defense()
                if cards_found:
                    self.click(baby_dragon_locationation[0], baby_dragon_locationation[1])
                    self.click(cards_found[0], cards_found[1] + 50)
        except Exception as e:
            pass
            #print(f"Error finding baby dragon: {e}")

    def lumberjack(self):
        try:
            lumberjack_locationation = self.find_image('golemdeck/mylumberjack.png', confidence=0.9, region=self.deck_area)
            if lumberjack_locationation:
                cards_found = self.defense()
                if cards_found:
                    self.click(lumberjack_locationation[0], lumberjack_locationation[1])
                    self.click(cards_found[0], cards_found[1])
        except Exception as e:
            pass
            #print(f"Error finding lumberjack: {e}")

    def knight(self):
        try:
            knight_locationation = self.find_image('golemdeck/myknight.png', confidence=0.9, region=self.deck_area)
            if knight_locationation:
                cards_found = self.defense()
                if cards_found:
                    self.click(knight_locationation[0], knight_locationation[1])
                    self.click(cards_found[0], cards_found[1])
        except Exception as e:
            pass
            #print(f"Error finding knight: {e}")

    def electro_dragon(self):
        try:
            electro_dragon_locationation = self.find_image('golemdeck/myelectrodragon.png', confidence=0.9, region=self.deck_area)
            if electro_dragon_locationation:
                cards_found = self.defense()
                if cards_found:
                    self.click(electro_dragon_locationation[0], electro_dragon_locationation[1])
                    self.click(cards_found[0], cards_found[1] + 100)
        except Exception as e:
            pass
            #print(f"Error finding electro dragon: {e}")

    #--------------------------------------------------------- DEFENSE -----------------------------------------------------------------------

    def defense(self):
        try:
            card_level = self.find_image('golemdeck/lvl11gold.png', confidence=0.8, region={'top': 475, 'left': 940, 'width': 664, 'height': 525})
            if card_level:
                return card_level
        except Exception as e:
            pass
            #print(f"Error finding level 11 gold card: {e}")

            try:
                card_level = self.find_image('golemdeck/level11.png', confidence=0.8, region={'top': 475, 'left': 940, 'width': 664, 'height': 525})
                if card_level:
                    return card_level
            except Exception as e:
                pass
                #print(f"Error finding level 11 card: {e}")

        return None

    #------------------------------------------------------ OFFENSE -----------------------------------------------------------------------

    def offense(self): #not in use currently
        try:
            card_level = self.find_image('golemdeck/level11gold2.png', confidence=0.9, region={'top': 475, 'left': 940, 'width': 664, 'height': 525})
            if card_level:
                return card_level
        except Exception as e:
            pass
            #print(f"Error finding level 11 gold card: {e}")

        try:
            card_level = self.find_image('golemdeck/level11.png', confidence=0.95, region={'top': 475, 'left': 940, 'width': 664, 'height': 525})
            if card_level:
                return card_level
        except Exception as e:
            pass
            #print(f"Error finding level 11 card: {e}")

        return None
