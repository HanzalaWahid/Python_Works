age = int(input("Enter Your Age: "))

if age >= 18:
    print("You Can Vote!")
    print("You Can not Vote " "Second time!")
elif 4 <= age <= 12:
    print("You Are a Kid!")
    print("You Can Vote When You are a Teen!")
# elif age > 18:
#      print('You are a Kid!')
else:
    print("You Can vote! But it wasn't count ")


