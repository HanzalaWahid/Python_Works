class Mathoperation:
    def add(self,a,b= 0):
        return a + b

math = Mathoperation()
result = (math.add(6,4))
print(result)

re = (math.add(6))
print(re)

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print ("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

dog = Dog()
cat = Cat()
dog.make_sound()
cat.make_sound()

from abc import  ABC , abstractmethod

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print ("Woof! this is dog sound")

class Cat(Animal):
    def make_sound(self):
        print ("Meow! this is cat sound")


dog = Dog()
cat = Cat()

cat.make_sound()
dog.make_sound()

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def show(self):
        print(f"Your name is {self.name} and your balance is {self.__balance}$")

    def deposit(self, amount_deposit):
        self.amount_deposit = amount_deposit
        self.__balance += amount_deposit
        print(f"You deposited an amount of {self.amount_deposit}$, and your current balance is {self.__balance}$")

    def withdraw(self, amount_withdraw):
        self.amount_withdraw = amount_withdraw
        if amount_withdraw > self.__balance:
            print("You do not have enough balance")
            self.__balance = 0
        else:
            self.__balance -= amount_withdraw
            print(f"You withdrew an amount of {self.amount_withdraw}$, and your balance is {self.__balance}$")

    def __display(self):
        print(f"Your current balance is {self.__balance}$")

e1 = Bank("Hanzala", 10000)
e1.show()
e1.deposit(6000)
e1.withdraw(1000)
e1._Bank__display()
