import questions
import get_user_hours
import get_tax
import utilities
import overtime
import get_user_hours
import user
import os
import sys


class App:

    def __init__(self):
        self.tax_year = questions.get_tax_year()
        self.casual = questions.input_for_casual_or_contracted()
        self.payrate, self.rate_for_calculations = questions.pay_rate(self.casual)
        self.total_pay, self.total_hours = self.get_questions()
        self.pay, self.year_pay = self.calculate_overtime()
        self.medicare_levy, self.total_off_set, self.pay_after_taxation, self.weekly_pay_after_tax = self.tax()
        self.main()


    def y_n(self):
        while True:
            y_or_n = input('[Y/N] > ')

            if y_or_n == 'y' or y_or_n == 'n':
                return y_or_n

            else:
                print("Error. Please enter y or n!")
                continue


    def get_questions(self):
        calc_weekday = get_user_hours.Weekdays(self.payrate, self.casual, self.rate_for_calculations, "How many hours are you working during the week?")
        weekday_hours, weekday_pay = calc_weekday.calc_pay()

        calc_saturday = get_user_hours.Saturday(self.payrate, self.casual,self.rate_for_calculations, "How many hours are you working on saturday?")
        saturday_hours, saturday_pay = calc_saturday.calc_pay()

        calc_sunday = get_user_hours.Sunday(self.payrate, self.casual, self.rate_for_calculations, "How many hours are you working on sunday?")
        sunday_hours, sunday_pay = calc_sunday.calc_pay()

        print("Are you working on a public holiday this week?")
        pub_hol = self.y_n()

        if pub_hol == "y":
            calc_public_holiday = get_user_hours.Public_holiday(self.payrate, self.casual, self.rate_for_calculations,"How many hours of public holiday time?")
            public_holiday_hours, public_holiday_pay = calc_public_holiday.calc_pay()

        else:
            public_holiday_hours = 0
            public_holiday_pay = 0
        
        total_hours = weekday_hours + saturday_hours + sunday_hours + public_holiday_hours 
        total_pay = weekday_pay + saturday_pay + sunday_pay + public_holiday_pay

        return total_pay, total_hours


    def calculate_overtime(self):
        if self.casual == "y":
            calculate_overtime_rate = self.rate_for_calculations * 0.50 + self.rate_for_calculations * 0.25 + self.rate_for_calculations
            over_41_hours = ((self.rate_for_calculations * 0.50 + self.rate_for_calculations * 0.25 + self.rate_for_calculations) * 3)
            over41hoursrate = self.rate_for_calculations * 0.25 + self.rate_for_calculations * 2

        else:
            calculate_overtime_rate = self.rate_for_calculations * 0.50 + self.rate_for_calculations
            over_41_hours = ((self.rate_for_calculations * 0.50 + self.rate_for_calculations) * 3)
            over41hoursrate = self.rate_for_calculations * 2
        
        p = self.total_hours - 38

        if self.total_hours >= 38:

            while True:
                
                if 38 < self.total_hours <= 41:
                    pay = ((self.total_hours - 38) * (calculate_overtime_rate)) + self.total_pay - self.payrate * p
                    break

                elif self.total_hours >= 42:
                    pay = (((self.total_hours - 41) * over41hoursrate) + over_41_hours) + self.total_pay - self.payrate * p
                    break

                else:
                    pay = self.total_pay
                    p = 0
                    break
                
        else:
            pay = self.total_pay
            p = 0
        
        year_pay = pay * 52
        return pay, year_pay


    def tax(self):
        taxes = get_tax.Tax(self.year_pay, self.tax_year)
        medicare_levy, total_off_set, pay_after_taxation, weekly_pay_after_tax = taxes.results()

        return medicare_levy, total_off_set, pay_after_taxation, weekly_pay_after_tax


    def main(self):

        while True:

            results = user.User_results(self.pay, self.weekly_pay_after_tax, self.year_pay, self.pay_after_taxation, self.medicare_levy, self.total_off_set)
            results.print_results()

            print(" ")
            print(" ")
            print("Do you want to calculate again?")
            yes_or_no = questions.y_or_n()

            if yes_or_no == "y":
                break
            
            elif yes_or_no == "n":
                utilities.call_exit()

def main():
    while True:
        App()

main()
        
            
            
            


            
            
            
            

            

