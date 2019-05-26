def addWord(word, Dict):
    #should keep the Dict. addWord(word) works with just 1 variable
    #but you can't change your target dictionary
    
    """update the dictionary Dict with the word count"""
    if word in Dict:
        Dict[word] +=1
        #same as Dict[word]++ if it's C
    else:
        Dict[word] = 1

import string
def processLine(line, Dict):
    """take in a line and process in word in the addWord method"""
    wordList = line.split()
    for word in wordList:
        if word != '--':
            word = word.lower()
            word = word.strip()
            #remove special characters
            word = word.strip(string.punctuation)
            addWord(word, Dict)

def prettyPrint(Dict):
    valKeyList=[]
    for key, val in Dict.items():
        #two variables, because you have two things:
        #the word itself (key)
        #and how many times it appears (val)
        
        valKeyList.append((val,key))
        print(val)
        print(key)
        
    valKeyList.sort(reverse= True)
    #print in reverse order: key first, then val
    
    print("{:10s}{:10s}".format('Word', 'Count'))
    #prints a title
    
    for val, key in valKeyList:
        #take val, key instead of key, val because you appended
        #val FIRST then key next.
        
        print("{:10s}{:10d}".format(key,val))

wcDict = {}
processLine("The quick brown fox, jumps! over the lazy~ dog", wcDict)

print(wcDict)
prettyPrint(wcDict)

#notice that prettyPrint still recognises wcDict even though you
#didn't call anything.

#make variable private: __variable. two underscores _
