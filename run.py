
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
import WLR

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
LETTER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
BOARD = WLR.Wordle_board("words.txt", 15)

PROPOSITIONS = []

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
    def __init__(self, row, guess, isWord):
        self.row = row
        self.guess = guess#Is a collection of five letter classes
        self.isWord = isWord#is it a word in the wordlist, a guess must match one of the words in the wordlist

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
        constraint.add_at_most_one(E, [SlotLetter(row, col, letter) for letter in LETTER])

#ADVANCED CONSTRAINTS

#If the letter is blank then the status must be empty and vice versa

# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    # Add custom constraints by creating formulas with the variables you created. 
    E.add_constraint((a | b) & ~x)
    # Implication
    E.add_constraint(y >> z)
    # Negate a formula
    E.add_constraint(~(x & y))
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BasicPropositions, but you want to enforce it for a, b, and c.:
    constraint.add_exactly_one(E, a, b, c)

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
