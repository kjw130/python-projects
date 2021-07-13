from questions import misc_number

class Hours:
    def __init__(self, payrate,casual, rate_for_calculations,  prompt):
        self.payrate = payrate
        self.rate_for_calculations = rate_for_calculations
        self.casual = casual
        self.prompt = prompt

        self.ask_hours = self.get_hours()
        self.saturday_rate, self.sunday_rate, self.public_holiday_rate = self.decide_payrate()


    def get_hours(self):
        print(self.prompt)
        ask_hours = misc_number()
        return ask_hours
    

    def decide_payrate(self):

        if self.casual == "y":
            saturday_rate = self.rate_for_calculations * 0.50 + self.rate_for_calculations
            sunday_rate = self.rate_for_calculations * 0.50 + self.rate_for_calculations * 0.25 + self.rate_for_calculations
        
        if self.casual == "n":
            saturday_rate = self.payrate * 0.25 + self.payrate
            sunday_rate = self.payrate * 0.50 + self.payrate

        public_holiday_rate = self.payrate * 2
        
        return saturday_rate, sunday_rate, public_holiday_rate


class Weekdays(Hours):
    def __init__(self, payrate,rate_for_calculations, casual, prompt):
        super().__init__(payrate,rate_for_calculations, casual, prompt)

    def calc_pay(self):
        pay = self.ask_hours*self.payrate
        return self.ask_hours, pay


class Saturday(Hours):
    def __init__(self, payrate,rate_for_calculations, casual, prompt):
        super().__init__(payrate,rate_for_calculations, casual, prompt)

    def calc_pay(self):
        pay = self.ask_hours*self.saturday_rate
        return self.ask_hours, pay


class Sunday(Hours):
    def __init__(self, payrate,rate_for_calculations, casual, prompt):
        super().__init__(payrate,rate_for_calculations, casual, prompt)

    def calc_pay(self):
        pay = self.ask_hours*self.sunday_rate
        return self.ask_hours, pay


class Public_holiday(Hours):
    def __init__(self, payrate,rate_for_calculations, casual, prompt):
        super().__init__(payrate,rate_for_calculations, casual, prompt)

    def calc_pay(self):
        pay = self.ask_hours * self.public_holiday_rate
        return self.ask_hours, pay







# def get_hours():

#     print()
    
    
#     print()
    

#     print()
    
    
    
    

#     return weekly_hours, saturday_hours, sunday_hours, public_holiday_hours


# # Split this into 2 classes. One for the hours and one for the payrate.

