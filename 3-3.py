#count vowels and consonants in a sentence

vowel = 0
consonant = 0

statement=input("What u wanna say").replace(" ","")
for letter in statement.upper():
    if letter >= "A" and letter <= 'Z':
        if letter in "AEIOU":
            print("letter is vowel: {}".format(letter))
            vowel +=1

        else:
            print("letter is consonant: {}".format(letter))
            consonant += 1

print ("{} vowels and {} consonants".format(vowel, consonant))


#same as the above, but with functional programming
vowelList = [x for x in statement.upper() if x in ['A','E','I','O','U']]
print('%d vowels'%len(vowelList))
print("{}".format(vowelList))

for i in range(len(vowelList)):
    print(vowelList[i])

#accept x into the vowelList array if the uppercase version of the statement
#contains AEIOU

#% and the {} is the same, but different format

#extract from statement
#for x in y = for everything in y, if x = 'aeiou'
#place it into an array of vowelList
#len = the length of the list.
    #dot product is possible! use for (x,y) in zip (arrayA, arrayB) I think
