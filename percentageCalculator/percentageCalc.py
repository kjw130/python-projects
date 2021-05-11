def options():
    print("Welcome to the percentage calculator, what would you like to calculate?")
    print("If you want to calculate what a percentage of a number is, press 1")
    print("If you want to increase a number by a percentage, press 2")
    print("If you want to find the percentage change, press 3")
    print("If you want to find what percent a number is of another number, press 4")
    

def ask_user():
    options()
    
    while True:
        ask_user.option = str(input("> "))
        ask_user.option = ask_user.option.lower()

        if ask_user.option == "1" or ask_user.option == "2" or ask_user.option == "3" or ask_user.option == "4":
            break

        elif ask_user.option == "options":
            ask_user()

        elif ask_user.option != "1" or ask_user.option != "2" or ask_user.option != "3" or ask_user.option != "4":
            print("Please enter 1, 2, 3 or 4 depending on what you want to calculate.")
            print("If you want to see the options again type 'options'")
            

def get_numbers():
    if ask_user.option == "1":
        print("Enter the number you want to find the percentage of, followed by the percentage.")
    elif ask_user.option == "2":
        print("Enter the number you want to increase by a percentage, followed by the percentage.")
    elif ask_user.option == "3":
        print("Enter the old number, followed by the number after the percentage change.")
    elif ask_user.option == "4":
        print("Enter the first number, followed by the second number.")

    while True:
        try:
            number1 = float(input("> "))
            number2 = float(input("> "))
            return number1, number2
            
        except ValueError:
            print("Please input the numbers as numbers. ie: 12")
        

def find_percent_of(number1, number2):
    decimal = number2 / 100
    percentage_of = number1 * decimal

    print(f"{number2}% of {number1} is {percentage_of}.")
    

def increase_number_by_a_percent(number1, number2):
    decimal = number2 / 100
    percentage_of = number1 * decimal
    result = number1 + percentage_of

    print(f"Increasing {number1} by {number2}%, results in {result}.")


def percentage_change(number1, number2):
    subtract = number2 - number1
    result = (subtract / number1) * 100

    print(f"The percentage change is {result: .2f}%.")


def percent_of_x_is_x(number1, number2):
    result = (number1 / number2) * 100

    print(f"{number1} is {result: .2f}% of {number2}.")


def main():
    ask_user()
    number1, number2 = get_numbers()

    if ask_user.option == "1":
        find_percent_of(number1, number2)

    elif ask_user.option == "2":
        increase_number_by_a_percent(number1, number2)

    elif ask_user.option == "3":
        percentage_change(number1, number2)

    elif ask_user.option == "4":
        percent_of_x_is_x(number1, number2)


main()
