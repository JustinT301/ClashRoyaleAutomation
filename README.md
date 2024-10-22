# Clash Royale Automation Bot

## Table of Contents
1. [Introdution](#introduction)
2. [Features](#features)
3. [Dependencies](#dependencies)
4. [Installation](#installation)
5. [How to Use](#how-to-use)
6. [Credits](#credits)

## Introduction
This is a Clash Royale Automation script that can play, exit matches, and queue into matches (Use at your own risk, this bot breaks Supercell TOS).

## Features
- Plays Clash Royale without user input
- Code is highly customizable, user can create functions for any card
- Has a preset golem nightwitch deck to test out
- Collects and opens chests

## Dependencies
* Python
   * Version: 3.12.4
   * Description: Python is the programming language used to develop this script.
* Google Play Emulator
   * Description: Keep in center of primary monitor (where it opens). 
* OpenCV
   * Version: 4.10.0.84
   * Image Recognition to detect cards.
* MSS
   * Version: 9.0.1
   * Screenshot Module
* NumPy
   * Version: 1.26.3
   * Array computation
* PyWin32
   * Version: 306
   * Clicks on cards, places them, and clicks on battle and exit buttons.
* Keyboard
   * Version: 0.13.5
   * Press 'q' to shutdown script.

## Installation
1. Install Git (Windows)
   * Download the [Git installer for windows](https://gitforwindows.org/).
   * Run the installer and follow the prompts. Ensure to select the option to add Git to your system PATH during installation.
2. Run and Verify Git Installation
   ```sh
   git --version
   ```
3. Navigate to the directory where you want to clone the respository:
   ```sh
   cd Desktop
   ```
4. Clone the repository:
   ```sh
   git clone https://github.com/JustinT301/golembot1.0.git
   ```
5. Navigate to the Cloned Repository:
   ```sh
   cd golembot1.0
   ```
6. Before running the code, ensure you have Python and Dependances installed:
   ```sh
   python --version
   ```
   If Python is not installed, it can be downloaded [here](https://www.python.org/downloads/release/python-3124/)
   ```sh
   pip install -r requirements.txt
   ```

7. Run the Clash Royale Automation bot code:
   ```sh
   python play.py
   ```
## How to Use
1. Open Clash Royale on Google Play Emulator
2. Edit the coordinates to fit your monitor size, the coordinates that will need to be changes are the specific area coordinates, not the ones that click where the image was found.
3. There is a preset golem deck for this, (golem, nightwitch, edrag, babydrag, lumberjack, knight, bats, skeletons/evo skellies), some other cards have been coded in but if a card that you want to use has not been coded in, you can add the images necessary to a folder and use the format of the other cards in cards.py to write your own.
4. Run the game:
   ```sh
   python play.py
   ```

## Credits
* Developed by:
   * Justin Turbyfill
* Date: August 15th, 2024
