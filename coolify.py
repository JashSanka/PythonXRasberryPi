# We will make a function that we will use in other files as libraries
def coolify(name):
    return name + " is cool"

def _main_():
    myname = input("please type in your name: ")
    myname=coolify(myname)
    print(myname)