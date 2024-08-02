# Clash Royale Automation Bot

## Table of Contents
1. [Introdution](#introduction)
2. [Features](#features)
3. [Dependencies](#dependencies)
4. [Installation](#installation)
5. [How to Use](#how-to-use)
6. [Credits](#credits)

## Introduction
This is a Clash Royale Automation script that can play, exit matches, and queue into matched (Use at your own risk, this bot breaks Supercell TOS).

## Features
- Plays Clash Royale without user input
- Code is highly customizable, user can create functions for any card
- Has a preset golem nightwitch deck to test out
- Currently does not collect chests due to TOS

## Dependencies
* Python
   * Version: 3.12.4
   * Description: Python is the programming language used to develop the Breakout game.
* Google Play Emulator
   * Description: Keep in center of primary monitor (where it opens). 
* PyAutoGUI
   * Version: 0.9.54
   * Image Recognition to detect cards.
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
2. Run the game:
   ```sh
   python play.py
   ```

## Credits
* Developed by:
   * Justin Turbyfill
* Date: August 2nd, 2024