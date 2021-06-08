import random

def get_users_choice():
    users_choice = str(input("> "))
    users_choice = users_choice.lower()
    return users_choice


def does_choice_exist(choices):
    while True:
        users_choice = get_users_choice()

        if users_choice in choices:
            return users_choice
            
        else:
            print("Not an option! Try again.")
    

def list_of_choices():
    choices = ["rock", "paper", "scissors"]
    return choices


def get_computers_choice(choices):
    computers_choice = random.choice(choices)
    return computers_choice


def get_winner(users_choice, computers_choice):

    print(f"You chose {users_choice}.")
    print(f"The computer chose {computers_choice}.")

    if users_choice == computers_choice:
        print("Draw!")

    elif users_choice == "rock" and computers_choice == "scissors" or users_choice == "paper" and computers_choice == "rock" or users_choice == "scissors" and computers_choice == "paper":
        print("You win!")
    
    elif users_choice == "rock" and computers_choice == "paper" or users_choice == "paper" and computers_choice == "scissors" or users_choice == "scissors" and computers_choice == "rock":
        print("You lose!")


def yes_or_no():
    while True:
        y_or_n = get_users_choice()
        if y_or_n == "y" or y_or_n == "n":
            return y_or_n
        
        else:
            print("Please answer y or n!")
       

def play_again():
    print("Play again? [y/n]")
    y_or_n = yes_or_no()
    if y_or_n == "n":
        exit_game()


def exit_game():
    exit(0)


def main():
    while True:
        choices = list_of_choices()

        print("rock/paper/scissors!")
        users_choice = does_choice_exist(choices)

        computers_choice = get_computers_choice(choices)
        get_winner(users_choice, computers_choice)

        play_again()

main()
