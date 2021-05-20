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


def get_payrate():
    
    print("What is your payrate?")
    payrate = misc_number()
    
    return payrate


def decide_payrate(payrate, yes_or_no):
    
    if yes_or_no == "y":
        rate_for_calculations = payrate / 1.25
        saturday_rate = rate_for_calculations * 0.50 + rate_for_calculations
        sunday_rate = rate_for_calculations * 0.50 + rate_for_calculations * 0.25 + rate_for_calculations
        
    else:
        rate_for_calculations = payrate
        saturday_rate = payrate * 0.25 + payrate
        sunday_rate = payrate * 0.50 + payrate

    public_holiday_rate = payrate * 2
    
    return rate_for_calculations, saturday_rate, sunday_rate, public_holiday_rate, 


def calc_pay(hours, payrate):
    
    pay = hours*payrate
    
    return pay


def get_weekly_hours_input():
    
    print("How many hours are you working during the week?")
    weekly_hours = misc_number()
    
    return weekly_hours


def get_saturday_hours_input():
    
    print("How many hours are you working on saturday?")
    saturday_hours = misc_number()
    
    return saturday_hours


def get_sunday_hours_input():
    
    print("How many hours are you working on sunday?")
    sunday_hours = misc_number()
    
    return sunday_hours


def publicHoliday():
    
    print("Are you working on a public holiday this week?")
    yes_or_no = y_or_n()
    
    return yes_or_no
    

def get_public_holiday_hours():
    
    yes_or_no = publicHoliday()

    if yes_or_no == "y":
        print("How many hours of public holiday time?")
        public_holiday_hours = misc_number()

    else:
        public_holiday_hours = 0

    return public_holiday_hours


def calculate_over_time_pay_rates(yes_or_no, rate_for_calculations):
    
    if yes_or_no == "y":
        calculate_overtime_rate = rate_for_calculations * 0.50 + rate_for_calculations * 0.25 + rate_for_calculations
        over_41_hours = ((rate_for_calculations * 0.50 + rate_for_calculations * 0.25 + rate_for_calculations) * 3)
        over41hoursrate = rate_for_calculations * 0.25 + rate_for_calculations * 2

    else:
        calculate_overtime_rate = rate_for_calculations * 0.50 + rate_for_calculations
        over_41_hours = ((rate_for_calculations * 0.50 + rate_for_calculations) * 3)
        over41hoursrate = rate_for_calculations * 2
    
    return calculate_overtime_rate, over_41_hours, over41hoursrate


def get_pay_before_taxes_and_overtime(weekday_pay, saturday_pay, sunday_pay, public_holiday_pay):

    before_taxes_and_overtime = weekday_pay + saturday_pay + sunday_pay + public_holiday_pay 

    return before_taxes_and_overtime
    

def calculate_overtime(payrate, total_hours, calculate_overtime_rate, over_41_hours, over41hoursrate, before_taxes_and_overtime):
    
    p = total_hours - 38

    if total_hours >= 38:

        while True:
            
            if 38 < total_hours <= 41:
                pay = ((total_hours - 38) * (calculate_overtime_rate)) + before_taxes_and_overtime - payrate * p
                break

            elif total_hours >= 42:
                pay = (((total_hours - 41) * over41hoursrate) + over_41_hours) + before_taxes_and_overtime - payrate * p
                break

            else:
                pay = before_taxes_and_overtime
                p = 0
                break
            
    else:
        pay = before_taxes_and_overtime
        p = 0
    
    return pay


def taxRates(tax_year):
    # Set tax is the tax for when you are in a higher bracket, if you are in bracket 3 in 2020,
    # You will always pay atleast $5,092 in tax from the previous bracket
    
    if tax_year == "2019":
        brackets = [18200, 37000, 90000, 180000]
        rates = [0.19, 0.325, 0.37, 0.45]
        set_tax = [3572, 20797, 54097]

    elif tax_year == "2020":
        brackets = [18200, 45000, 120000, 180000 ]
        rates = [0.19, 0.325, 0.37, 0.45]
        set_tax = [5092, 29467, 51667]

    return brackets, rates, set_tax


def incometax(pay, brackets, rates, set_tax):

    year_pay = pay * 52

    if year_pay <= (brackets[0]):
        tax = 0

    elif (brackets[0]) < year_pay <= (brackets[1]):
        tax = (year_pay - (brackets[0])) * (rates[0])

    elif (brackets[1]) <= year_pay <= (brackets[2]):
        tax = (year_pay - (brackets[1])) * (rates[1]) + (set_tax[0])

    elif (brackets[2]) < year_pay <= (brackets[3]):
        tax = (year_pay - (brackets[2])) * (rates[2]) + (set_tax[1])

    elif year_pay > (brackets[3]):
        tax = (year_pay - (brackets[3])) * (rates[3]) + (set_tax[2])

    return tax, year_pay


def low_tax_off_set(year_pay, tax, maximum_off_set, off_set_rate):
    
    if year_pay <= 18200:
        low_off_set = 0

    elif 18200 < year_pay <= 37500:
        if tax >= maximum_off_set:
            low_off_set = maximum_off_set
        # This is because the tax paid cannot be less than zero If the user is only paying $200 in tax, they can only
        # get a maximum of $200 tax offset, rather than the set rate of $700 or $445, depending on the year
        elif tax <= maximum_off_set:
            low_off_set = tax

    elif 37501 <= year_pay <= 45000:
        low_off_set = maximum_off_set - ((year_pay - 37500) * off_set_rate)

    elif 45001 <= year_pay <= 66667:
        low_off_set = 325 - ((year_pay - 45000) * 0.015)

    elif year_pay >= 66668:
        low_off_set = 0
        
    return low_off_set


def middle_income_offset(year_pay, tax, maximum_off_set):
    
    if year_pay <= 18200:
        middle_off_set = 0

    elif 18200 < year_pay <= 37000:
        if tax <= maximum_off_set:
            middle_off_set = 0

        elif maximum_off_set < tax < 955:
            middle_off_set = tax - maximum_off_set

        elif tax >= 955:
            middle_off_set = 255

    elif 37001 <= year_pay <= 48000:
        middle_off_set = 255 + ((year_pay - 37000) * 0.075)

    elif 48001 <= year_pay <= 90000:
        middle_off_set = 1080

    elif 90001 <= year_pay <= 126000:
        middle_off_set = 1080 - ((year_pay - 90001) * 0.03)

    elif year_pay >= 126000:
        middle_off_set = 0

    return middle_off_set


def offSetMaximum(tax_year):
    
    if tax_year == "2019":
        maximum_off_set = 445
        off_set_rate = 0.0165

    elif tax_year == "2020":
        maximum_off_set = 700
        off_set_rate = 0.05

    return maximum_off_set, off_set_rate


def calculate_total_off_set(tax, year_pay, tax_year):

    maximum_off_set, off_set_rate = offSetMaximum(tax_year)

    middle_off_set = middle_income_offset(year_pay, tax, maximum_off_set)
    low_off_set = low_tax_off_set(year_pay, tax, maximum_off_set, off_set_rate)

    total_off_set = low_off_set + middle_off_set

    return total_off_set


def calculate_medicare_levy(year_pay):
    
    if year_pay >= 28501:
        medicare_levy = year_pay * 0.02
    elif year_pay <= 28500:
        medicare_levy = 0

    return medicare_levy


def pay_after_tax(year_pay, tax, medicare_levy, total_off_set):

    pay_after_taxation = year_pay - tax - medicare_levy + total_off_set
    weekly_pay_after_tax = pay_after_taxation/52

    return pay_after_taxation, weekly_pay_after_tax


def y_or_n():
    
    while True:
        yes_or_no = str(input("[y/n] >"))
        yes_or_no = yes_or_no.lower()

        if yes_or_no == "y" or yes_or_no == "n":
            return yes_or_no
        else:
            print("Please enter y or n.")


def initial_questions():

    tax_year = get_tax_year()

    yes_or_no = input_for_casual_or_contracted()

    payrate = get_payrate()

    rate_for_calculations, saturday_rate, sunday_rate, public_holiday_rate = decide_payrate(payrate, yes_or_no)


    return tax_year, payrate, rate_for_calculations, yes_or_no, saturday_rate, sunday_rate, public_holiday_rate


def calculate_the_hours():

    weekly_hours = get_weekly_hours_input()
    saturday_hours = get_saturday_hours_input()
    sunday_hours = get_sunday_hours_input()
    public_holiday_hours = get_public_holiday_hours()
    total_hours = weekly_hours + saturday_hours + sunday_hours + public_holiday_hours

    return total_hours, weekly_hours, saturday_hours, sunday_hours, public_holiday_hours


def calculate_the_payrates(weekly_hours, payrate, saturday_hours, saturday_rate, sunday_hours, sunday_rate, public_holiday_hours, public_holiday_rate):

    weekday_pay = calc_pay(weekly_hours, payrate)
    saturday_pay = calc_pay(saturday_hours, saturday_rate)
    sunday_pay = calc_pay(sunday_hours, sunday_rate)
    public_holiday_pay = calc_pay(public_holiday_hours, public_holiday_rate)

    return weekday_pay, saturday_pay, sunday_pay, public_holiday_pay


def pay_totals():

    tax_year, payrate, rate_for_calculations, yes_or_no, saturday_rate, sunday_rate, public_holiday_rate = initial_questions()
    total_hours, weekly_hours, saturday_hours, sunday_hours, public_holiday_hours = calculate_the_hours()
    weekday_pay, saturday_pay, sunday_pay, public_holiday_pay = calculate_the_payrates(weekly_hours, payrate, saturday_hours, saturday_rate, sunday_hours, sunday_rate, public_holiday_hours, public_holiday_rate)
    before_taxes_and_overtime = get_pay_before_taxes_and_overtime(weekday_pay, saturday_pay, sunday_pay, public_holiday_pay)
    calculate_overtime_rate, over_41_hours, over41hoursrate = calculate_over_time_pay_rates(yes_or_no, rate_for_calculations)
    pay = calculate_overtime(payrate, total_hours, calculate_overtime_rate, over_41_hours, over41hoursrate, before_taxes_and_overtime)

    return pay, tax_year


def taxes():

    pay, tax_year = pay_totals() 
    brackets, rates, set_tax = taxRates(tax_year)
    tax, year_pay = incometax(pay, brackets, rates, set_tax)
    total_off_set = calculate_total_off_set(tax, year_pay, tax_year)
    medicare_levy = calculate_medicare_levy(year_pay)

    results(tax, total_off_set, year_pay, medicare_levy, pay)

    
 def results(tax, total_off_set, year_pay, medicare_levy, pay):
    
    pay_after_taxation, weekly_pay_after_tax = pay_after_tax(year_pay, tax, medicare_levy, total_off_set)
    
    print(f"You will earn ${pay: .2f} this week, before tax.")
    print(f"You will earn ${weekly_pay_after_tax: .2f} this week, after tax.")
    print(f"On this payrate, you will earn ${year_pay: .2f} a year, before tax.")
    print(f"On this payrate you will earn ${pay_after_taxation: .2f} a year, after tax.")
    print(f"This calculation includes a medicare levy of ${medicare_levy: .2f}, and a tax offset of ${total_off_set: .2f}")   
    

def calculate_everything():
    taxes()

    
def call_exit():
    exit(0)   

    
def mainFunc():
    
    while True:

        calculate_everything()

        print(" ")
        print(" ")
        print("Do you want to calculate again?")
        yes_or_no = y_or_n()

        if yes_or_no == "y":
            continue
        elif yes_or_no == "n":
            call_exit()


mainFunc()
