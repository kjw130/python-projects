class Tax:
    def __init__(self, year_pay,  tax_year):
        
        self.year_pay = year_pay
        self.tax_year = tax_year
        self.tax = self.incometax()
        self.maximum_off_set, self.off_set_rate = self.offSetMaximum()
        self.low_off_set = self.low_tax_off_set()
        self.middle_off_set = self.middle_income_offset()
        self.total_off_set = self.calculate_total_off_set()
        
        self.medicare_levy = self.calculate_medicare_levy()
        self.pay_after_taxation, self.weekly_pay_after_tax = self.pay_after_tax()


    def pay_after_tax(self):
        pay_after_taxation = self.year_pay - self.tax - self.medicare_levy + self.total_off_set
        weekly_pay_after_tax = pay_after_taxation/52
        
        return pay_after_taxation, weekly_pay_after_tax


    def calculate_medicare_levy(self):
        if self.year_pay >= 28501:
            medicare_levy = self.year_pay * 0.02
        elif self.year_pay <= 28500:
            medicare_levy = 0

        return medicare_levy


    def incometax(self):
        
        if self.tax_year == "2019":
            brackets = [18200, 37000, 90000, 180000]
            rates = [0.19, 0.325, 0.37, 0.45]
            set_tax = [3572, 20797, 54097]

        elif self.tax_year == "2020":
            brackets = [18200, 45000, 120000, 180000 ]
            rates = [0.19, 0.325, 0.37, 0.45]
            set_tax = [5092, 29467, 51667]

        if self.year_pay <= (brackets[0]):
            tax = 0

        elif (brackets[0]) < self.year_pay <= (brackets[1]):
            tax = (self.year_pay - (brackets[0])) * (rates[0])

        elif (brackets[1]) <= self.year_pay <= (brackets[2]):
            tax = (self.year_pay - (brackets[1])) * (rates[1]) + (set_tax[0])

        elif (brackets[2]) < self.year_pay <= (brackets[3]):
            tax = (self.year_pay - (brackets[2])) * (rates[2]) + (set_tax[1])

        elif self.year_pay > (brackets[3]):
            tax = (self.year_pay - (brackets[3])) * (rates[3]) + (set_tax[2])

        return tax

    def offSetMaximum(self):
        if self.tax_year == "2019":
            maximum_off_set = 445
            off_set_rate = 0.0165

        elif self.tax_year == "2020":
            maximum_off_set = 700
            off_set_rate = 0.05

        return maximum_off_set, off_set_rate


    def low_tax_off_set(self):
        
        if self.year_pay <= 18200:
            low_off_set = 0

        elif 18200 < self.year_pay <= 37500:
            if self.tax >= self.maximum_off_set:
                low_off_set = self.maximum_off_set
            # This is because the tax paid cannot be less than zero If the user is only paying $200 in tax, they can only
            # get a maximum of $200 tax offset, rather than the set rate of $700 or $445, depending on the year
            elif self.tax <= self.maximum_off_set:
                low_off_set = self.tax

        elif 37501 <= self.year_pay <= 45000:
            low_off_set = self.maximum_off_set - ((self.year_pay - 37500) * self.off_set_rate)

        elif 45001 <= self.year_pay <= 66667:
            low_off_set = 325 - ((self.year_pay - 45000) * 0.015)

        elif self.year_pay >= 66668:
            low_off_set = 0
            
        return low_off_set
    

    def middle_income_offset(self):
        if self.year_pay <= 18200:
            middle_off_set = 0

        elif 18200 < self.year_pay <= 37000:
            if self.tax <= self.maximum_off_set:
                middle_off_set = 0

            elif self.maximum_off_set < self.tax < 955:
                middle_off_set = self.tax - self.maximum_off_set

            elif self.tax >= 955:
                middle_off_set = 255

        elif 37001 <= self.year_pay <= 48000:
            middle_off_set = 255 + ((self.year_pay - 37000) * 0.075)

        elif 48001 <= self.year_pay <= 90000:
            middle_off_set = 1080

        elif 90001 <= self.year_pay <= 126000:
            middle_off_set = 1080 - ((self.year_pay - 90001) * 0.03)

        elif self.year_pay >= 126000:
            middle_off_set = 0

        return middle_off_set


    def calculate_total_off_set(self):
        total_off_set = self.low_off_set + self.middle_off_set
        return total_off_set


    def results(self):
        return self.medicare_levy, self.total_off_set, self.pay_after_taxation, self.weekly_pay_after_tax

    

    




    






