
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
import WLR
import re

# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class BasicPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

ROW = [1, 2, 3, 4, 5, 6]
COL = [1, 2, 3, 4, 5]
STATUS = ["CORRECT", "INCORRECT", "PARTIAL", "EMPTY"]
POSSIBLE_LETTER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
BOARD = WLR.Wordle_board("words.txt", 15)



PROPOSITIONS = []
WRONG_GUESSES = []
class Unique(object):
    def __hash__(self):
        return hash(str(self))
    def __eq__(self, other):
        return hash(self) == hash(other)
    def __repr__(self):
        return str(self)
    def __str__(self):
        assert False, "You need to define the __str__ function on a proposition class"


#Contains the information about a letters location, status and the char representation on the wordle board
 
@proposition(E)
class Slots:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    

    def __repr__(self):
        return f"slot({self.row},{self.col})"

#Holds the slot coordinates with it's status (from STATUS)
@proposition(E)
class SlotStatus:
    def __init__(self, row, col, status):
        self.row = row
        self.col = col
        self.status = status

    def __repr__(self):
        return f"slot({self.row},{self.col})=>{self.status}"

#Holds info about the slot and the letter IN the slot
@proposition(E)
class SlotLetter:
    def __init__(self, row, col, letter):
        self.row = row
        self.col = col
        self.letter = letter

    def __repr__(self):
        return f"{self.letter} at slot({self.row},{self.col})"

@proposition(E)
class Guess:
    def __init__(self, row, col, status, letter):
        self.row = row
        self.col = col
        self.status = status
        self.letter = letter

#Word class, contains a word from the set of possible words and checks if it matches
@proposition(E)
class Word:
    def __init__(self, word, pos_guess):
        self.word = word
        self.pos_guess = pos_guess

    def __repr__(self):
        return f" The word is: " + str(self.word) + ". Guess status: " + str(self.pos_guess)

        
# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def wordle_theory():
   #Adds constraints
#BASIC CONSTRAINTS 
    guessed_list = BOARD.get_guess_list()
    print("guess list idk" + str(guessed_list))

    if(len(guessed_list) > 1):
#Each row maps to every column
        for row in ROW:
            for col in COL:
                constraint.add_at_most_one(E, Slots(row, col))

        #For each slot, there is exactly one status applied to it
        for row in ROW:
            for col in COL:
                constraint.add_at_most_one(E, [SlotStatus(row, col, status) for status in STATUS]) #Get char from the char at the index (Fang Lei's class)

        #For each slot, there is exactly one letter applied to it
        for row in ROW:
            for col in COL:
                constraint.add_at_most_one(E, [SlotLetter(row, col, letter) for letter in POSSIBLE_LETTER])

        #Each letter has a position and a status (by adding two constraints, the result should be the intersection of them)
        for row in ROW:
            for col in COL:
                for letter in POSSIBLE_LETTER:
                    constraint.add_at_most_one(E, [Guess(row, col, status, letter) for status in STATUS])

        for row in ROW:
            for col in COL:
                for status in STATUS:
                    constraint.add_at_most_one(E, [Guess(row, col, status, letter) for letter in POSSIBLE_LETTER])

        #ADVANCED CONSTRAINTS

        #If the letter is blank then the status must be empty and vice versa
        for row in ROW:
            for col in COL:
                E.add_constraint(SlotLetter(row, col, "BLANK") >> SlotStatus(row, col, STATUS[3]))

        for row in ROW:
            for col in COL:
                E.add_constraint(SlotStatus(row, col, STATUS[3]) >> SlotLetter(row, col, "BLANK"))

        for row in ROW:
            for word in guessed_list:
                E.add_constraint(Guess(row, 1, STATUS[2], word[0]) >> (Guess(row, 2, STATUS[0], word[1]) | Guess(row, 3, STATUS[0], word[2]) | Guess(row, 4, STATUS[0], word[3]) | Guess(row, 5, STATUS[0], word[4])))
                E.add_constraint(Guess(row, 2, STATUS[2], word[1]) >> (Guess(row, 1, STATUS[0], word[0]) | Guess(row, 3, STATUS[0], word[2]) | Guess(row, 4, STATUS[0], word[3]) | Guess(row, 5, STATUS[0], word[4])))
                E.add_constraint(Guess(row, 3, STATUS[2], word[2]) >> (Guess(row, 2, STATUS[0], word[1]) | Guess(row, 1, STATUS[0], word[0]) | Guess(row, 4, STATUS[0], word[3]) | Guess(row, 5, STATUS[0], word[4])))
                E.add_constraint(Guess(row, 4, STATUS[2], word[3]) >> (Guess(row, 2, STATUS[0], word[1]) | Guess(row, 3, STATUS[0], word[2]) | Guess(row, 1, STATUS[0], word[0]) | Guess(row, 5, STATUS[0], word[4])))
                E.add_constraint(Guess(row, 5, STATUS[2], word[4]) >> (Guess(row, 2, STATUS[0], word[1]) | Guess(row, 3, STATUS[0], word[2]) | Guess(row, 4, STATUS[0], word[3]) | Guess(row, 1, STATUS[0], word[0])))

        #If there are five correct letters, then the word is correct
        for row in ROW:
            for word in guessed_list:
                E.add_constraint((Guess(row, 1, STATUS[0], word[0]) & Guess(row, 2, STATUS[0], word[1]) & Guess(row, 3, STATUS[0], word[2]) & Guess(row, 4, STATUS[0], word[3]) & Guess(row, 5, STATUS[0], word[4])) >> Word(word, True))
        #SOLVING CONSTRAINTS

        #If we run out of letters in letter bank allow duplicate letters 

        #IF there are 5 partially correct letter and totally correct letters, start trying to guess the word

        #If the letter is not in the correct word,then all words in the wordlist with incorrect letters should be removed
        #If the letter is not in the correct word,then all words in the wordlist with incorrect letters should be removed
        for row in ROW:
            for word in guessed_list:
                E.add_constraint((Guess(row, 1, STATUS[1], word[0]) & Guess(row, 2, STATUS[1], word[1]) & Guess(row, 3, STATUS[1], word[2]) & Guess(row, 4, STATUS[1], word[3]) & Guess(row, 5, STATUS[1], word[4])) >> Word(word, False))
                if(Word(word, False)== True):
                    remove_word_list = []
                    current_list_size = range(len(guessed_list))
                    for x in current_list_size:
                        if re.search([word[0],word[1],word[2],word[3],word[4]],x.upper()) == True:
                            remove_word_list.append(x)
                    BOARD.remove_invalid(remove_word_list)
                    guessed_list = BOARD.get_guess_list()
        #If the correct letter is in the right position, then remove all words without the correct letter from word list
            #Check if the correct letter is in the correct position
        def remove_word(col, letter):
            remove_word_list = guessed_list.copy()
            for x in range(len(guessed_list)):
                if x[col] == letter:
                    remove_word_list.remove(x)
            BOARD.remove_invalid(remove_word_list)
            guessed_list = BOARD.get_guess_list()


        for row in ROW:
            for col in COL:
                for letter in POSSIBLE_LETTER:
                    exclusion_list = POSSIBLE_LETTER.copy().remove(letter)
                    #E.add_constraint(SlotStatus(row, col, STATUS[0]) & SlotLetter(row, col letter) >> )
                    E.add_constraint(Guess(row, col, STATUS[0], letter) >> ~(Guess(row, col, STATUS[0], exclusion_list)))
                    if(Guess(row, col, STATUS[0], letter) == True):
                        remove_word(col, letter)
    else:
        return E


if __name__ == "__main__":
    T = wordle_theory()
    # Don't compile until you're finished adding all your constraints!
    T = E.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    #print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()
