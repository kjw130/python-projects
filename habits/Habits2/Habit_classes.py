import os.path
import os
import csv
import utilities



class Habit_layout:
    def __init__ (self, habit, current_date):
        self.habit = habit
        self.current_date = current_date
        
        self.new = self.new_habit_layout()
        
    def new_habit_layout(self):
        new = {self.habit: {
            'Date started': self.current_date,
            'Current streak': 0}}

        return new


class Create_new:
    def __init__(self, user_habits):
        self.user_habits = user_habits
        print("Add a habit!")
        self.habit_input = utilities.get_input()
        self.current_date = utilities.get_date()
        self.new_habit = Habit_layout(self.habit_input, self.current_date)
        
    def add_new_habit(self):
        self.user_habits.update(self.new_habit.new_habit_layout())
        return self.user_habits


class Delete:
    def __init__(self, user_habits):
        self.user_habits = user_habits
        self.habit = self.decide_habit()

    def decide_habit(self):
        utilities.print_user_habits(self.user_habits)
        print("What habit do you want to delete?")
        habit = utilities.get_input()
        return habit

    
    def delete_habit(self):
        print(f"\nRemoving {self.habit}!")
        del self.user_habits[self.habit]
        utilities.print_user_habits(self.user_habits)

        return self.user_habits


    def delete_habits_func(self):
        
        while True:

            if self.habit in self.user_habits.keys():

                self.user_habits = self.delete_habit()

            else:
                print("Habit not found, try again?")

                yes_or_no = utilities.y_or_n()

                if yes_or_no == 'y':
                    self.delete_habits_func()

            return self.user_habits


class Addtostreak:
    def __init__(self, user_habits):
        self.user_habits = user_habits
        utilities.print_user_habits(self.user_habits)
    
    def add_to_streak(self):
        for x in self.user_habits:
            print(f"Did you do {x} today?")
            yes_or_no = utilities.y_or_n()
            if yes_or_no == "y":
                self.user_habits[x]["Current streak"] = self.user_habits[x]["Current streak"] + 1

            if yes_or_no == "n":
                continue

        return self.user_habits


class Delete_all:
    def __init__(self, user_habits):
        self.user_habits = user_habits

    def delete_all_habits(self):
        print("Are you sure you want to delete your habits?")
        yes_or_no = utilities.y_or_n()
        
        if yes_or_no == "y":
            does_file_exist = utilities.check_if_file_exists()
            if does_file_exist:
                os.remove("user_habits.csv")
            
            self.user_habits.clear()

        return self.user_habits
    

class Save:
    def __init__(self, user_habits):
        self.user_habits = user_habits
        
    def save_habit(self):
        if self.user_habits:
            with open('user_habits.csv', 'w', newline='') as file:
                fields = ['habit','Date started', 'Current streak' ]
                w = csv.DictWriter( file, fields )
                w.writeheader()
                for key,val in sorted(self.user_habits.items()):
                        row = {'habit': key}
                        row.update(val)
                        w.writerow(row)