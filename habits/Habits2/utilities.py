from datetime import date
import os
import os.path


def get_input():
    user_input = str(input("> "))
    user_input = user_input.lower()
    return user_input


def get_date():
    current_date = str(date.today())
    return current_date


def y_or_n():
    while True:
        yes_or_no = str(input("[y/n] >"))
        yes_or_no = yes_or_no.lower()

        if yes_or_no == "y" or yes_or_no == "n":
            return yes_or_no
        else:
            print("Please enter y or n.")


def print_user_habits(user_habits):
    for k, y in user_habits.items():
        print("\n" + k)

        for key in y:
            print(key + ':', y[key])

    print("")


def check_if_file_exists():
    does_file_exist = os.path.exists('user_habits.csv')
    return does_file_exist

def call_exit():
    exit(0)

