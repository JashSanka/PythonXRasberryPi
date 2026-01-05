class Leg():
    __smelly=True

    def bend_knee(self):
        print("knee bent")
    
    @property
    def smelly(self):
        return self.__smelly
    
    @smelly.setter
    def smelly(self,smell):
        self.__smelly=smell

    def is_smelly(self):
        return self.__smelly

