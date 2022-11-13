import random


class Wordle_board:
    
    """
    Parameters
    file - the name of the file
    wordlist - original list of words when initialized
    guesses - guesses made
    guess_list - wordlist excluding all the guesses
    guess_data - Data table showing letters that are incorrect, partially correct, or correct
    
    guesslist and guesses should logically add up to wordlist
    """
    
    
    file = ""
    wordlist = []
    correct_word = ""
    guesses = []
    guess_list = []
    guess_data = []
    
    
    
    """
    Parameters
    file - name of file to open with list of words
    listsize - Size of the word pool you wish to have
    
    
    Initializes a list of words of size int listsize from String file and then picks out a word to be the correct word
    """
    def __init__(self, file, listsize):
        self.file = file
        
        f = open(self.file, "r")
        
        for x in f:
            self.wordlist.append(x.strip())
        #Prints words
        #Print(self.wordlist)
        #Prints self.wordlist
        #print(len(self.wordlist))
        
        while len(self.wordlist) > listsize:
            purgePos = random.randint(0, len(self.wordlist)-1)
            self.wordlist.pop(purgePos)
        
        #Prints self.wordlist and size of word list
        #print(self.wordlist)
        #print(len(self.wordlist))
        
        self.guess_list = self.wordlist.copy()
        self.correct_word = self.wordlist[random.randint(0, len(self.wordlist)-1)]
        print("The correct word is: "+self.correct_word)
        
    
        #print(self.wordlist)
        #print(len(self.wordlist))
        
        
    """
    Parameters
    guess - the amount of guesses you're making
    
    Makes guesses equal to int guess
    
    Useless function now
    """
    def auto_guess(self, guess):
        self.guesses = []
        
        
        
        while (len(self.guesses) < guess):
            guess_pos = random.randint(0, len(self.guess_list)-1)
            candidate_guess = self.guess_list[guess_pos]
            if candidate_guess == self.correct_word:
                continue
            self.guesses.append(candidate_guess)
            self.guess_list.pop(guess_pos)
        
        print(self.wordlist)
        print(self.guess_list)
        print(self.guesses)
        
    
    """
    Compiles the data of the guesses
    
    returns none if there are no guesses
    """
    def data(self):
        self.guess_data = []
        
        if self.guesses == []:
            print("There are no guesses")
            return None
        
        for i in range(len(self.guesses)):
            self.guess_data.append([])
        
        #print(self.guess_data)
        
        for i in range(len(self.guesses)):
            correct = self.correct_word
            print(self.guesses[i])
            for j in range(len(self.guesses[i])):
                #print(self.guesses[i][j])
                if self.guesses[i][j] in self.correct_word[j]:
                    self.guess_data[i].append("C")
                    continue
                
                if self.guesses[i][j] in self.correct_word:
                    if self.guesses[i].count(self.guesses[i][j]) > 1:
                        self.guess_data[i].append(ord(self.guesses[i][j]))
                        continue
                    self.guess_data[i].append("P")
                    continue
                
                self.guess_data[i].append("I")
            
            dupes = False
            dupe_dict = {}
            for j in range(len(self.guesses[i])):
                if isinstance(self.guess_data[i][j], int):
                    if self.guess_data[i][j] in dupe_dict:
                        dupe_dict[self.guess_data[i][j]] += 1
                        print(dupe_dict[self.guess_data[i][j]])
                    else:
                        dupe_dict.update({self.guess_data[i][j]:1})
                        print("no")
                    dupes = True
                    
            for j in range(len(self.guesses[i])):
                if self.guesses[i][j] in self.correct_word[j] and ord(self.guesses[i][j]) in dupe_dict:
                    dupe_dict[ord(self.guesses[i][j])] -= 1
            #print(dupes)
            
            #print(dupe_dict)
            
            for key in dupe_dict:
                while key in self.guess_data[i]:
                    if dupe_dict[key] > 0:
                        self.guess_data[i][self.guess_data[i].index(key)] = "P"
                        dupe_dict[key] -= 1
                        continue
                    self.guess_data[i][self.guess_data[i].index(key)] = "I"
                    
                
                #print(key)
                #print(dupe_dict[key])
                #print(self.guess_data[i].index(key))
                #print(key in self.guess_data[i])
                
            
    """
    Displays data
    
    returns none if there is no data
    """
    def display(self):
        
        if self.guess_data == []:
            print("There is no data")
            return None        
        
        for i in self.guess_data:
            print(i)
        print(self.correct_word)
    
    
    """
    Makes a specific guess with a single string input
    """
    def make_guess(self, guess):
        self.guesses.append(guess)
        
        if guess in self.guess_list:
            self.guess_list.remove(guess)
            
    """
    Returns a list for wordlist
    """
    def get_wordlist(self):
        return self.wordlist.copy()
    
    
    """
    Returns a String as correct word
    """    
    def get_correct_word(self):
        return self.correct_word[:]
    
    
    """
    Returns a list for guesses
    """    
    def get_guesses(self):
        return self.guesses.copy()
    
    
    """
    Returns a list for guess list
    """    
    def get_guess_list(self):
        return self.guess_list.copy()
    
    
    """
    Returns a 2d list for data
    """
    def get_guess_data(self):
        return self.guess_data.copy()   
        
        
        
w1 = Wordle_board("words.txt", 15)
w1.auto_guess(5)
w1.make_guess("apple")
w1.make_guess("orang")
w1.data()
w1.display()
input()
