from abc import ABC, abstractmethod

class SomeAbstractclass(ABC):
    @abstractmethod
    def someabstractmethod(self):
        pass

class Employee(ABC):
    @abstractmethod 
    def donate(self):
        pass    

class Donation(Employee):
    def donate(self):
        a = input("How much would you like to donate: ")


john = Donation()
j = john.donate()

peter = Donation()
p = peter.donate()
