# import time
#
# import pyautogui as auto
#
# time.sleep(5)
#
# for i in range(0,100):
#     auto.typeWrite
#
# games = ["cricket","golf"]
# print(games)
# games.append("Hockey")
# print(games)
# games.insert(1,"Football")
# print(games)
# games.remove("golf")
# print(games)
# games.pop(1)
# print(games)
#
# values = (3,4,5,6,7,9,15)
# values.index(7,4)
# print(values)
# values.count(3)
# print(values)
# values.min(7)
# print(values)
#
# values = (3, 4, 5, 6, 7, 9, 15)
#
# # Find the index of 7, starting the search from index 4
# try:
#     index_7 = values.index(7, 4)
#     print(f"Index of 7: {index_7}")
# except ValueError:
#     print("7 is not in the tuple")
#
# # Count the number of occurrences of 3
# count_3 = values.count(3)
# print(f"Count of 3: {count_3}")
#
# # Find the minimum value in the tuple
# min_value = min(values)
# print(f"Minimum value in the tuple: {min_value}")

# s = set()
# s.add(20)
# s.add("20")
# s.add(20.0)
# print(len(s))

# dict = {}
# a  = input("Enter your favourite language Hanzala:\n ")
# b  = input("Enter your favourite language Ahmed:\n ")
# c  = input("Enter your favourite language Talha:\n ")
# d  = input("Enter your favourite language Mashood:\n ")
#
# dict["Hanzala"] = a
# dict["Ahmed"] = b
# dict["Talha"] = c
# dict["Mashood"] = d
# print( dict)
#
# def square (x):
#     return x**2
# print(square(10))
# import pandas as pd
#
#
# # Read the Excel file into a DataFrame
# df = pd.read_excel(r"C:\Users\kk\Desktop\internship\DataScience\Data-set\SampleData.csv")
#

# import numpy as np
# c=np.array([20,1,2,3,4])
#
# c[0]=100
#
# c[0]=2
#
# print(c)
#
# u = [1,0]
# v = [0,1]
# z = []
#
# for n,m in zip (u,v):
#     z.append(n+m)
#
# print(z)


# a = [1, 0, 6]
# b = [8, 1, 4]
# c = [2, 6, 1]
#
# d = []
#
# for x, y, z in zip(a, b, c):
#     d.append(x + y + z)
#
# print(d)
#
# import numpy as np
#
# u = np.array([1, 0])
# v = np.array([0, 1])
#
# z = u + v
# # z:array[1,1]
# print(z)
#
# import numpy as np
#
# u = np.array([1, 0])
# v = np.array([0, 1])
#
# z = u - v  # z:array[1,1]
# print(z)
#
# import numpy as np
#
# u = np.array([1, 0])
# v = np.array([0, 1])
#
# z = u * v  # z:array[1,1]
# print(z)

# a = np.array([2,3])
# b =2 * a
# print(b)
#
# a = [1,2]
# z = []
#
# for b in a:
#     z.append(2*b)
# print(z)

# import numpy as np
#
# a = np.array([2,12,42,3,-13,54,3])
# b = a + 1
# print(b)
#
# a = [21,22,122,135,56]
# b = []
# for c in a:
#     b.append(c+1)
# print(b)

# a = np.array([43,21,135,646,4464])
# b = a.dot(a)
# print(b)

# a = np.array([43,21,135,646,4464])
# mean = a.mean()
# print("Mean:",mean)
#
# a=np.array([0,1])
# b=np.array([1,0])
# c = np.dot(a,b)
# print(c)
#
# X=np.array([[1,0,1],[2,2,2]])
# out=X[0:2,2]
# print(out)

# X=np.array([[1,0],[0,1]])
# Y=np.array([[2,1],[1,2]])
# Z=np.dot(X,Y)
# print(Z)

# number = [1,2,3]
# for num in number:
#     print(num)

# j = 1
# while j <= 2:
#     print(j)
#     j += 1
#     continue

# for index in range (200,10,-35):
#     print(index)
#
# def check_prime(a):
#     if a > 1:
#         for i in range(2,a):
#             if a % i == 0:
#                 return False
#         return True
#     return False
#
# a = int(input("Enter your number: "))
#
# if check_prime(a):
#     print("It is prime number")
# else:
#     print("It is not prime number")
#
# text = input("enter the text: ")
# spam = False
#
# if ("Make a  lot of money").lower() in text.lower():
#     spam =  True
#     print("It's a Spam")
# elif ("Buy now").lower() in text.lower():
#     spam = True
#     print("It's a Spam")
# elif ("Subscribe This").lower() in text.lower():
#     spam = True
#     print("It's a Spam")
# elif ("Click This").lower() in text.lower():
#     spam = True
#     print("It's a Spam")
# else:
#     print("There is nothing wrong it not a spam ")

# user_name = input("Enter your user_name: ")
# user_name_without_space = user_name.replace(" ","")
#
# if len(user_name_without_space) == 10:
#     print("The length of user_name is equals to 10")
# elif len(user_name_without_space) < 10:
#     print("The length of user_name is less than  10")
# elif len(user_name_without_space) > 10:
#     print("The length of user_name is greater than  10")
# else:
#     print("Please Enter a valid name ")

# name_list = []
# while True:
#
#     name = input("Enter any name: ")
#
#     if name.lower() == "quit":
#         break
#
#     if name in name_list:
#         print("It's present in list")
#     else:
#         print("It is not present in list")
#
#     name_list.append(name)

# names = ["Sania","Hafsa","Hanzala","Mashood"]
# name = input("Enter name to check: ")
#
# if name.lower() in [n.lower() for n in names]:
#     print("It is present")
# else:
#     print("It is not present")

# marks1 = int(input("Enter marks1: "))
# marks2 = int(input("Enter marks2: "))
# total = 200
# result = ((marks1 + marks2)/200)*100
# percentage = result
# if result >= 90 and result <= 100:
#     print(f"Your grade is A++ and percentage is  {percentage} ")
# elif result >= 80 and result <= 90:
#     print(f"Your grade is A and percentage is {percentage}")
# elif result >= 70 and result <= 80:
#     print(f"Your grade is B and percentage is {percentage}")
# elif result >= 60 and result <= 70:
#     print(f"Your grade is C and percentage is {percentage}")
# elif result >= 50 and result <= 60:
#     print(f"Your grade is D and percentage is {percentage}")
# elif result < 50:
#     print(f"You grade is F and Your percentage is {percentage} and You are fail ")
# else:
#     print("Please enter valid numbers ")

# post = input("Enter the text:")
# user_post = post.lower()
#
# if "harry" in user_post:
#     print("It about Harry")
# else:
#     print("It does not about Harry")

# Method 1 simple call function
# def Greet():
#     print("Good Day Hanzala " )
# a = Greet()

# Method 2 pass argument
# def Greet(name):
#     print("Good Day " + name)
# a = Greet("Hanzala")

# Method 3
# def Greet (name):
#     gr = "Hello " + name
#     return gr
# a = Greet("Hanzala")
# print(a)

# import random
#
# r = random.randrange(1,20) # randrange function exclude 20 means it include number from 1 to 20
# r = random.randint(1,30) # randint function include 30 also
# print(r)

# i = 0
# while i < 100:
#     print(i)
#     i += 1

# a = [2,213,3122,211,2]
#
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# num = int(input("Enter any number: "))
# print(f"The tables of {num} is: ")
#
# for i in range(1,21):
#     result = num * i
#     print(f"{num} * {i} = {result}")

# num = int(input("Enter any number: "))
# print(f"The tables of {num} is: ")
# i = 1
#
# while  i < 21:
#     result = num * i
#     print(f"{num} * {i} = {result}")
#     i += 1

# text = input("Enter your text: ").lower()
# vowels = ["a","e","i","o","u"]
# vol_check = 0
# for vowel in text:
#     if vowel in vowels:
#         vol_check += 1
#
# print(f"the vowel in text are: {vol_check}")

# num = int(input("Enter any number: "))
# is_prime = True
# for i in range (2,num):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime and num > 1:
#     print("It a prime number ")
# else:
#     print("It not a prime number")

# def factorial (n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#        return n*factorial(n-1)
#
# result = (factorial(5))
# print(result)

# n = int(input("Enter the number: "))
# i = 1
# total = 0
# while i <= n:
#     total += i
#     i += 1

# print(f"The sum of n number is {total}")

# import math
# result = math.factorial(int(input("Enter the number for factorial: ")))
#  pie = math.pi
#  add = math.exp(5)
#  print(add)
#  print(pie)
#  print(result)

# n = int(input("Enter number for factorial: "))
# result = 1
#
# for i in range(1,n+1):
#     result *= i

# print(f"the factorial of {n} is: {result}")

# num = int(input("Enter number for tables: "))
# print(f"The Table of {num} is: ")
# for i in range (1,10+1):
#     re = num * i
#     print(f"{num} * {i} = {re}")

# num = int(input("Enter number for factorial: "))
# factorial = 1
#
# for i in range (1,num+1):
#     factorial = factorial * I
#
# print(f"the factorial of {num} is : {factorial}")

# right-angle triangle pattern
# string = "*"
# for x in range(1,6):
#     print(string * x)

# n = 4
#
# for i in range(4):
#     print("*" * (i+1))

# print("\n")
#   invert right-angle triangle pattern
# string = "*"
# for x in range(6,0,-1):
#     print(string * x)
#
# n = 5
#
# for i in range(n):
#     print(" " *(n - i - 1) + "*" *(2 * i + 1) + " " *(n - i - 1))

# Table in reversed order
# num = int(input("Enter number for tables: "))
# print(f"The Table of {num} is: ")
# for i in range (11,0,-1):
#     re = num * i
#     print(f"{num} * {i} = {re}")

# def greet (name="XYZ"):
#     print("Good Day \n " + name)
# greet("Hanzala")
# greet()
# greet("MAs-hood")

# def add (num1,num2):
#     return num1 + num2

#  add(5,2)
# print(add(4,3))

# l = ["he is a friend of mine".split()]
# print(l)
# l1 = ["The show is sprit against ".split()]
# print(l1)
# f = open("poem.txt","r")
# d = f.read()
# print(d)
# f.close()
# if "twinkle"  in  d:
#     print("It is present")
#     count = d.count("twinkle")
#     print(count)
# else:
#     print("It is not present")

# with open("poem.txt") as f:
#     read = f.read()
#     print(read)
#     if "Twinkle".lower() in read:
#         print("The word Twinkle is  present")
#         count = read.count("twinkle")
#         print(f"The word twinkle is present {count} time")
#     else:
#         print("The word Twinkle is not present")
# def game ():
#     score = 42
#     return score
#
# score = game()
#
# try:
#     with open("hiscore.txt", "a") as f:
#         hi_score= int(f.read())
# except Exception as e:
#     print(f"the file is not found {e}")
#     hi_score = 0
#
#
# if hi_score < score:
#     with open("hiscore.txt","w") as f:
#         f.write(str(score))
#
# f = open('sample.txt',"r")
# data = f.read()
# print(data)
#
# data = f.read()
# print(data)
#
# data = f.read()
# print(data)
#
# f.close()

# f = open("sample.txt","a")
# tr = f.write("How to update it to hii")
# print(tr)
# f.close()


# for i in range (2,31):
#     with open(f"tables/multiplication_table_of{i}.txt","w") as f:
#         for j in range(1,11):
#             f.write(f"{i}*{j} = {i*j}")
#             if j != 10:
#                 f.write("\n")
# with open("sample.txt","r") as f:
#     d = f.read()
#     print(d)
#     if "dog".lower() in d.lower():
#         new_d = d.replace("Dog","#####")
# with open("sample.txt","w") as f:
#     f.write(new_d)

# word = ["dog","donkey","shit","yuck"]
#
# with open("sample.txt","r") as f:
#     d = f.read()
#     print(d)
# for words in word:
#     if words.lower() in d.lower():
#         d = d.replace(words,"#####")
#
# with open("sample.txt","w") as f:
#     f.write(d)

# i = 1
#
# with open("logfile.txt") as f:
#     while True:
#         content = f.readline()
#         if not content:
#             break
#         if "python" in content.strip().lower():
#             print(f"'python' is there in line {i} ")
#             break
#         else:
#             i += 1

# with open("text.txt") as f:
#     content = f.read()
#
# with open("copy.txt","w") as f:
#     f.write(content)

# class Number ():
#     def sum (self,a,b):
#         return a + b
#
# num = Number()
# a = 1
# b = 3
# s = num.sum(a,b)
# print(s)

# class RailwayForm:
#     typeOfFrom = "railway form"
#     def printData (self):
#         print(f"Name is {self.name}")
#         print(f"Place to visit is {self.PlaceToVisit}")
#
#
# hanzalaapplication = RailwayForm()
# hanzalaapplication.name = "Hanzala"
# hanzalaapplication.PlaceToVisit = "London"
# hanzalaapplication.printData()

class Remote:
    def ispressedleft (self):
        pass
class Player:
    def moveLeft(self):
        pass
    def moveRight(self):
        pass
    def moveTop(self):
        pass

Player1 = Player()
Remote1 = Remote()

if (Remote1.ispressedleft()):
    Player1.moveLeft()

