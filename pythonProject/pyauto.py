# # import time
# #
# # import pyautogui as auto
# #
# # time.sleep(5)
# #
# # for i in range(0,100):
# #     auto.typeWrite
# #
# # games = ["cricket","golf"]
# # print(games)
# # games.append("Hockey")
# # print(games)
# # games.insert(1,"Football")
# # print(games)
# # games.remove("golf")
# # print(games)
# # games.pop(1)
# # print(games)
# #
# # values = (3,4,5,6,7,9,15)
# # values.index(7,4)
# # print(values)
# # values.count(3)
# # print(values)
# # values.min(7)
# # print(values)
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
# df = pd.read_excel(r"C:\Users\kk\Desktop\intership\DataScience\Data-set\SampleData.csv")
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
#         print("It's is not present in list")
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
# print(f"The table of {num} is: ")
#
# for i in range(1,21):
#     result = num * i
#     print(f"{num} * {i} = {result}")

# num = int(input("Enter any number: "))
# print(f"The table of {num} is: ")
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

# print(f"the factorail of {n} is: {result}")

# num = int(input("Enter number for table: "))
# print(f"The Table of {num} is: ")
# for i in range (1,10+1):
#     re = num * i
#     print(f"{num} * {i} = {re}")

# num = int(input("Enter number for factorail: "))
# factorial = 1
#
# for i in range (1,num+1):
#     factorial = factorial * i
#
# print(f"the factorial of {num} is : {factorial}")
