class Employee:
    def __init__(self,name,designation,salary,):
        self.name = name
        self.designation = designation
        self.salary = salary
    def display(self):
        print(f"{self.name} : {self.name}")
        print(f"{self.designation} : {self.designation}")
        print(f"{self.salary} : {self.salary}")

class Wallet:
    def __init__(self,balance):
        self.__balance = balance
    def add_money(self,amount):
        if amount > 0:
            self.__balance += amount
    def show_balance(self):
        return self.__balance


class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
class Dog(Animal):
    def __init__(self,name):
      super().__init__(name)
    def bark(self):
        print(f"{self.name} says woof!")

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x} and {self.y}"
    def __add__(self,x,y):
        print(f"{x} + {y}")
class InvalidAgeError(Exception):
    pass
class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

        try:
           if age<0 or age >100:
                raise
        except InvalidAgeError:
            print("age must between 0 and 100")
        finally:
           print("age must be greater than 0 and smaller than 100")

