# # # # question 1 print fuction
# # # print('''Twinkle, twinkle, little star,
# # # 	How I wonder what you are!
# # # 		Up above the world so high,
# # # 		Like a diamond in the sky.
# # # Twinkle, twinkle, little star,
# # # 	How I wonder what you are''')
# # # # question 2 Write a Python program to find out what version of Python you are using.
# # #
# # # import sys # sys to import specific details of version
# # #
# # # print("Python verssion")
# # #
# # # print(sys.version)
# # #
# # # # question 3 Write a Python program to display the current date and time.
# # #
# # # import datetime
# # # import time
# # #
# # # current = datetime.datetime.now()
# # # print("The time or date is ",current)
# # #
# # # # question 4 Write a Python program that calculates the area of a circle based on the radius entered by the user.
# # #
# # # radius = int(input("Enter the radius of circle: "))
# # # area = 3.142 * float(radius*radius)
# # # print("The area is ", area)
# # #
# # # #Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# # #
# # # name = input("Enter your fisrt name: ")
# # #
# # # name = input("Enter your last name: ")
# # #
# # # print(f"Hello {name} + {name} ")
# # #
# # # # 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# # # list = [3, 5, 7, 23]
# # # tuple =(3, 5, 7, 23)
# # # print(list,tuple)
# # #
# # # # 8. Write a Python program to display the first and last colors from the following list.
# # # color_list = ["Red","Green","White" ,"Black"]
# # # print(color_list[0])
# # # print(color_list[-1])
# #
# # # for i in range(5):
# # #     for j in range(4):
# # #         if j == i:
# # #             print('*')
# # #             break
# # #         print(i,j)
# #
# # # 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# #
# # # n = int(input("Enter the number(n): "))
# # # n1 = int(str(n)*1)
# # # n2 = int(str(n)*2)
# # # n3 = int(str(n)*3)
# # # sum = n1 + n2 + n3
# # # print(sum)
# #
# # # def check_prime(a):
# # #     if a > 1:
# # #         for i in range(2,0):
# # #             if a % i == 0:
# # #                 return False
# # #         return True
# # #     return False
# # #
# # # a = int(input("Enter number: "))
# # #
# # # if check_prime(a):
# # #     print("It is a prime number")
# # # else:
# # #     print("It is not a prime number")
# #
# # # i = 0
# # # while 50 >= i:
# # #     print(i)
# # #     i +=1
# #
# # # a = ['a','c','ac']
# # # for item in a:
# # #     print(item)
# # # else:
# # #     print("New item")
# #
# # # for i in range(1,1000,2):
# # #     print("The all are odd number ",i)
# # # #
# # # for i in range (0,43):
# # #     print(i)
# # #     if i == 4:
# # #         print("Just looking like a wow ")
# # #         break
# # #     else:
# # #         print("Name kiya hai bhophinader jogi ")
# # #         continue
# #
# # # for j in range(6):
# # #     print("Aayein")
# # #     if j == 5:
# # #         continue
# # #         print(j)
# #
# #
# # # m = [2,1,21,11]
# # # for i in m:
# # #     # print(i)
# # #     pass
# #
# # # p1 = Myclass()
# # # print(p1.x)
# #
# #
# # a = "Hanzala"
# # b = "Hanzala"
# # if a is b:
# #     print("N")
# # else:
# #     print("A")
# #
# # a = [1,2,4,8]
# # b = a
# # c = [1,2,4,8]
# # print(c is a)
# # print(a is b)
# #
# #
# # a = int(input("Enter any number: "))
# # b = int(input("Enter any number: "))
# # c = int(input("Enter any number: "))
# # d = int(input("Enter any number: "))
# #
# # if a > b and  a > c and a > d:
# #     print("a is greater ")
# # elif b > a and b > c and b > d:
# #     print("b is greater ")
# # elif c > a and c > b and c > d:
# #     print("c is greater ")
# # elif d > a and d > b and d > c:
# #     print("d is greater ")
# #
# #
# # marks1 = int(input("Enter marks of subject one: "))
# # marks2 = int(input("Enter marks of subject second: "))
# #
# #
# # total = 200
# # sum = marks1 + marks2
# # percentage = (sum / total) * 100
# #
# # if percentage >= 40  and marks1 >= 33 and marks2 >= 33:
# #     print("You passed :)")
# # else:
# #     print("You are failed :(")
# # # print(percentage)
# #
# # import  re
# #
# # s1 = "Michael Jackson is the best"
# #
# # # Define the pattern to search for
# # pattern = r"Jackson"
# #
# # # Use the search() function to search for the pattern in the string
# # result = re.search(pattern, s1)
# #
# # # Check if a match was found
# # if result:
# #     print("Match found!")
# # else:
# #     print("Match not found.")
# #
# # import re
# # pattern = r"(\d)(\d)(\d)(\d)(\D)(\D)"
# # text = "1234AB"
# # match = re.search(pattern,text)
# # if match:
# #     print("It found: ",match.groups())
# # else:
# #     print("It not found")
# #
# # import re
# #
# # s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
# # # Define the regular expression pattern to search for
# # pattern = r"King of Pop"
# #
# # # Define the replacement string
# # replacement = "legend"
# #
# # # Use the sub function to replace the pattern with the replacement string
# # new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)
# # # The new_string contains the original string with the pattern replaced by the replacement string
# # print(new_string)
# # l1 = ["Ahmed","Sania","Sumaiya","Shaheer","Mashood","Sohail","Hanzala","Hashir"]
# # for name in l1:
# #     if name.startswith("S"):
# #
# #         print(f"Hello {name}")
# #     else:
# #         print("Hello Everyone")#
#
# # n = 5
# # factorial =1
# # for i in range(n):
# #     factorial  *= (i+1)
# # print(factorial)
#
# # def factorial_recursive (n):
# #     if n == 1 or n == 0:
# #         return 1
# #     return n * factorial_recursive(n-1)
# #
# # f = factorial_recursive(4)
# # print(f)
#
# # def greatest_number(num1,num2,num3):
# #     if num1 > num2 and num1 > num3:
# #         print("The num1 is greater ")
# #         return num1
# #     elif num2 > num1 and num2 > num3:
# #         print("The num2 is greater ")
# #         return num2
# #     elif num3 > num2 and num3 > num2:
# #         print("The num3 is greater ")
# #         return num3
# #     else:
# #         print("None of this is great")
# #
# # gr = greatest_number(10,12,15)
# # print("The greatest  number is",gr)
#
# # def maximum (n1,n2,n3):
# #     if n1 > n2:
# #         if n1 > n3:
# #             return n1
# #         else:
# #             return n3
# #     if n2 > n3:
# #         return n2
# #     else:
# #         return n3
#
# # n = maximum(26,42,53)
# # print("The greatest number is ",n)
#
# # def conveter(C):
# #     F = (C * (9/5)) + 32
# #     return F
#
# # celsuis = int(input("Enter The temperature in Celsuis: "))
# # TC = conveter(celsuis)
# # print(f"The temperature in celsius is {celsuis} and in Fahrenheit it is {TC}")
#
#
# # t1 = ("hi",3,232.2)
# # t2 = t1 + ("rock",56,3.42)
# # print(t2[3][0:3])
# # print(len(t2))
#
# # t = (3,42,(2,49),(22.2,"dark","a"),("a"))
# # print(t[3][1][2])
#
# # print("Hello" ,end=" ")
# # print("Hanzala",end=" ")
# # print("What do you do ?",end=" ")
# # print("Let's escape the matrix",end=" ")
#
# # def natural_number (n):
# #     return sum (range(1,n+1))
#
# # n = int(input("Enter your number: "))
# # total = natural_number(n)
# # print(total)
# #
# # def natural_number (n):
# #     if n == 1:
# #         return 1
# #     else:
# #         return  n + natural_number(n-1)
# #
# # n = int(input("Enter your number: "))
# # total_recursive = natural_number(n)
# # print(total_recursive)
# #
# # def fibonacci (n):
# #     if n <= 1:
# #         return n
# #     else:
# #         return fibonacci(n-1)+fibonacci(n-2)
#
# # n = int(input("Enter any number: "))
# # total = fibonacci(n)
# # print(total)
#
# # n = "*"
# # for i in range(3,0,-1):
# #      print(n*i)
#
# # n =3
# # for i in range (n):
# #     print("*" * (n-i))
#
# # def conveter(INCH):
# #     Cm = INCH * 2.54
# #     return Cm
#
# # INCH = int(input("Enter  inches: "))
# # Cm = conveter(INCH)
# # print(f"The length in inch is  {INCH}  and in Centimeter is {Cm}")
# # import requests
# # from bs4 import BeautifulSoup
#
# # def remove_strip(string,word):
# #     new_str = string.replace(word,"")
# #     return new_str.strip()
#
# # t = "Hanzala Kaha Ho"
# # n = remove_strip(t,"Ho")
# # print(n)
#
# # def tables (num,i):
# #     result = num * i
# #     return result
# #
# # for i in range(1,11):
# #     print(tables(3,i))
#
# # First class definition for 'myclass' with attribute 'x' set to 5
# # class myclass:
# #     x = 5
#
# # Creating an instance 'p1' of the class 'myclass'
# # p1 = myclass()
# # Accessing and printing the attribute 'x' of the instance 'p1'
# # print(p1.x)
#
# # The following code defines a new class with the same name 'myclass'
# # This will override the previous definition of 'myclass'
# #
# # # Second class definition for 'myclass' with attribute 'x' set to 5
# # class myclass:
# #     x = 5
# #
# # # Printing the information about the current definition of 'myclass'
# # print(myclass)
# #
# # Define a class named 'Person'
# # class Person:
# #     # Constructor method '__init__' initializes instances of the class with provided values for 'name' and 'age'
# #     def __init__(self, name, age):
# #         # Instance variable 'name' to store the name of the person
# #         self.name = name
# #         # Instance variable 'age' to store the age of the person
# #         self.age = age
#
# # # Create an instance 'p1' of the 'Person' class with name "Hanzala" and age 19
# # p1 = Person("Hanzala", 19)
# #
# # # Access and print the 'name' attribute of the instance 'p1'
# # print(p1.name)
# #
# # # Access and print the 'age' attribute of the instance 'p1'
# # print(p1.age)
#
# # Define a class named 'Person'
# # class Person:
# #    # Constructor method '__init__' initializes instances of the class with provided values for 'name' and 'age'
# #     def __init__(self, name, age):
# #         # Instance variable 'name' to store the name of the person
# #         self.name = name
# #         # Instance variable 'age' to store the age of the person
# #         self.age = age
#
# #     #Method 'func1' to print information about the person using instance variables
# #     def func1(self):
# #       # Print a formatted string with the person's name and age
# #         print(f"Your name is {self.name} and age is {self.age}")
#
# # # Create an instance 'p1' of the 'Person' class with name "Hanzala" and age 21
# # p1 = Person("Hanzala", 21)
#
# #  Call the 'func1' method on the instance 'p1' to print information about the person
# # p1.func1()
#
# # # Define a class named Employee
# # class Employee:
# #     # Class variables shared by all instances
# #     company = "Microsoft"
# #     salary = 100000
#
# # # Create instances of the Employee class
# # hanzala = Employee()
# # harry = Employee()
#
# # # Access and print the 'company' attribute of the 'harry' instance
# # s = harry.company
# # print(s)
# #
# # # Update the 'company' class variable for all instances to "IBM"
# # d = Employee.company = "IBM"
# # print(d)
#
# # # Update the 'salary' attribute for individual instances
# # harry.salary = 3000
# # hanzala.salary = 3220
#
# # Print the salaries of 'harry' and 'hanzala'
# # print(f"Harry salary is {harry.salary}")
# # print(f"Hanzala salary is {hanzala.salary}")
#
# Define a class named Employee
# class Employee:
#     # Class variable 'company' with a default value "MICROSOFT"
#     company = "MICROSOFT"
#
#     # Method to print a salary-related message
#     def getsalary(self):
#         print(f"Your salary is deposited in your account {self.salary}.")
#
# # Create an instance of the Employee class named 'hanzala'
# hanzala = Employee()
#
# # Set the 'salary' attribute for the 'hanzala' instance
# hanzala.salary = 12000000
#
# # Call the 'getsalary' method on the 'hanzala' instance
# hanzala.getsalary()
#
# # The above line is equivalent to the following explicit call
# Employee.getsalary(hanzala)


# class Person:
#     type = "humanbeing"
#
#     def __init__(self,name ,age):
#         self.name = name
#         self.age = age
#
#     def getinfo(self):
#         print(f"The name of person is {self.name} and age is {self.age}")
#
# h1 = Person("Hanzala",21)
# h1.getinfo()

# Define a class named Person
# class Person:
#     # Class variable 'type' with a default value "humanbeing"
#     type = "humanbeing"
#
#     # Constructor method to initialize instance attributes 'name' and 'age'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # Static method to print information about a person, taking an instance as a parameter
#     @staticmethod
#     def getinfo(instance):
#         print(f"The name of the person is {instance.name} and age is {instance.age}")
#
# # Create an instance of the Person class named 'h1'
# h1 = Person("Hanzala", 21)
#
# # Call the 'getinfo' static method on the class, passing the 'h1' instance as a parameter
# Person.getinfo(h1)
#
# # Redefine the Person class with a modified static method
# class Person:
#     # Class variable 'type' with a default value "humanbeing"
#     type = "humanbeing"
#
#     # Constructor method to initialize instance attributes 'name' and 'age'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # Static method to print information about the type of person, without taking an instance parameter
#     @staticmethod
#     def getinfo():
#         print(f"The type of person is {Person.type}")
#
# # Create an instance of the modified Person class named 'h1'
# h1 = Person("Hanzala", 21)
#
# # Call the modified 'getinfo' static method on the class itself (not on an instance)
# Person.getinfo()
