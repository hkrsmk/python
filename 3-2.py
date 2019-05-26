#loops syntax:
#for variable in range (start, stop, increment):
#   do something


#sum numbers from 0 to 99:
sum = 0
for j in range (100):
    sum += j
    print("+{:d}={:d}".format(j,sum))

print(sum)

for letter in 'python':
    print(letter)

for x in 'python':
    print(x)

word = 'python'
for letter in word[2:4]:
    print(letter)
    #rmb the string starts from 0! So, third and fourth characters are used
