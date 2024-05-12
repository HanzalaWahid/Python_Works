# try:
#     age = int(input("Enter your age: "))
#     if age <= 13:
#         print("You are a child ")
#     elif age <= 19 :
#         print("You are a Teen ")
#     elif age <= 59:
#         print("You are a Adult ")
#     else:
#         print("You are a Senior ")
# except Exception as e:
#     print(f"You entered something wrong which is {e}")
#
# day = input("Enter day in which you watch movie: ")
# movie_ticket = int(input("Enter your age: "))
# if age <= 18 and day == 'Wednesday':
#     print(f"The price is 12$ If day is  {day} It's a discount of 2$ ")
# elif age <= 8 and day == 'Wednesday':
#     print(f"The price is 8$ If day is {day} It's a discount of 2$")
# else:
#      print(f"The price is $10. There is no discount for {day}.")
#
# score = int(input("Enter your number: "))
# if score >= 90 and score <=  100:
#     print("Your Grade is A")
# elif score >= 80 and score < 90:
#     print("Your Grade is B")
# elif score >= 70 and score < 80:
#     print("Your Grade is C")
# elif score >= 60 and score < 60:
#     print("Your Grade is D")
# elif score > 0 and score < 60:
#     print("Your Grade is F")
# else:
#     print("Invalid  Grade ")
#
# Fruit = {"Banana":"Yellow","Grapes":"Green","Peach":"Brown"}
# fruit_name = input("Enter any fruit: ")
# fruit_name = fruit_name.capitalize()
#
# if fruit_name in Fruit:
#     color = Fruit[fruit_name].lower()
#     if color == "yellow":
#         print("It is Ripe")
#     elif color == "green":
#         print("It is Unripe")
#     elif color == "brown":
#         print("It is Overripe")
# else:
#     print("Choose fruit from the list")
#
# weather = ["sunny", "rainy", "snowy"]
# weather_choice = input("Enter your choice: ").strip().lower()
# if weather_choice in weather:
#     if weather_choice == "sunny":
#         print("Go for a walk")
#     elif weather_choice == "rainy":
#         print("Read a book")
#     elif weather_choice == "snowy":
#         print("Build a Snowman")
# else:
#     print("Choose a weather from above")
# try:
#     distance = int(input("Enter your distance: "))
#     if distance <= 3:
#         print(f"The distance is {distance}km your transportaion is walk")
#     elif distance <= 15:
#         print(f"The distance is {distance}km your transportaion is bike")
#     elif distance > 15:
#         print(f"The distance is {distance}km your transportaion is car")
# except Exception as e:
#     print(f"Their is a error {e}")
#     print("Choose a suitable distance")
#
# order_size = {"size1":'small',"size2":"meduim","size3":"large"}
# feeling = input("If you want a Extra-Shot (yes/no): ")
# order = input("Enter your size: ")
# if order in order_size:
#     if feeling.lower() == "yes":
#         print(f"The order is a {order_size[order]} coffee with a Extra-shot")
#     else:
#         print(f"The order  is {order_size[order]}")
# else:
#     print("You do not want any thing")
#
#
#
# password = input("Enter your password: ")
# if len(password) <= 6:
#     print("Your password is Weak")
# elif len(password) <= 8:
#     print("Your password is Medium")
# else:
#     print("Your password is Strong")
#
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
#
# print_continue = True
#
# for num in numbers:
#     if num % 2 == 0:
#         print(num)
#     elif num == 237:
#         break
#     elif print_continue:
#         print_continue = False
#
# if not  print_continue:
#     print("Contniue")

# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# count = 0

# for num in numbers:
#     if num < 0:
#         print(num,"is negative")
#     else:
#         print(num,"is positive")
#         count += 1
# print("Total positive number",count)

# n = int(input("Enter your range: "))
# Sum = 0
# for i in range(n):
#     if i % 2 == 0:
#         Sum += i
# print(Sum)


# table = int(input("Enter table for multiplication: "))
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(f"{table} * {i} = {table * i} ")

# first method to reverse a string
# string = input("Enter your string: ")
# reversed_string = ""
# for i in string:
#     reversed_string = i + reversed_string
#
# print(reversed_string)

# second method to reverse a string
# string = input("Enter your string: ")
# reversed_string = ""
# for i in range(len(string) -1 ,-1 , -1):
#     reversed_string += string[i]
#
# print(reversed_string)


# non_repated = []
#
# string = input("Enter string: ")
# for i in string:
#     if string.count(i) == 1:
#         non_repated.append(i)
#
# print(non_repated)
#
# fact = int(input("Enter number for factorial: "))
# result = 1
# for i in  range(1, fact + 1):
#     result *= i
#
#     print(result)

# num = 5
# facto = 1
# while num > 0:
#     facto *= num
#     num -= 1
#  print(f"the factorial is {facto}")

# while True:
#     user_input = int(input("Enter a number between 0 and 10: "))
#     if 1 <= user_input <= 10:
#         print("The number is between 1 and 10.")
#         break
#     print("Please enter a number between 0 and 10.")

# fruits = ["apple","mango","banana","kiwi","apple","kiwi","apple"]
# unique_item = set()
# for item in fruits:
#     if item in unique_item:
#         print("Duplicate",item)
#         break
#     else:
#         unique_item.add(item)

# import time

# wait_time = 1
# max_tries  = 5
# attempt = 0
#
# while attempt < max_tries:
#     print(f"Attempts {attempt + 1} Wait Time {wait_time}")
#     time.sleep(wait_time)
#     wait_time *= 2
#     attempt += 1

# import math
# def circle(radius):
#     return radius ** 2
#
# radius  = 6
# area = math.pi * circle(radius)
# print(area)

# def greet(name= "Hanzala"):
#     return "Hello \t" + name
#
# user = greet("MASHOOD")
# print(user)

# a = lambda x , y :( x ** 3 ,  y ** 2)
# result = a(2,6)
# print(result)

# def sum_all(*args):
#     return sum(args)
#
# print(sum_all(12,2,34,4353,5,3,53,53436654545,6))

# def kwargs(**kwargs):
#     for key , values in kwargs.items():
#         print(f"{key}:  {values} ")
#
# kwargs(name = "IRON MAN" , power = "Fly", enemy = "Thanos")

# def even_generator(limit):
#     for i in range(2,limit + 1, 2):
#         yield i
#
# for num in even_generator(10):
#     print(num)

# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num  * factorial(num - 1)
#
# num = 5
# print(f"Factorial of {num} is {factorial(num)}")


# class Car:
#     total_car = 0
#     def __init__(self,brand,model,fuel):
#         self.__brand = brand
#         self.model = model
#         self.fuel = fuel
#         Car.total_car += 1
#
#     def fuel_type(self):
#         print(f"The fuel required is {self.fuel}")
#     def show(self):
#         print(f"The brand name is {self.get_brand()} and model is {self.model} and the fuel required is {self.fuel}")
#     def get_brand(self):
#         return self.__brand
#
# c1 = Car("Toyota","CLI","2 liter diesel")
# c1.show()
# # print(f"Model:{c1.model} Brand:{c1.get_brand()}")
# class Electric_Car(Car):
#     def __init__(self,brand,model,battery_size,Electric_charge):
#         super().__init__(brand,model,Electric_charge)
#         self.battery_size = battery_size
#         self.Electric_charge = Electric_charge
#     def fuel_type(self):
#         print(f"The fuel required is {self.Electric_charge}")
#
#     def display(self):
#         super().show()
#         # print(f"The size of battery is {self.battery_size} and fuel requried is {self.Electric_charge}")
#
# c2 = Electric_Car("Rolls Royals","LAMOZIN","T40-78A","20 volts")
# c2.display()
# print(Car.total_car)

# import time
# def timer(func):
#     def wrapper(*args,**kwarg):
#         start_time = time.time()
#         result = func(*args,**kwarg)
#         end_time = time.time()
#         print(f"start time: {start_time} end time: {end_time}")
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)

# example_function(2)

# def debug (func):
#     def wrapper(*args,**kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwargs_value = ', '.join(f"{key} = {value}" for key, value in kwargs.items())
#         result = func(*args,**kwargs)
#         print(f"calling {func.__name__} with value is args: {args_value}, kwargs is {kwargs_value}")
#         return result
#     return wrapper
# @debug
# def greet(name,greet="Hello"):
#     print(f"{name} {greet}")
#
# greet("Hanzala")


import time

# def cache(func):
#
#     cache_value = {}
#     def wrapper(*args):
#         if args in cache_value:
#             return cache_value[args]
#         result = func(*args)
#         return result
#     return wrapper
# @cache
# def long_function(a,b):
#     time.sleep(4)
#     return a + b
#
# print(long_function(4,5))

