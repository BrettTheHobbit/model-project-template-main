
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

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
    def __init__(self, row, col, status, char):
        self.row = row
        self.col = col
        self.status = status
        self.char = char

    def __repr__(self):
        return f"slot({self.row},{self.col})=>{self.status}"


#Word class, contains five letter classes (same row, diff col)
@proposition(E)
class Word:
    def __init__(self, letter):
        self.word = letter
        self.letter1 = letter[0]
        self.letter2 = letter[1]
        self.letter3 = letter[2]
        self.letter4 = letter[3]
        self.letter5 = letter[4]

    def __repr__(self):
        return f" The word is: " + str(self.letter1.char) + str(self.letter2.char) + str(self.letter3.char) + str(self.letter4.char) + str(self.letter5.char)

    #Returns true if a guess is a good guess, false if guess is a bad guess
    def good_guess():
        #A guess is a good guess IF (defines what a good guess is)
        pass
        
#CONSTRAINTS

#For each slot, there is exactly one status applied to it
for row in ROW:
    for col in COL:
        constraint.add_exactly_one(E, [Letter(row, col, status) for status in STATUS]) #Get char from the char at the index (Fang Lei's class)

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
