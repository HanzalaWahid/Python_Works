def godown():
    print("GO UP ")
    print("GO SLOW ")
    print("GO HIGH ")
    print("GO DOWN ")
    print("GO GO GO FAST ")
    return True


print("The godown function is a working well")
godown_result = godown()

if godown_result:
    print("That great")
    num = int(input("Enter number: "))
    if num == 1:
        print("The input value is equal to 1 ")
    else:
        print("The input value is not equal to 1 ")

else:
    print("The godown function not return true")


def letter_generator(name, date):
    st = f"This is {name} and i will start my job from {date}"
    print(st)


letter_generator("Hanzala", "19 September 2023!")


# letter_generator("Hafsa",   "12 April 2023!")
# letter_generator("Hashir",  "4 December 2023!")
# letter_generator("Mashood", "21 September 2023!")

def average(a, b):
    return (a + b) / 2


result = average(43, 45)
print(result)
