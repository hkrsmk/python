import datetime

def tellmeAge(yearBorn):
    #work out age from year of birth
    return datetime.date.today().year - yearBorn

user_input_year = int(input("What year did it start?"))

print("It's {} years old".format(tellmeAge(user_input_year)))
