# # # question 1 print fuction
# # print('''Twinkle, twinkle, little star,
# # 	How I wonder what you are!
# # 		Up above the world so high,
# # 		Like a diamond in the sky.
# # Twinkle, twinkle, little star,
# # 	How I wonder what you are''')
# # # question 2 Write a Python program to find out what version of Python you are using.
# #
# # import sys # sys to import specific details of version
# #
# # print("Python verssion")
# #
# # print(sys.version)
# #
# # # question 3 Write a Python program to display the current date and time.
# #
# # import datetime
# # import time
# #
# # current = datetime.datetime.now()
# # print("The time or date is ",current)
# #
# # # question 4 Write a Python program that calculates the area of a circle based on the radius entered by the user.
# #
# # radius = int(input("Enter the radius of circle: "))
# # area = 3.142 * float(radius*radius)
# # print("The area is ", area)
# #
# # #Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# #
# # name = input("Enter your fisrt name: ")
# #
# # name = input("Enter your last name: ")
# #
# # print(f"Hello {name} + {name} ")
# #
# # # 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# # list = [3, 5, 7, 23]
# # tuple =(3, 5, 7, 23)
# # print(list,tuple)
# #
# # # 8. Write a Python program to display the first and last colors from the following list.
# # color_list = ["Red","Green","White" ,"Black"]
# # print(color_list[0])
# # print(color_list[-1])
#
# # for i in range(5):
# #     for j in range(4):
# #         if j == i:
# #             print('*')
# #             break
# #         print(i,j)
#
# # 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#
# # n = int(input("Enter the number(n): "))
# # n1 = int(str(n)*1)
# # n2 = int(str(n)*2)
# # n3 = int(str(n)*3)
# # sum = n1 + n2 + n3
# # print(sum)
#
# # def check_prime(a):
# #     if a > 1:
# #         for i in range(2,0):
# #             if a % i == 0:
# #                 return False
# #         return True
# #     return False
# #
# # a = int(input("Enter number: "))
# #
# # if check_prime(a):
# #     print("It is a prime number")
# # else:
# #     print("It is not a prime number")
#
# # i = 0
# # while 50 >= i:
# #     print(i)
# #     i +=1
#
# # a = ['a','c','ac']
# # for item in a:
# #     print(item)
# # else:
# #     print("New item")
#
# # for i in range(1,1000,2):
# #     print("The all are odd number ",i)
# # #
# # for i in range (0,43):
# #     print(i)
# #     if i == 4:
# #         print("Just looking like a wow ")
# #         break
# #     else:
# #         print("Name kiya hai bhophinader jogi ")
# #         continue
#
# # for j in range(6):
# #     print("Aayein")
# #     if j == 5:
# #         continue
# #         print(j)
#
#
# # m = [2,1,21,11]
# # for i in m:
# #     # print(i)
# #     pass
#
# # p1 = Myclass()
# # print(p1.x)
#
#
# a = "Hanzala"
# b = "Hanzala"
# if a is b:
#     print("N")
# else:
#     print("A")
#
# a = [1,2,4,8]
# b = a
# c = [1,2,4,8]
# print(c is a)
# print(a is b)
#
#
# a = int(input("Enter any number: "))
# b = int(input("Enter any number: "))
# c = int(input("Enter any number: "))
# d = int(input("Enter any number: "))
#
# if a > b and  a > c and a > d:
#     print("a is greater ")
# elif b > a and b > c and b > d:
#     print("b is greater ")
# elif c > a and c > b and c > d:
#     print("c is greater ")
# elif d > a and d > b and d > c:
#     print("d is greater ")
#
#
# marks1 = int(input("Enter marks of subject one: "))
# marks2 = int(input("Enter marks of subject second: "))
#
#
# total = 200
# sum = marks1 + marks2
# percentage = (sum / total) * 100
#
# if percentage >= 40  and marks1 >= 33 and marks2 >= 33:
#     print("You passed :)")
# else:
#     print("You are failed :(")
# # print(percentage)
#
# import  re
#
# s1 = "Michael Jackson is the best"
#
# # Define the pattern to search for
# pattern = r"Jackson"
#
# # Use the search() function to search for the pattern in the string
# result = re.search(pattern, s1)
#
# # Check if a match was found
# if result:
#     print("Match found!")
# else:
#     print("Match not found.")
#
# import re
# pattern = r"(\d)(\d)(\d)(\d)(\D)(\D)"
# text = "1234AB"
# match = re.search(pattern,text)
# if match:
#     print("It found: ",match.groups())
# else:
#     print("It not found")
#
# import re
#
# s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
# # Define the regular expression pattern to search for
# pattern = r"King of Pop"
#
# # Define the replacement string
# replacement = "legend"
#
# # Use the sub function to replace the pattern with the replacement string
# new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)
# # The new_string contains the original string with the pattern replaced by the replacement string
# print(new_string)
# l1 = ["Ahmed","Sania","Sumaiya","Shaheer","Mashood","Sohail","Hanzala","Hashir"]
# for name in l1:
#     if name.startswith("S"):
#
#         print(f"Hello {name}")
#     else:
#         print("Hello Everyone")#
