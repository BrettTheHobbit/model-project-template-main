import random
class Word_random:
    
    file = ""
    
    def __init__(self, file):
        self.file = file
    
    #Randomly picks out a certain amount of words from the file
    def Word_randomed(self):
        f = open(self.file, "r")
        
        wordlist = []
        
        for x in f:
            wordlist.append(x.strip())
        #Prints words
        #Print(wordlist)
        #Prints wordlist
        #print(len(wordlist))
        
        listsize = 10
        
        while len(wordlist) > listsize:
            purgePos = random.randint(0, len(wordlist)-1)
            wordlist.pop(purgePos)
        
        #Prints wordlist and size of word list
        print(wordlist)
        print(len(wordlist))
        
        
        
#w1 = Word_random("words.txt")
#w1.Word_randomed()