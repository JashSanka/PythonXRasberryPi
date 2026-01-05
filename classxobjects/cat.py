from animal import Animal
from leg import Leg
# cat=Animal()
# dog=Animal()
# cat.eyes=1
# dog.eyes=4
# cat.show()
# dog.show()
# print(cat.eyes)

# cat.show()

# left_leg=Leg()

# left_leg.smelly=False
# print(left_leg.is_smelly())

class Cat(Animal):
    left_leg = Leg()
    right_leg= Leg()
    name=""

    def __init__(self,cat_name = None):
        if cat_name is None:

            self.name = "no name"
        else:
            self.name=cat_name

    def show(self):
        print("The cat's name is: ")
        print(self.name)
        super().show()
    pass

Salem= Cat("Salem")
Salem.eyes = 1
Salem.show()


    