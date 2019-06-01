#classes are objects
#basically, in python, objects are used for the memory space
#compared to just functions, classes can let you 'tag' extra info
#so you create some memory space to store info more so than functions can

#however objects have their own problems

import random

class Coin:
    #simulates a coin that's flipped
    
    def __init__(self):
        self.sideup = "Heads"
        #initialise sideup data as 'heads'

    def toss(self):
        #toss is a METHOD in the object.
        
        if random.randint(0,1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    def get_sideup(self):
        return self.sideup
