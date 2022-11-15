
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

ROW = [1, 2, 3, 4, 5]
COL = [1, 2, 3, 4, 5, 6]
STATUS = ["CORRECT", "INCORRECT", "PARTIAL", "EMPTY"]
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
class Letter: 
    def __init__(self, col, status):
        self.col = col
        self.status = status

    def __repr__(self):
        return f"slot({self.row},{self.col})=>{self.status}"


#Word class, contains five letter classes (same row, diff col)
@proposition(E)
class Word:
    def __init__(self, row, word, pos_guess):
        self.row = row
        self.word = word
        self.pos_guess = pos_guess

    def __repr__(self):
        return f" The word is: " + str(self.word) + ". Guess status: " + str(self.pos_guess)

        
#CONSTRAINTS

#For each slot, there is exactly one status applied to it
for col in COL:
    constraint.add_at_most_one(E, [Letter(col, status) for status in STATUS]) #Get char from the char at the index (Fang Lei's class)

#For incorrect guesses
for row in ROW:
    for word in WORD:
        for col in COL:
            E.add_constraint(Word(row,word,pos_guess) >> Letter(col,STATUS[1])) #basically somehow we change pos_guess to false and then we remove from the wordbank
            #E.add_constraint(Letter(row, col, STATUS[1]) >> Word(words, False))#NEEDS TO BE UPDATED BUT IS A GOOD START
#For partially correct guesses

#For correct guesses

#There is at least one word (guess) that is correct completely

#For each guess, all five letters are in the same row.

#A guess can only be good or bad (G(x) v B(x)^~(G(x)^B(x))) [NEEDS A CLASS FOR A GOOD GUESS AND A BAD GUESS]

#If letter (at row col) is correct guess, then that implies all words with the same letter in the same slot will be possible answers


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
