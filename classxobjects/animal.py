class Animal():
    # now data in eyes is protected
    __eyes=2

    def show(self):
        """Shows the number of eyes"""
        print(self.__eyes)

    def __secret(self):
        print("This is a secret")

    # Decorator
    @property
    def eyes(self):
        """Gets Number of eyes"""
        self.__secret()
        return self.__eyes
    
    @eyes.setter
    def eyes(self, eyes):
        """Sets the number of eyes"""
        if eyes <= 3:
            self.__eyes = eyes
        else:
            self.__eyes = 2

