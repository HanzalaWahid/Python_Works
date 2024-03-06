# Calculate area and perimeter of circle
class Circle:
    def CalculateArea(self,radius,pi=3.142):
        self.radius = radius
        self.pi = pi
        self.area = self.pi * self.radius ** 2

    def display(self):
        print(f"The area of circle is {self.area}")

    def CalculatePerimeter(self,radius,pi=3.142):
        self.radius = radius
        self.pi = pi
        self.perimeter = 2 * self.pi * self.radius

    def show (self):
        print(f"The perimeter of circle is {self.perimeter}")

c1 = Circle()
c1.CalculateArea(6)
c1.display()
c1.CalculatePerimeter(8)
c1.show()

# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import  datetime
class Person:
    def __init__(self,name,country,date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth,"%d-%m-%Y")

    def Age(self):
        current_date_time = datetime.now()
        age = current_date_time.year - self.date_of_birth.year - ((current_date_time.month, current_date_time.day) < (self.date_of_birth.month, self.date_of_birth.day))
        self.age = age

    def show (self):
        print(f"The name of person is {self.name} the country he live in {self.country} his date of birth is {self.date_of_birth} and age is {self.age}")

p1 = Person(name="Hanzala",country="Russia",date_of_birth= "19-4-2004")
p1.Age()
p1.show()

class myfunc:
    @classmethod
    def wrapper (cls,function):
        def function(self):
            print("something is happening before ")
            func()
            print("something is happening after")
        return function

    @wrapper
    def say_hello(self):
        print("Hello")

s1 = myfunc()
s1.say_hello()
