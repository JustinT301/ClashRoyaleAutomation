import cv2
import numpy as np
import time
import random
import win32api, win32con
import mss

class UI:
    def __init__(self):
        self.battle_button_region = {'top': 815, 'left': 1040, 'width': 300, 'height': 180} 
        #formatted as y1,x1,x2,y2 where x1,y1 is the top left point, x2 is how far to the right and y2 is how far down
        self.ok_button_region = {'top': 1173, 'left': 1173, 'width': 210, 'height': 110}
        self.elixir10_region = {'top': 1318, 'left': 1518, 'width': 150, 'height': 100}
        self.deck_x = [1131, 1272, 1429, 1572]

    def click(self, x, y):
        win32api.SetCursorPos((x, y)) #formatted as x,y (standard position formatting)
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

    def battle(self):  # looks for battle button
        try:
            battle_button_location = self.find_image('golemdeck/battlebutton2.png', confidence=0.7, region=self.battle_button_region)
            if battle_button_location:
                self.click(battle_button_location[0] + 5, battle_button_location[1] + 5)
                return 1
        except Exception as e:
            pass
            #print(f"Error finding battle button: {e}")
        return 0

    def endgame(self):  # looks for OK button when match ends then looks for chests to open or unlock
        try:
            ok_button_location = self.find_image('golemdeck/ok.png', confidence=0.7, region=self.ok_button_region)
            if ok_button_location:
                self.click(ok_button_location[0] + 1, ok_button_location[1] + 1)
                time.sleep(2)
                self.chests()
                return 1
        except Exception as e:
            pass
            #print(f"Error finding OK button: {e}")
        return 0
    
    def chests(self):
        try:
            open_chest_location = self.find_image('golemdeck/open.png', confidence=0.95, region={'top': 1181, 'left': 914, 'width': 740, 'height': 70})
            if open_chest_location:
                self.click(open_chest_location[0] + 5, open_chest_location[1] + 5)
                time.sleep(0.5)
                for _ in range(10):
                    self.click(1515,700)
                    time.sleep(0.25)
        except Exception as e:
            pass

        try:
            chest_opening_location = self.find_image('golemdeck/chest_timer.png', confidence=0.7, region={'top': 1015, 'left': 900, 'width': 625, 'height': 50})
            if not chest_opening_location:
                self.click(990, 1142)
                time.sleep(0.5)
                self.click(1257,950)
        except Exception as e:
            pass

    def elixir10(self):  # prevents leaking elixir
        try:
            elixir10_location = self.find_image('golemdeck/elixir10.png', confidence=0.7, region=self.elixir10_region)
            if elixir10_location:
                self.click(elixir10_location[0] + 1, elixir10_location[1] + 1)
                self.click(random.choice(self.deck_x), 1243)
                self.click(1251, 1051)
                time.sleep(0.25)
        except Exception as e:
            pass
            #print(f"Error finding elixir 10 indicator: {e}")

