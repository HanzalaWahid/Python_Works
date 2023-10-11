import random


def get_user_choice():
    while True:
        user_choice = input("Choose Rock,Paper or Scissors: ").strip().lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid Choice. Please choose Rock , Paper or Scissors ")


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "IT's a Tie"
    elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You Win"
    else:
        return "Computer Wins"


def play_game():
    print("Welcome to Rock, Paper and Scissor")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You choose {user_choice},and the computer choose {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Do you want to play again? (yes/no)").strip().lower()
        if play_again != "yes":
            break


if __name__ == "__main__":
    play_game()
