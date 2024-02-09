import  random
randomnumber = random.randint(1,100)
userguess = None
guess = 0

while randomnumber != userguess:
        userguess = int(input("Enter the guess: "))
        guess += 1

        if randomnumber == userguess:
            print("Your guess is correct ")

        elif randomnumber > userguess:
            print("You guess is small. Try again ")
        else:
            print("You guess is large. Try again")

print(f"You guessed the number in {guess} guesses")

with open("highscore.txt","r") as f:
    hiscore = int(f.read())


if guess < hiscore:
    print("You just broken the Highscore")
    with open ("highscore.txt","w")as f:
         f.write(str(guess) + "\n")
