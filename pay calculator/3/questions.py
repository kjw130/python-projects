def get_tax_year():
    print("What tax year are you calculating for? [2019/2020]")
    
    while True:
        tax_year = str(input("> "))
        if tax_year == "2019" or tax_year == "2020":
            return tax_year

        else:
            print("Please input 2019 or 2020 depending on the tax year you want to do the taxes for.")


def input_for_casual_or_contracted():
    print("are you casual?")
    yes_or_no = y_or_n()
    return yes_or_no


def misc_number():
    while True:
        try:
            number = float(input("> "))
            return number

        except ValueError:
            print("Please input as a number!")


def y_or_n():
    while True:
        yes_or_no = str(input("[y/n] >"))
        yes_or_no = yes_or_no.lower()

        if yes_or_no == "y" or yes_or_no == "n":
            return yes_or_no
        else:
            print("Please enter y or n.")


def pay_rate(casual):
    print("What is your payrate?")
    payrate = misc_number()

    if casual == "y":
        rate_for_calculations = payrate / 1.25
    else:
        rate_for_calculations = payrate

    return payrate, rate_for_calculations
