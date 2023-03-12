from interface import FlyBirds, LandBirds

class Canary(FlyBirds):
    def eat(self):
        print('I am eating!')

    def fly(self):
        print('I am flying!')

    def scream(self):
        print('I am screaming!')

class Penguin(LandBirds):
    def eat(self):
        print('I am eating!')
        self.__lay_eggs()

    def scream(self):
        print('I am screaming!')

    def __lay_eggs(self):
        print('Now Im going to lay eggs!')