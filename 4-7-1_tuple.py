def Spell_0_10(n):
    refTuple = ("zero","one","two","three","four","five",
                "six","seven","eight","nine","ten")
    return refTuple[n]

print(1, " is spelt as ", Spell_0_10(1))
for i in range(11):
    print("{} is spelt as {}".format(i,Spell_0_10(i)))

for i in range (-9,0,1):
    print("{} is spelt as {}".format(i, Spell_0_10(i)))
