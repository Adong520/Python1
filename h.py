import random
import sys
import os

class Animal:
    __name = 0
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_sound(self):
        return self.__sound


    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says abc {}".format(self.__name,self.__height,self.__weight,self.__sound)

cat = Animal('Whiskers',33,10,'Meow')

print(cat.toString())


class Dog(Animal):
    __owner = ""

    def __init__(self,name, height, weight, sound, owner):
        super(Dog,self).__init__(name, height, weight, sound)
        self.__owner = owner

    def set_owner(self, owner):
        self.__owner = owner


    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
         return "{} is {} cm tall and {} kilograms and says and {} owner is {}".format(self._Animal__name,
                                                                                       self._Animal__height,
                                                                                       self._Animal__weight,
                                                                                       self._Animal__sound,
                                                                                       self.__owner)
    def multiple_sounds(self,how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


spot = Dog("Spot",50,30,"woo","Dong")

print(spot.toString())

spot.multiple_sounds()

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

#test_animals.get_type(cat)

test_animals.get_type(spot)


