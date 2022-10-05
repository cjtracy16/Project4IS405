import random

from WordleDictionary import FIVE_LETTER_WORDS

from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR, WordleGWindow, N_COLS, N_ROWS #, set_square_letter, get_square_letter


def wordle():

    # set WordleGWindow class to gw
    gw = WordleGWindow()
    
    # get random word
    randomWord = random.choice(FIVE_LETTER_WORDS)
    #print(randomWord)

    # split random word into 5 distinct letters
    letterList = list(randomWord)
    letterList = letterList

    correctWord = ''.join(letterList)
    correctWord = correctWord.lower()
    print(correctWord) #! !!!!COMMENT OR REMOVE THIS BEFORE SUBMITTING!!!!

    # set_square_letter to for each item to random list, 
    # then display them on the grid using set_square_letter method 
    # gridSpaces = [0,1,2,3,4]
    # for i in gridSpaces:
    #     gw.set_square_letter(0,i,letterList[i])


    def enter_action(s):
        # Get row from
        row = gw.get_current_row()

        # Get word from window:
        wordLetters = []
        for col in range(0, 5):
            wordLetters.append(gw.get_square_letter(row, col).lower())

        guessedWord = ''.join(wordLetters)
        guessedWord = guessedWord
        print(guessedWord) #! !!!!COMMENT OR REMOVE THIS BEFORE SUBMITTING!!!!

        # Checks to see if the entered word is a legitimate word       
        if guessedWord in FIVE_LETTER_WORDS:
            # If the word matches exactly
            if correctWord == guessedWord:
                for spot in range(0, 5):
                    gw.set_square_color(row, spot, CORRECT_COLOR)

                if row == 0:
                    gw.show_message("You guessed the word in " + str(row + 1) + " guess!")
                else:
                    gw.show_message("You guessed the word in " + str(row + 1) + " guesses!")

                #END GAME <NEED TO IMPLEMENT>
            
            # If the word doesn't match exactly Update Colors and Squares
            else:
                for spot in range(0, 5):
                    # If correct letter && correct spot === turn green (CORRECT_COLOR); Can reuse letter
                    if wordLetters[spot] == letterList[spot]:
                        gw.set_square_color(row, spot, CORRECT_COLOR)
                        gw.show_message("Incorrect. Keep Guessing")
             
                    # If correct letter NOT correct spot == turn yellow (PRESENT_COLOR); Can reuse letter
                    elif wordLetters[spot] in letterList:
                        gw.set_square_color(row, spot, PRESENT_COLOR)
                        gw.show_message("Incorrect. Keep Guessing")

                    # If NOT correct letter && NOT correct spot == turn red (MISSING_COLOR); Can't letter
                    else:
                        gw.set_square_color(row, spot, MISSING_COLOR)
                        gw.show_message("Incorrect. Keep Guessing")        

                # Increment row for next guess
                row += 1
                gw.set_current_row(row)

        # If NOT a legitmate word then display: "Not in word list
        else:
            gw.show_message("Not in word list.")

        

    # gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    
# Startup code

if __name__ == "__main__":
    wordle()