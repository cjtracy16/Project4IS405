# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        # Get row from
        row = gw.get_current_row()

        # Get word from window:
        wordLeters = []
        for col in range(0, 5):
            wordLeters.append(gw.get_square_letter(row, col))

        word = ''.join(wordLeters)
        word = word.lower()

        # Checks to see if the entered word is a legitimate word

        # If NOT a legitmate word then display: "Not in word list
        if word in FIVE_LETTER_WORDS:
            # If legitimate word then display a positive message
            gw.show_message("You have to implement this method.")

        else:
            gw.show_message("Not in word list.")

        

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    

# Startup code

if __name__ == "__main__":
    wordle()
