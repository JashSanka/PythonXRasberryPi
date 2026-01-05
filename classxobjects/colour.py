class Colour():
    r=0
    g=0
    b=0
    def __init__(self,r=None,g=None,b=None):
        if r is None:
            self.r=0
        else:
            self.r=r
        if g is None:
            self.g=0
        else:
            self.g=g
        if b is None:
            self.b=0
        else:
            self.b=b
    def show(self):
        print("RGB values:",self.r,self.g,self.b)
    # Other means use another instance of this class
    def __add__(self, other):
        self.r+=other.r
        self.g+=other.g
        self.b+=other.b
        return Colour(self.r,self.g,self.b)


red=Colour(255,0,0)
red.show()

green=Colour(0,255,0)
green.show()

yellow=red+green
yellow.show()