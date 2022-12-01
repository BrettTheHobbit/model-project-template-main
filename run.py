
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
POSSIBLE_LETTER1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
POSSIBLE_LETTER2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
POSSIBLE_LETTER3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
POSSIBLE_LETTER4 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
POSSIBLE_LETTER5 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
BOARD = WLR.Wordle_board("words.txt", 15)
guess_list = BOARD.get_guess_list()


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

        
#BASIC CONSTRAINTS

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

#If the letter is partial, it is correct in the  one of the other four slots
for row in ROW:
    for p in POSSIBLE_LETTER:
        E.add_constraint(Guess(row, 1, STATUS[2], p) >> (Guess(row, 2, STATUS[0], p) | Guess(row, 3, STATUS[0], p) | Guess(row, 4, STATUS[0], p) | Guess(row, 5, STATUS[0], p)))
        E.add_constraint(Guess(row, 2, STATUS[2], p) >> (Guess(row, 1, STATUS[0], p) | Guess(row, 3, STATUS[0], p) | Guess(row, 4, STATUS[0], p) | Guess(row, 5, STATUS[0], p)))
        E.add_constraint(Guess(row, 3, STATUS[2], p) >> (Guess(row, 2, STATUS[0], p) | Guess(row, 1, STATUS[0], p) | Guess(row, 4, STATUS[0], p) | Guess(row, 5, STATUS[0], p)))
        E.add_constraint(Guess(row, 4, STATUS[2], p) >> (Guess(row, 2, STATUS[0], p) | Guess(row, 3, STATUS[0], p) | Guess(row, 1, STATUS[0], p) | Guess(row, 5, STATUS[0], p)))
        E.add_constraint(Guess(row, 5, STATUS[2], p) >> (Guess(row, 2, STATUS[0], p) | Guess(row, 3, STATUS[0], p) | Guess(row, 4, STATUS[0], p) | Guess(row, 1, STATUS[0], p)))

#If there are five correct letters, then the word is correct
for row in ROW:
    for p in POSSIBLE_LETTER:
        E.add_constraint((Guess(row, 1, STATUS[0], p) & Guess(row, 2, STATUS[0], p) & Guess(row, 3, STATUS[0], p) & Guess(row, 4, STATUS[0], p) & Guess(row, 5, STATUS[0], p)) >> Word(Guess(row, 1, STATUS[0], p).letter + Guess(row, 2, STATUS[0], p).letter + Guess(row, 3, STATUS[0], p).letter + Guess(row, 4, STATUS[0], p).letter + Guess(row, 5, STATUS[0], p).letter, True))

#SOLVING CONSTRAINTS

#If we run out of letters in letter bank allow duplicate letters 

#IF there are 5 partially correct letter and totally correct letters, start trying to guess the word

#If the letter is not in the correct word,then all words in the wordlist with incorrect letters should be removed
for row in ROW:
    for p in POSSIBLE_LETTER:
        full_word = Guess(row, 1, STATUS[1], p).letter + Guess(row, 2, STATUS[1], p).letter + Guess(row, 3, STATUS[1], p).letter + Guess(row, 4, STATUS[1], p).letter + Guess(row, 5, STATUS[1], p).letter
        E.add_constraint((Guess(row, 1, STATUS[1], p) & Guess(row, 2, STATUS[1], p) & Guess(row, 3, STATUS[1], p) & Guess(row, 4, STATUS[1], p) & Guess(row, 5, STATUS[1], p)) >> Word(full_word, False))
        if(Word(full_word, False)== True):
            remove_word_list = []
            current_list_size = range(len(guess_list))
            for x in current_list_size:
                if re.search([full_word[0],full_word[1],full_word[2],full_word[3],full_word[4]],x.upper()) == True:
                    remove_word_list.append(x)
            guess_list = BOARD.remove_invalid(remove_word_list)
 
#If the correct letter is in the right position, then remove all words without the correct letter from word list
    #Check if the correct letter is in the correct position
def remove_word(col, letter):
    remove_word_list = guess_list.copy()
    for x in range(len(guess_list)):
        if x[col] == letter:
            remove_word_list.remove(x)
    guess_list = BOARD.remove_invalid(remove_word_list)


for row in ROW:
    for col in COL:
        for letter in POSSIBLE_LETTER:
            exclusion_list = POSSIBLE_LETTER.copy().remove(letter)
            #E.add_constraint(SlotStatus(row, col, STATUS[0]) & SlotLetter(row, col letter) >> )
            E.add_constraint(Guess(row, col, STATUS[0], letter) >> ~(Guess(row, col, STATUS[0], exclusion_list)))
            if(Guess(row, col, STATUS[0], letter) == True):
                remove_word(col, letter)

# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    # Add custom constraints by creating formulas with the variables you created. 
    #E.add_constraint((a | b) & ~x)
    # Implication
    #E.add_constraint(y >> z)
    # Negate a formula
    #E.add_constraint(~(x & y))
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BasicPropositions, but you want to enforce it for a, b, and c.:
    #constraint.add_exactly_one(E, a, b, c)

    return E


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
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
