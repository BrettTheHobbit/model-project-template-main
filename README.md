# CISC/CMPE 204 Modelling Project

Our project uses a logical model to determine the possible answers left in a wordle problem, given that you have a full set of information from the previous five guesses. When given the previous five guesses, the model will specifically return the possible words the correct answer could be. The model does this by taking a text file filled with possible answers and eliminating them as the information is processed.

## Wordle Rules

Wordle is an online guessing game in which you want to guess a selected five letter word.

## Structure

* `documents`: Contains folders for both of your draft and final submissions. README.md files are included in both.
* `run.py`: General wrapper script that you can choose to use or not. Only requirement is that you implement the one function inside of there for the auto-checks.
* `test.py`: Run this file to confirm that your submission has everything required. This essentially just means it will check for the right files and sufficient theory size.
