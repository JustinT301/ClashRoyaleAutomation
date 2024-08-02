import pyautogui
import time
import keyboard
import random
import os
from cards import Cards
from cr_ui import UI

deck_area = [1069,1163,569,165]
elixir_area = [1050,1270,100,100]
pyautogui.useImageNotFoundException()
elixir_single_time = 2.8 #double elixir is 1.4 seconds per elixir, triple is .933
ui = UI()
cards = Cards()


def main():
    while keyboard.is_pressed('q') == False:

        golem_location = None
        nightwitch_location = None
        rand_skeletons = random.randint(0,10) #RNG to prevent overcommitments
        rand_bats = random.randint(0,10)
        rand_baby_dragon = random.randint(0,5)
        rand_lumberjack = random.randint(0,5)
        rand_knight = random.randint(0,4)
        rand_electro_dragon = random.randint(0,5)

        battle1 = ui.battle()
        if battle1 == 1:
            time.sleep(10)
            pyautogui.screenshot(region=[1020, 222, 100, 100], imageFilename= 'golemdeck/opponents_left_tower.png')

        endgame1 = ui.endgame()
        if endgame1 == 1:
            os.remove('golemdeck/opponents_left_tower.png')

        if rand_skeletons == 0: #looks for then plays cards
            cards.skeletons()
            cards.evo_skeletons()

        if rand_bats == 0:
            cards.bats()
        
        if rand_baby_dragon == 0:
            cards.baby_dragon()
        
        if rand_electro_dragon == 0:
            cards.electro_dragon()

        if rand_lumberjack == 0:
            cards.lumberjack()
        
        if rand_knight == 0:
            cards.knight()


        cards.golem_nightwitch(golem_location, nightwitch_location, elixir_single_time)
        cards.dragon_choice()
        ui.elixir10()

if __name__ == '__main__':
    main()
