# CISC/CMPE 204 Modelling Project

Our project uses a logical model to determine the possible answers left in a wordle problem, given that you have a full set of information from the previous five guesses. When given the previous five guesses, the model will specifically return the possible words the correct answer could be. The model does this by taking a text file filled with possible answers and eliminating them as the information is processed.

## Wordle Rules

Wordle is an online guessing game in which you want to guess a selected five letter word from a wordbank within six guesses.

For every guess, information is returned back to the player, telling the player if the letter is incorrect (shown in gray), if the letter is in the word but in the wrong spot (shown in yellow) and if a letter is in the wrod in the right spot (shown in green).

You win the game if you can guess the word within six guesses.

## Files
### test.py
Tests the final output of the program (came with the standard class template).

### WLR.py
The file for word solving  given an example set of words
#### init
initializes the board for the wordle game
#### data
Compiles the data of the guesses and returns none if there are no guesses
#### display
Displays data and returns none if there is no data
#### make_guess
Makes a specific guess with a single string input
#### get_wordlist
Returns a list for wordlist
#### get_correct_word
Returns a String as correct word
#### get_guesses
Returns a list for guesses
#### get_guess_list
Returns a list for guess list
#### get_guess_data
Returns a 2d list for data
#### get_letter_list
Returns a list of letters
#### test_case_1
Gives an example case that can be tested
#### check_letter
Checks letter at a position to see if it's empty
#### remove_invalid
Takes in array of strings (invalid words) and removes from guess_list (of possible words)

### run.py
Attempts to calculate the solution to the wordle problem.
#### wordle_theory
Adds the constraints to the encoding, returns the encoding after adding said constraints

## Structure

* `documents`: Contains folders for both of your draft and final submissions. README.md files are included in both.
* `run.py`: General wrapper script that you can choose to use or not. Only requirement is that you implement the one function inside of there for the auto-checks.
* `test.py`: Run this file to confirm that your submission has everything required. This essentially just means it will check for the right files and sufficient theory size.
