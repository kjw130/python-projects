class User_results:
    def __init__(self, pay, weekly_pay_after_tax, year_pay, pay_after_taxation, medicare_levy, total_off_set):
        self.pay = pay
        self.weekly_pay_after_tax = weekly_pay_after_tax
        self.year_pay = year_pay
        self.pay_after_taxation = pay_after_taxation
        self.medicare_levy = medicare_levy
        self.total_off_set = total_off_set
    
    def print_results(self):
        print(f"You will earn ${self.pay: .2f} this week, before tax.")
        print(f"You will earn ${self.weekly_pay_after_tax: .2f} this week, after tax.")
        print(f"On this payrate, you will earn ${self.year_pay: .2f} a year, before tax.")
        print(f"On this payrate you will earn ${self.pay_after_taxation: .2f} a year, after tax.")
        print(f"This calculation includes a medicare levy of ${self.medicare_levy: .2f}, and a tax offset of ${self.total_off_set: .2f}")

