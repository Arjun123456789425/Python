# class Animal:
#     def move(self):
#              print('Animal walks')

# class Frog(Animal):
#        def move(self):
#               print('Frog jumps')   # Method overriding
# frog =Frog()     
# frog.move()                                  

# class Animal:
#     def sound(self):
#         print('Animal making sound')

# class Cat(Animal):
#     def sound(self):
#         print('Meow')

       
# class Dog(Animal):
#     def sound(self):
#         print('Woof')
    
# animal =Animal()
# animal.sound()
# cat=Cat()    
# cat.sound() 
# dog =Dog()
# dog.sound()                

from abc import ABC, abstractmethod
class Vehicle(ABC):
    def start():
        pass

class Vehicle():
    def start():
        print('Vehicle starting')    

class Car(Vehicle):
    def start():
        print('Car starts using keys')

class Electric_bike(Vehicle):
    def start():
        print('Bike starts bt push button')

electric =Electric_bike()
electric.start()
