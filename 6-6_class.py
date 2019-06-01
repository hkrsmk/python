class AngryBird:
    """ The Angry Bird Game actors."""
    #build an angry bird game.
    #note that your file should not be the same name as your class
    #or else it will be confusing.

    myName = input("What name?")

    """def __init__(self):
        self.myName = "John"
        #__ is two underscores.
    """
    #note that the green quoted will clash with the below __init__. So
    #if you still want John, need to put it into the init.
    
    def __init__(self, name="Jo"):
        self.myName = name
        #this is what prints if you leave the input part blank.
    
    def talk(self):
        #self must always be the first parameter for classes in python.
        #so you need to call self before myName.
        print("Hello I'm ", self.myName)

#"""
    def __str__(self):
        return self.myName
#"""

#================Main Program================================
b1 = AngryBird("Prata")
b1.talk()
print(b1)

#print(b1) the memory of the object if the __str__ codeblock is not used

b2 = AngryBird("Peter")
b2.talk()
print(b2)

b3 = AngryBird()
b3.talk()
