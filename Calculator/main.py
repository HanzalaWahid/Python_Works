print("Welcome to Calculator ")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multilpy(a, b):
    return a * b

def divison(a, b):
    if b == 0:
        print("DIVISION IS NOT POSSIBLE")
        return none
    return a / b

a = float(input("Enter First number: "))
b = float(input("Enter Second number: "))

opt = input("Enter the opreation (+,-,*,/)")

if opt == "+":
    result = (add(a, b))
elif opt == "-":
    result = (subtract(a, b))
elif opt == "*":
    result = (multilpy(a, b))
elif opt == "/":
    result = (divison(a, b))
else:
    print("You entered wrong operation :) ")
    result = None

if result is not None:
    print("Result", result)
