# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS #, set_square_letter, get_square_letter

def wordle():

    # set WordleGWindow class to gw
    gw = WordleGWindow()
    
    # get random word
    randomWord = random.choice(FIVE_LETTER_WORDS)
    #print(randomWord)

    # split random word into 5 distinct letters
    letterList = list(randomWord)

    # set_square_letter to for each item to random list, 
    # then display them on the grid using set_square_letter method 
    gridSpaces = [0,1,2,3,4]
    for i in gridSpaces:
        gw.set_square_letter(0,i,letterList[i])

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()