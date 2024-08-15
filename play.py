import cv2
import time
import keyboard
import random
import os
from cards import Cards
from cr_ui import UI


elixir_single_time = 2.8  # double elixir is 1.4 seconds per elixir, triple is .933
ui = UI()
cards = Cards()


def main():
    while not keyboard.is_pressed('q'):

        golem_location = None
        nightwitch_location = None
        rand_skeletons = random.randint(0, 10)  # RNG to prevent overcommitments
        rand_bats = random.randint(0, 10)
        rand_baby_dragon = random.randint(0, 5)
        rand_lumberjack = random.randint(0, 5)
        rand_knight = random.randint(0, 4)
        rand_electro_dragon = random.randint(0, 5)

        battle1 = ui.battle()
        if battle1 == 1:
            time.sleep(10)
            screenshot = ui.capture_screenshot(region={'top': 222, 'left': 1020, 'width': 100, 'height': 100})
            cv2.imwrite('golemdeck/opponents_left_tower.png', screenshot)

        endgame1 = ui.endgame()
        if endgame1 == 1:
            if os.path.exists('golemdeck/opponents_left_tower.png'):
                os.remove('golemdeck/opponents_left_tower.png')

        if rand_skeletons == 0:  # looks for then plays cards
            cards.skeletons()
            cards.evo_skeletons()
            time.sleep(0.5)
            continue

        if rand_bats == 0:
            cards.bats()
            time.sleep(0.5)
            continue
            
        if rand_baby_dragon == 0:
            cards.baby_dragon()
            time.sleep(0.5)
            continue
            
        if rand_electro_dragon == 0:
            cards.electro_dragon()
            time.sleep(0.5)
            continue
            
        if rand_lumberjack == 0:
            cards.lumberjack()
            time.sleep(0.5)
            continue
            
        if rand_knight == 0:
            cards.knight()
            time.sleep(0.5)
            continue
            
        cards.golem_nightwitch(golem_location, nightwitch_location, elixir_single_time)
        cards.dragon_choice()
        ui.elixir10()

if __name__ == '__main__':
    main()
