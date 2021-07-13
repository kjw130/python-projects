import csv
import os
import os.path
import Habit_classes
import utilities

class StartApp:
    def __init__(self):
        self.does_file_exist = utilities.check_if_file_exists()
        self.user_habits = self.detect_csv()
        Main(self.user_habits)

    def detect_csv(self):
        
        if not self.does_file_exist:
            new_or_old_list = 'new'
        elif self.does_file_exist:
            new_or_old_list = "old"

        if new_or_old_list == "new":
            user_habits = {}
            new = Habit_classes.Create_new(user_habits)
            user_habits = new.add_new_habit()

        elif new_or_old_list == "old":
            user_habits = self.load_list()
        
        return user_habits

    def load_list(self):
        with open('user_habits.csv', mode ='r')as file:

            csvFile = csv.DictReader(file)

            iterations = 0
            for lines in csvFile:
                if iterations == 0:
                    user_habits = {lines['habit']: {
                    'Date started': lines['Date started'],
                    'Current streak': lines['Current streak']}}
                    iterations +=1
                else:
                    new_habit = {lines['habit']: {
                    'Date started': lines['Date started'],
                    'Current streak': lines['Current streak']}}
                    
                    user_habits.update(new_habit)

        return user_habits


class Main:
    def __init__(self, user_habits):
        self.user_habits = user_habits
        self.main()

    def new_habit_or_stats(self):
        while True:
            print("Do you want to create a new habit, add to a streak, delete a habit, save, exit the app, or delete all habits?")
            print("[new/add/delete/save/exit/all]")
            habit_or_stats = utilities.get_input()
            if habit_or_stats == "new" or habit_or_stats == "add" or habit_or_stats == "delete" \
                    or habit_or_stats == "save" or habit_or_stats == "exit" or habit_or_stats == "all":

                return habit_or_stats

            else:
                print(f"{habit_or_stats} didn't work. Try again!")

    def main(self):
        
        while True:

            utilities.print_user_habits(self.user_habits)

            habit_or_stats = self.new_habit_or_stats()

            if habit_or_stats == "new":
                new = Habit_classes.Create_new(self.user_habits)
                self.user_habits = new.add_new_habit()

            elif habit_or_stats == "add":
                add = Habit_classes.Addtostreak(self.user_habits)
                self.user_habits = add.add_to_streak()

            elif habit_or_stats == "delete":
                delete = Habit_classes.Delete(self.user_habits)
                self.user_habits = delete.delete_habits_func()

            elif habit_or_stats == "save":
                save = Habit_classes.Save(self.user_habits)
                save.save_habit()

                print(f"Successfully saved!")

            elif habit_or_stats == "exit":
                print(f"Save before exiting?")

                yes_or_no = utilities.y_or_n()

                if yes_or_no == "y":
                    save = Habit_classes.Save(self.user_habits)
                    save.save_habit()

                utilities.call_exit()

            elif habit_or_stats == "all":
                delete_all = Habit_classes.Delete_all(self.user_habits)
                self.user_habits = delete_all.delete_all_habits()


if __name__ == "__main__":
    StartApp()
