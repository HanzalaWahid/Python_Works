
# Snake Water Gun game
import random
# A function name Win to check who is going to win
def Win(comp, you):
    if comp == you:
        return "IT's a Tie"
    elif comp == "s":
        if you == "g":
            return "You Win"
        else:
            return "Computer Win"
    elif comp == "w":
        if you == "s":
            return "You Win"
        else:
            return "Computer Win"
    elif comp == "g":
        if you == "w":
            return "You win"
        else:
            return "Computer Win"


print("Computer Turn: Snake (1) Water (2) and Gun (3) ")
# by using random module we randomly check what computer choose
comp_choice = random.randint(1, 3)
if comp_choice == 1:
    comp = "s"
elif comp_choice == 2:
    comp = "w"
elif comp_choice == 3:
    comp = "g"

print(f"Computer choose :{comp}")
you = input("Player 2 Turn : Snake (1) Water (2) and Gun (3) ")
validate_inputs = ["1", "2", "3"]

#check if input is validate or not
if you not in validate_inputs:
    print("Invalid Input.Please enter 1 , 2 ,3")
else:
    choice_mapping = {"1": "s", "2": "w", "3": "g"}
    result = Win(comp, choice_mapping[you])
    print(result)

# Same logic
# Rock Paper Scissor game
import random

def Win(comp, you):
    if comp == you:
        return "IT's a Tie"
    elif comp == "r":
        if you == "p":
            return "You win"
        else:
            return "Computer win"
    elif comp == "p":
        if you == "s":
            return "You win"
        else:
            return "Computer win"
    elif comp == "s":
        if you == "r":
            return "You win"
        else:
            return "Computer win"


print("Computer Turn: Rock (1) Paper(2) Scissor(3)")
comp_choice = random.randint(1, 3)
if comp_choice == 1:
    comp = "r"
elif comp_choice == 2:
    comp = "p"
if comp_choice == 3:
    comp = "s"

print(f"Computer choose {comp}")
you = input("Your Turn: Rock (1) Paper(2) Scissor(3)  ")
validate_input = ["1", "2", "3"]
choice_mapping = {"1": "r", "2": "p", "3": "s"}
if you  not in validate_input:
    print("Please Enter validate input: 1, 2, 3 ")
else:
    result = Win(comp, choice_mapping[you])
    print(result)
