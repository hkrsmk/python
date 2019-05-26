import requests

#open cmd as administrator,
#then type "python -m pip install -U pip requests (new)" to install pip

#Get response from API endpoint.
a = input("please enter")

#in a browser, input [REDACTED]
response = requests.get("redacted_link" + a)
data = response.json()

print(data['result'])

#data is a library:
el2cl = {}
el2cl['one']='yi'
el2cl['two']='er'

#type 'el2cl' in the python script thing then u can see the library
#or el2cl['two']
#another way to do it: (this overwrites the past array)
el2cl={'apple':430}

if 'orange' in el2cl:
    print("I have oranges")
else:
    print("No oranges")

if 'apple' in el2cl:
    print("I have apples")
    el2cl['apple']+=30
    print("I've added 30 apples to stock")

#el2cl.get('apple')
    #^gets the number of apples
    
#el2cl.pop('apple')
    #^throws away the apple item
