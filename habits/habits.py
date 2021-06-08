import pickle
from datetime import date
import os.path
import os


def get_input():
    user_input = str(input("> "))
    user_input = user_input.lower()
    return user_input


def get_date():
    current_date = str(date.today())
    return current_date


def new_habit_layout():
    print("Add a habit!")
    user_input = get_input()
    current_date = get_date()

    new = {user_input: {
        'Date started': current_date,
        'Current streak': 0}}

    return new


def load_list():
    pickle_off = open('habit_list.txt', 'rb')
    user_habits = pickle.load(pickle_off)

    return user_habits


def open_list_new_or_old(new_or_old_list):
    if new_or_old_list == "new":
        user_habits = new_habit_layout()

    elif new_or_old_list == "old":
        user_habits = load_list()

    return user_habits


def y_or_n():
    while True:
        yes_or_no = str(input("[y/n] >"))
        yes_or_no = yes_or_no.lower()

        if yes_or_no == "y" or yes_or_no == "n":
            return yes_or_no
        else:
            print("Please enter y or n.")


def amount_of_days(started):
    today = get_date()
    days = today - started
    days = days.days()
    return days


def add_new_habit(user_habits):
    new_habit = new_habit_layout()
    user_habits.update(new_habit)
    print_user_habits(user_habits)

    return user_habits


def delete_habit(user_habits, habit):
    print(f"\nRemoving {habit}!")
    del user_habits[habit]
    print_user_habits(user_habits)

    return user_habits


def delete_habits_func(user_habits):
    print_user_habits(user_habits)

    print("What habit do you want to delete?")

    habit = get_input()

    if habit in user_habits.keys():

        user_habits = delete_habit(user_habits, habit)

    else:
        print("Habit not found, try again?")

        yes_or_no = y_or_n()

        if yes_or_no == 'y':
            delete_habits_func(user_habits)

    return user_habits


def add_to_streak(user_habits):
    for x in user_habits:
        print(f"Did you do {x} today?")
        yes_or_no = y_or_n()
        if yes_or_no == "y":
            user_habits[x]["Current streak"] = user_habits[x]["Current streak"] + 1

        if yes_or_no == "n":
            continue
    print_user_habits(user_habits)


def print_options():
    print("Do you want to create a new habit, add to a streak, delete a habit, save, exit the app, or delete all habits?")
    print("[new/add/delete/save/exit/all]")


def new_habit_or_stats():
    while True:

        print_options()
        habit_or_stats = get_input()
        if habit_or_stats == "new" or habit_or_stats == "add" or habit_or_stats == "delete" \
                or habit_or_stats == "save" or habit_or_stats == "exit" or habit_or_stats == "all":

            return habit_or_stats

        else:
            print(f"{habit_or_stats} didn't work. Try again!")


def delete_all_habits():
    os.remove("habit_list.txt")


def habit_stats_exit(user_habits):
    habit_or_stats = new_habit_or_stats()

    if habit_or_stats == "new":
        user_habits = add_new_habit(user_habits)

    elif habit_or_stats == "add":
        add_to_streak(user_habits)

    elif habit_or_stats == "delete":
        user_habits = delete_habits_func(user_habits)

    elif habit_or_stats == "save":
        save_habit(user_habits)
        print(f"Successfully saved!")

    elif habit_or_stats == "exit":
        print(f"Save before exiting?")
        yes_or_no = y_or_n()
        if yes_or_no == "y":
            save_habit(user_habits)
        call_exit()

    elif habit_or_stats == "all":
        delete_all_habits()


def check_if_file_exists():
    does_file_exist = os.path.exists('habit_list.txt')
    return does_file_exist


def new_or_old(does_file_exist):
    if does_file_exist:
        new_or_old_list = "old"

    elif not does_file_exist:
        new_or_old_list = 'new'

    return new_or_old_list


def print_user_habits(user_habits):
    for k, y in user_habits.items():
        print("\n" + k)

        for key in y:
            print(key + ':', y[key])

    print("")


def save_habit(user_habits):
    with open('habit_list.txt', 'wb') as fh:
        pickle.dump(user_habits, fh)


def call_exit():
    exit(0)


def start_of_app():
    does_file_exist = check_if_file_exists()
    new_or_old_list = new_or_old(does_file_exist)
    user_habits = open_list_new_or_old(new_or_old_list)

    return user_habits


def main():
    user_habits = start_of_app()
    print_user_habits(user_habits)

    while True:
        habit_stats_exit(user_habits)


if __name__ == "__main__":
    main()
