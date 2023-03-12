from abc import ABC, abstractmethod

class FlyBirds(ABC):
    
    @abstractmethod
    def eat(self):
        raise 'Should Implement eat method'

    @abstractmethod
    def fly(self):
        raise 'Should Implement fly method'

    @abstractmethod
    def scream(self):
        raise 'Should Implement scream method'

class LandBirds(ABC):
    
    @abstractmethod
    def eat(self):
        raise 'Should Implement eat method'

    @abstractmethod
    def scream(self):
        raise 'Should Implement scream method'