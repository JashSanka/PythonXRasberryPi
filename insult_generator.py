from random import choice
adjectives=["wet","big","smelly","small minded"]
nouns=["turnip","dog","idiot","nose picker"]

def print_insult():
    print("You are a",end=" ")
    print(choice(adjectives),end=" ")
    print(choice(nouns))
def read_name():
    return input("Please type your name")
name=""
user_answer=""
name=read_name()
while user_answer != "no":
    if name=="jash":
        print("Jash is awesome no insults for him")
        break
    else:
        print_insult()
        user_answer=input("can you take anymore ?")

