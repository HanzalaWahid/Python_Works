# Question 1
print('''Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are''')

# Question 2
import sys

print("Python version")
print(sys.version)

# Question 3
import datetime

current = datetime.datetime.now()
print("The time or date is ", current)

# Question 4
radius = int(input("Enter the radius of circle: "))
area = 3.142 * float(radius * radius)
print("The area is ", area)

# Question 5
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Hello {last_name} {first_name}")

# Question 6
numbers = input("Enter a sequence of comma-separated numbers: ")
numbers_list = numbers.split(',')
numbers_tuple = tuple(numbers_list)
print("List:", numbers_list)
print("Tuple:", numbers_tuple)

# Question 8
color_list = ["Red", "Green", "White", "Black"]
print("First color:", color_list[0])
print("Last color:", color_list[-1])

# Question 10
n = int(input("Enter the number (n): "))
n1 = int(str(n) * 1)
n2 = int(str(n) * 2)
n3 = int(str(n) * 3)
sum_result = n1 + n2 + n3
print("Sum:", sum_result)


# Question 11
def check_prime(a):
    if a > 1:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True
    return False


number = int(input("Enter a number: "))

if check_prime(number):
    print("It is a prime number")
else:
    print("It is not a prime number")

# Question 12
i = 0
while i <= 50:
    print(i)
    i += 1
# Question 1
a = ['a', 'c', 'ac']
for item in a:
    print(item)
else:
    print("New item")

# Question 2
for i in range(1, 1000, 2):
    print("The all are odd number ", i)

# Question 3
for i in range(0, 43):
    print(i)
    if i == 4:
        print("Just looking like a wow ")
        break
    else:
        print("Name kiya hai bhophinader jogi ")
        continue

# Question 4
for j in range(6):
    print("Aayein")
    if j == 5:
        continue
        # print(j)

# Question 5
m = [2, 1, 21, 11]
for i in m:
    # print(i)
    pass

# Question 7
a = "Hanzala"
b = "Hanzala"
if a is b:
    print("N")
else:
    print("A")

# Question 8
a = [1, 2, 4, 8]
b = a
c = [1, 2, 4, 8]
print(c is a)
print(a is b)

# Question 9
a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
c = int(input("Enter any number: "))
d = int(input("Enter any number: "))

if a > b and a > c and a > d:
    print("a is greater ")
elif b > a and b > c and b > d:
    print("b is greater ")
elif c > a and c > b and c > d:
    print("c is greater ")
elif d > a and d > b and d > c:
    print("d is greater ")

# Question 10
marks1 = int(input("Enter marks of subject one: "))
marks2 = int(input("Enter marks of subject second: "))

total = 200
sum = marks1 + marks2
percentage = (sum / total) * 100

if percentage >= 40 and marks1 >= 33 and marks2 >= 33:
    print("You passed :)")
else:
    print("You are failed :(")

# Question 11
import re

s1 = "Michael Jackson is the best"

# Define the pattern to search for
pattern = r"Jackson"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")

# Question 1
import re

pattern = r"(\d)(\d)(\d)(\d)(\D)(\D)"
text = "1234AB"
match = re.search(pattern, text)
if match:
    print("It found: ", match.groups())
else:
    print("It not found")

# Question 2
import re

s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
pattern = r"King of Pop"
replacement = "legend"
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)
print(new_string)

# Question 3
l1 = ["Ahmed", "Sania", "Sumaiya", "Shaheer", "Mashood", "Sohail", "Hanzala", "Hashir"]
for name in l1:
    if name.startswith("S"):
        print(f"Hello {name}")
    else:
        print("Hello Everyone")

# Question 4
n = 5
factorial = 1
for i in range(n):
    factorial *= (i + 1)
print(factorial)


# Question 5
def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n - 1)


f = factorial_recursive(4)
print(f)


# Question 6
def greatest_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num2 and num3 > num2:
        return num3
    else:
        return None


gr = greatest_number(10, 12, 15)
print("The greatest number is", gr)


# Question 7
def maximum(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            return n1
        else:
            return n3
    if n2 > n3:
        return n2
    else:
        return n3


n = maximum(26, 42, 53)
print("The greatest number is ", n)


# Question 8
def converter(C):
    F = (C * (9 / 5)) + 32
    return F


celsius = int(input("Enter The temperature in Celsius: "))
TC = converter(celsius)
print(f"The temperature in Celsius is {celsius} and in Fahrenheit it is {TC}")

# Question 1
t1 = ("hi", 3, 232.2)
t2 = t1 + ("rock", 56, 3.42)
print(t2[3][0:3])
print(len(t2))

# Question 2
t = (3, 42, (2, 49), (22.2, "dark", "a"), ("a"))
print(t[3][1][2])

# Question 3
print("Hello", end=" ")
print("Hanzala", end=" ")
print("What do you do?", end=" ")
print("Let's escape the matrix", end=" ")


# Question 4
def natural_number(n):
    return sum(range(1, n + 1))


n = int(input("Enter your number: "))
total = natural_number(n)
print(total)


# Question 5
def natural_number_recursive(n):
    if n == 1:
        return 1
    else:
        return n + natural_number_recursive(n - 1)


n = int(input("Enter your number: "))
total_recursive = natural_number_recursive(n)
print(total_recursive)


# Question 6
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter any number: "))
total_fibonacci = fibonacci(n)
print(total_fibonacci)

# Question 7
n = "*"
for i in range(3, 0, -1):
    print(n * i)

# Question 8
n = 3
for i in range(n):
    print("*" * (n - i))


# Question 9
def converter(INCH):
    Cm = INCH * 2.54
    return Cm


INCH = int(input("Enter inches: "))
Cm = converter(INCH)
print(f"The length in inches is {INCH} and in Centimeters is {Cm}")


# Question 10 (Sample code, as it is incomplete)
# import requests
# from bs4 import BeautifulSoup

# Question 11
def remove_strip(string, word):
    new_str = string.replace(word, "")
    return new_str.strip()


text = "Hanzala Kaha Ho"
result = remove_strip(text, "Ho")
print(result)


# Question 12
def tables(num, i):
    result = num * i
    return result


for i in range(1, 11):
    print(tables(3, i))


# Question 1
class myclass:
    x = 5


p1 = myclass()
print(p1.x)


# Question 2
class myclass:
    x = 5


print(myclass)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Create an instance 'p1' of the 'Person' class with name "Hanzala" and age 19
p1 = Person("Hanzala", 19)

# Access and print the 'name' attribute of the instance 'p1'
print(p1.name)

# Access and print the 'age' attribute of the instance 'p1'
print(p1.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func1(self):
        print(f"Your name is {self.name} and age is {self.age}")


# Create an instance 'p1' of the 'Person' class with name "Hanzala" and age 21
p1 = Person("Hanzala", 21)

# Call the 'func1' method on the instance 'p1' to print information about the person
p1.func1()


# Define a class named Employee
class Employee:
    # Class variables shared by all instances
    company = "Microsoft"
    salary = 100000


# Create instances of the Employee class
hanzala = Employee()
harry = Employee()

# Access and print the 'company' attribute of the 'harry' instance
s = harry.company
print(s)

# Update the 'company' class variable for all instances to "IBM"
Employee.company = "IBM"
d = Employee.company
print(d)

# Update the 'salary' attribute for individual instances
harry.salary = 3000
hanzala.salary = 3220

# Print the salaries of 'harry' and 'hanzala'
print(f"Harry salary is {harry.salary}")
print(f"Hanzala salary is {hanzala.salary}")


# Redefine the Employee class with modified methods
class Employee:
    # Class variable 'company' with a default value "MICROSOFT"
    company = "MICROSOFT"

    # Method to print a salary-related message
    def getsalary(self):
        print(f"Your salary is deposited in your account {self.salary}.")


# Create an instance of the Employee class named 'hanzala'
hanzala = Employee()

# Set the 'salary' attribute for the 'hanzala' instance
hanzala.salary = 12000000

# Call the 'getsalary' method on the 'hanzala' instance
hanzala.getsalary()

# The above line is equivalent to the following explicit call
Employee.getsalary(hanzala)


class Person:
    type = "humanbeing"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getinfo(self):
        print(f"The name of person is {self.name} and age is {self.age}")


h1 = Person("Hanzala", 21)
h1.getinfo()


# #Define a class named Person
class Person:
    # Class variable 'type' with a default value "humanbeing"
    type = "humanbeing"

    # Constructor method to initialize instance attributes 'name' and 'age'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Static method to print information about a person, taking an instance as a parameter
    @staticmethod
    def getinfo(instance):
        print(f"The name of the person is {instance.name} and age is {instance.age}")


# Create an instance of the Person class named 'h1'
h1 = Person("Hanzala", 21)

# Call the 'getinfo' static method on the class, passing the 'h1' instance as a parameter
Person.getinfo(h1)


# Redefine the Person class with a modified static method
class Person:
    # Class variable 'type' with a default value "humanbeing"
    type = "humanbeing"

    # Constructor method to initialize instance attributes 'name' and 'age'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Static method to print information about the type of person, without taking an instance parameter
    @staticmethod
    def getinfo():
        print(f"The type of person is {Person.type}")


# Create an instance of the modified Person class named 'h1'
h1 = Person("Hanzala", 21)

# Call the modified 'getinfo' static method on the class itself (not on an instance)
Person.getinfo()


class Per:
    pass

    @staticmethod
    def printdata():
        print("This is printdata form ")

    @staticmethod
    def how():
        print("How is how :) wow ")


Per.printdata()
Per.how()


class Employee:
    company = "Youtube"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def showdata(self):
        print(
            f"The name of person is {self.name} and the age of person is {self.age} and he works for {self.company} and his salary is {self.salary}")


e1 = Employee("Hanzala", 19, 100000)
e2 = Employee("Mashood", 20, 100000)
e3 = Employee("Hashir", 21, 100000)

e1.showdata()
e2.showdata()
e3.showdata()

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * radius ** 2
        self.perimeter = 2 * math.pi * radius

    def show(self):
        print(f"the area of circle of radius {self.radius} is {self.area} and the perimeter is {self.perimeter}")


c1 = Circle(21)
c2 = Circle(10)
c3 = Circle(14)
c1.show()
c2.show()
c3.show()


class Programmer:
    company = "Microsoft"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def show(self):
        print(
            f"The Person is working in {self.company} the name of person is {self.name} the age of person {self.age} and the salray of person {self.salary}  ")


e1 = Programmer(name="Hanzala", age=20, salary=10000)
e2 = Programmer(name="Hafsa", age=17, salary=2000000000000)
e3 = Programmer(name="Hashir", age=14, salary=10000000000000)

e1.show()
e2.show()
e3.show()


class Calculator:
    def __init__(self, num):
        self.square = num ** 2
        self.cube = num ** 3
        self.squareroot = num ** 0.5

    def show(self):
        print(
            f"Calculate the square is {self.square} the cube is {self.cube} and the squareroot is {self.squareroot}  ")


n1 = Calculator(3)
n2 = Calculator(5)
n1.show()
n2.show()

pressure = force / area
volume_cylinder = 3.142 * r ** 2 * h
area = l * b


# #Create a class along with membership functions calculate pressure and volume.
# #Create class for two different shapes of pipes and measure the pressure and volume of crosection
class Parameter:
    pi = 3.142

    def Pressure(self):
        pass

    def volume(self):
        pass


class CylinderPipe(Parameter):

    def Pressure(self, force):
        self.force = force

    def cross_section_area(self, radius, height):
        self.area = 2 * self.pi * radius ** 2 + 2 * self.pi * radius * height
        self.height = height

    def show(self):
        print(f"The Pressure of cylinder is {self.area}")


ob1 = CylinderPipe()
ob1.cross_section_area(5, 10)
ob1.show()


class SquarePipe(Parameter):

    def Pressure(self, force):
        self.force = force

    def cross_section_area(self, side_length):
        self.area = 4 * self.pi * side_length ** 2
        self.side_length = side_length

    def show(self):
        print(f"The Pressure of square pipe is {self.area}")


ob2 = SquarePipe()
ob2.cross_section_area(8)
ob2.show()


class Calculator:
    def __init__(self, num):
        self.square = num ** 2
        self.cube = num ** 3
        self.squareroot = num ** 0.5

    @staticmethod
    def greet():
        print("Hello User")

    def show(self):
        print(
            f"Calculate the square is {self.square} the cube is {self.cube} and the squareroot is {self.squareroot}  ")


n1 = Calculator(3)
n2 = Calculator(5)
Calculator.greet()
n1.show()
n2.show()


class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.__seats = seats

    def show(self):
        print(f"The name of train is {self.name}\n"
              f"The fare of one person is {self.fare}\nAnd total numbers of seat is {self.__seats} ")

    def bookTicket(self):
        if self.__seats > 0:
            print(f"You seat is booked and seat number is {self.__seats}")
            self.__seats -= 1
        else:
            print("The Train is full! ")

    def inf(self):
        print(f"{self.__seats}")


ob = Train("Karachi express", 250, 400)
ob.show()
ob.inf()
ob.bookTicket()


class Employee:
    company = "Google"
    name = "Mashood"
    language = "Java Script"

    def __init__(self, name, company, language):
        self.name = name
        self.company = company
        self.language = language

    def showdetails(self):
        print(
            f"The person is working in {self.company}\nThe name is {self.name}\nThe language he works is {self.language} ")


class Programmer(Employee):
    def __init__(self, name, company, language):
        self.name = name
        self.company = company
        self.language = language

    def showdetails(self):
        print(f"The person is a Programmer and working in {self.company}\nThe name is {self.name} and "
              f"The Person works on language is {self.language}")


print(f"The person is a Programmer and working in {Employee.company}\nThe name is {Employee.name} and "
      f"The Person works on language is {Employee.language}")

p1 = Programmer("Hanzala", "Facebook", "Python")
p1.showdetails()
e2 = Employee("Talha", "Youtube", "C++")
e2.showdetails()

print("*********************")


class Employee:
    company = "Google"
    name = "Mashood"
    language = "Java Script"

    def __init__(self, name, company, language):
        self.name = name  # Instance attribute
        self.company = company  # Instance attribute
        self.language = language  # Instance attribute

    def showdetails(self):
        print(
            f"The person is working in {self.company}\nThe name is {self.name}\nThe language he works is {self.language}")


class Programmer(Employee):
    def __init__(self, name, company, language):
        super().__init__(name, company, language)  # Call the superclass's __init__ method

    def showdetails(self):
        print(f"The person is a Programmer and working in {self.company}\nThe name is {self.name} and "
              f"The person works with the language {self.language}")


# Creating instances
p1 = Programmer("Hanzala", "Facebook", "Python")
p1.showdetails()

e2 = Employee("Talha", "Youtube", "C++")
e2.showdetails()


class Person:
    def __init__(self, speak):
        self.speak = speak

    def show(self):
        print(f"The Person speak {self.speak}")


class Animal(Person):
    def __init__(self, speak, walk):
        super().__init__(speak)
        self.walk = walk


a1 = Animal("Waow", "Yes")
a1.show()


class Employee:
    company = "Youtube"
    com_code = 3210


class Freelancer:
    company = "Fiver"
    level = 3

    def upgradelevel(self):
        self.level += 1


class Programmer(Employee, Freelancer):
    name = "Hanzala"

    def show(self):
        print(f"The name of person is {self.name}.\nHe works in {self.company} his company code is {self.com_code}"
              f".\nHe is also a good freelancer and his sales level is {self.level}")


p = Programmer()
p.show()


class Employee:
    company = "FORD"
    name = "Hanzala"
    salary = 21

    def currentSalary(self, new_salary):
        self.salary = new_salary
        print(f"New_Salary (instance method): {self.salary}")

    @classmethod
    def changeSalary(cls, new_salary):
        cls.salary = new_salary
        print(f"New_Salary (class method): {cls.salary}")


e1 = Employee()
e1.changeSalary(30)
e1.currentSalary(45)
Employee.changeSalary(400)
print(e1.salary)


class Employee:
    company = "NIKE"
    salary = 1000
    salary_bonus = 200

    @property
    def totalSalary(self):
        return self.salary + self.salary_bonus


e1 = Employee()
print(f"The total salary is {e1.totalSalary}")


class Employee:
    company = "Youtube"
    salary = 400
    salarybonus = 600

    @property
    def totalsalary(self):
        return self.salary + self.salarybonus


e = Employee()
print(e.totalsalary)


class Number:
    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, num2):
        print("Add")
        return self.num1 + num2.num1


n1 = Number(5)
n2 = Number(4)
sum = n1 + n2
print(sum)


class MyClass:
    def __init__(self):
        # Private attribute
        self._my_value = 0

    # Getter method
    @property
    def my_value(self):
        return self._my_value

    # Setter method
    @my_value.setter
    def my_value(self, new_value):
        # You can add validation or additional logic here
        self._my_value = new_value


# Example usage
obj = MyClass()

# Using the getter
current_value = obj.my_value
print(f"Current value: {current_value}")

#  #Using the setter
obj.my_value = 42
print(f"Updated value: {obj.my_value}")


class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __str__(self):
        return (f" {self.real} + {self.img}i ")


ob = ComplexNumber(4, 2)
ob1 = ComplexNumber(3, 1)

result = ob + ob1
print(result)


class Car:
    def __init__(self, color):
        self.__color = color

    def displaycolor(self):
        print(self.__color)


c1 = Car("blue")
c1.displaycolor()
print(c1._Car__color)


class Emp:
    def __init__(self, salary):
        self._salary = salary

    def show(self):
        print(self._salary)


e1 = Emp(3220)
e1.show()
print(e1._salary)


class C2DVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = self.x ** 2 + self.y ** 2

    def get_magnitude(self):
        print(f"The magnitude of a 2d Vector is {self.magnitude}")

    def __add__(self, other):
        if isinstance(other, C2DVector):
            return C2DVector(self.x + other.x, self.y + other.y)
        else:
            raise ValueError("Unsupported operand for type + ")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return C2DVector(self.x * other, self.y * other)
        elif isinstance(other, C2DVector):
            return C2DVector(self.x * other.x, self.y * other.y)
        else:
            raise ValueError("Unsupported operand for type * ")


cd = C2DVector(5, 4)
cd.get_magnitude()


class C3DVector(C2DVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        self.magnitude_3d = self.x ** 2 + self.y ** 2 + self.z ** 2

    def showmagnitude(self):
        print(f"The magnitude of 3d vector is {self.magnitude_3d}")


c1 = C3DVector(4, 2, 2)
c1.showmagnitude()


class C2DVector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap} "


class C3DVector(C2DVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


v2d = C2DVector(1, 5)
v3d = C3DVector(2, 5, 6)
print(v2d)
print(v3d)


class Animal:
    pass


class Pet(Animal):
    pass


class Dog(Pet):
    def __init__(self, bark):
        self.bark = bark

    def show(self):
        print(f"The Dog bark is {self.bark}")


d1 = Dog("woof,ruff,wow;yap")
d1.show()


class Employee:
    salary = 1000
    increment = 2.0

    @property
    def salary_increment(self):
        return self.salary * self.increment

    @salary_increment.setter
    def salary_increment(self, new_increment):
        if new_increment < 0:
            print(" Increment should be a positive value   ")

        else:
            self.increment = new_increment
            print("You got increment")

    def show(self):
        print(f"Your salary is {self.salary_increment}")


s1 = Employee()
s1.show()


class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        new_real = self.real * other.real - self.imaginary * other.imaginary
        new_imaginary = self.real * other.imaginary + self.imaginary * other.real
        return Complex(new_real, new_imaginary)

    def __str__(self):
        return f"The result is {self.real} + {self.imaginary}i"


c1 = Complex(5, 7)
c2 = Complex(4, 6)
result_add = c1 + c2
print(result_add)
result_mul = c1 * c2
print(result_mul)


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.vec = [x, y, z]

    def __str__(self):
        return f"The vector is {self.vec[0]}i {self.vec[1]}j {self.vec[2]}k"


vec = Vector(2, 5, 6)
print(vec)
