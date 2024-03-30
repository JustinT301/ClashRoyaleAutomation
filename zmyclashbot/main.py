from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import os
from cards import *
from cr_ui import *


deck_area = [1069,1163,569,165]
elixir_area = [1050,1270,100,100]
#cycle_click = [[1000,1000],[],[],[],[],[],[],[],[],[]] #put coords to randomly choose
pyautogui.useImageNotFoundException()
#single_elixir_start = time.time()
elixir_single_time = 2.8
elixir_double_time = 1.4
elixir_triple_time = 0.93333334

def main():
    #single_elixir(deck_area, elixir_area, cycle_click) potential idea
    #double_elixir(deck_area, elixir_area, cycle_click)
    #triple_elixir(deck_area, elixir_area, cycle_click)
    left_tower_screenshot = None
#def single_elixir(deck_area, elixir_area, cycle_click):
    while keyboard.is_pressed('q') == False:
        start = time.time()
        golem_location = None
        nightwitch_location = None
        rand_skeletons = random.randint(0,10)
        rand_bats = random.randint(0,10)
        rand_baby_dragon = random.randint(0,5)
        rand_lumberjack = random.randint(0,5)
        rand_knight = random.randint(0,4)
        rand_electro_dragon = random.randint(0,5)

        battle1 = battle()
        if battle1 == 1:
            time.sleep(10)
            pyautogui.screenshot(region=[1020, 222, 100, 100], imageFilename= 'golemdeck/leftower1234.png')

        endgame1 = endgame()
        if endgame1 == 1:
            os.remove('golemdeck/leftower1234.png')

        #if rand_bomber == 0:
        #    bomber()

        if rand_skeletons == 0:
            skeletons()
            evo_skeletons()

        if rand_bats == 0:
            bats()
        
        if rand_baby_dragon == 0:
            baby_dragon()
        
        if rand_electro_dragon == 0:
            baby_dragon()

        if rand_lumberjack == 0:
            lumberjack()
        
        if rand_knight == 0:
            knight()
            #arrows()

        #if rand_archers == 0:
        #    archers()

        golem_nightwitch(golem_location, nightwitch_location, elixir_single_time)
        dragon_choice()
        elixir10()

        end = time.time()
        print(f"time = {end-start}")
        
        #single_elixir_end = time.time()
        #elapsed_time_1x = single_elixir_end - single_elixir_start
        #if elapsed_time_1x >= 120: #change this if statement to also work for getting from 2x to 3x
        #    break

        #time.sleep(.5)

if __name__ == '__main__':
    main()

#THINGS TO FIX:
    #1. figure out why sometimes golem gets clicked when below 8 elixir, may be confidence issue
    #possibly fixed by perfect confidence value, pretty much fixed by now

    #2. work on arrows, baby dragon, and evo skeletons
    #3. figure out defense
    #4. create viable card order
    #5. rework clone, possibly with lower confidence and left lane region
    #6. eventually add 2x elixir and 3x elixir mode

    #7. add a coordinate list with alotta coordinates for random to choose from for cycle cards
    #here = [[1000,1000],[1200,1200]]
    #click(here[0][0], here[0][1])

    #8. try to move some of the cards over to another .py file
    #9. fix region 2 not found for arrows
    #10. use for loop to check multiple images for defense
    #11. make cycle units or baby drag get dropped if elixir hits 10
    #12. get pol arena images (gonna have to play games and stall against challenger 1 players, maybe screen record it to get screenshots)