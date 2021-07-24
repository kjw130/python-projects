class Utils:
    def y_n(self):
        while True:
            yes_or_no = input("[Y|N] >")
            yes_or_no = yes_or_no.lower()

            if yes_or_no == "y" or yes_or_no == "n":
                return yes_or_no

            else:
                print("Please enter y or n!")
                continue

    def number(self):
        while True:
            number = input("Enter a number >")
            try:
                number = int(number)
                return number
            except:
                print("Please enter as a number! ")
                continue


class Currency:
    def __init__(self, ConversionRateToUsd, ConversionRateFromUsd):
        self.ConversionRateToUsd = ConversionRateToUsd
        self.ConversionRateFromUsd = ConversionRateFromUsd

    def convertToUsd(self, Amount):
        conversion = Amount*self.ConversionRateToUsd
        return conversion

    def convertFromUsd(self,Amount):
        conversion = Amount*self.ConversionRateFromUsd
        return conversion


class USD(Currency):
    def __init__(self, ConversionRateToUsd, ConversionRateFromUsd):
        super().__init__(ConversionRateToUsd, ConversionRateFromUsd)


class AUD(Currency):
    def __init__(self, ConversionRateToUsd, ConversionRateFromUsd):
        super().__init__(ConversionRateToUsd, ConversionRateFromUsd)


class POUND(Currency):
    def __init__(self, ConversionRateToUsd, ConversionRateFromUsd):
        super().__init__(ConversionRateToUsd, ConversionRateFromUsd)


class CNY(Currency):
    def __init__(self, ConversionRateToUsd, ConversionRateFromUsd):
        super().__init__(ConversionRateToUsd, ConversionRateFromUsd)


class JPY(Currency):
    def __init__(self,ConversionRateToUsd, ConversionRateFromUsd):
        super().__init__(ConversionRateToUsd, ConversionRateFromUsd)


class App:
    def __init__(self):
        self.AvailableCurrencies = ['aud', 'usd', 'pound', 'cny', 'jpy']
        self.utils = Utils()
        self.usd = USD(1, 1)
        self.aud = AUD(0.74, 1.36)
        self.pound = POUND(1.38, 0.73)
        self.cny = CNY(0.15, 6.48)
        self.jpy = JPY(0.0090, 110.55)
        self.main()


    def Get_Conversion(self, ConvertTo, ConvertFrom, Amount):

        if ConvertTo == ConvertFrom:
            Conversion = Amount*1

        elif ConvertTo == 'usd':

            if ConvertFrom == 'aud':
                Conversion = self.aud.convertToUsd(Amount)
                
            elif ConvertFrom == 'pound':
                Conversion = self.pound.convertToUsd(Amount)

            elif ConvertFrom == 'cny':
                Conversion = self.cny.convertToUsd(Amount)
            
            elif ConvertFrom == 'jpy':
                Conversion = self.jpy.convertToUsd(Amount)

        elif ConvertTo == 'aud':
            
            if ConvertFrom == 'usd':
                Conversion = self.aud.convertFromUsd(Amount)

            elif ConvertFrom == 'pound':
                ConversionTranslate = self.pound.convertToUsd(Amount)
                Conversion = self.aud.convertFromUsd(ConversionTranslate)

            elif ConvertFrom == 'cny':
                ConversionTranslate = self.cny.convertToUsd(Amount)
                Conversion = self.aud.convertFromUsd(ConversionTranslate)
            
            elif ConvertFrom == 'jpy':
                ConversionTranslate = self.jpy.convertToUsd(Amount)
                Conversion = self.aud.convertFromUsd(ConversionTranslate)

        elif ConvertTo == 'pound':

            if ConvertFrom == 'usd':
                Conversion = self.pound.convertFromUsd(Amount)

            elif ConvertFrom == 'aud':
                ConversionTranslate = self.aud.convertToUsd(Amount)
                Conversion = self.pound.convertFromUsd(ConversionTranslate)

            elif ConvertFrom == 'cny':
                ConversionTranslate = self.cny.convertToUsd(Amount)
                Conversion = self.pound.convertFromUsd(ConversionTranslate)
            
            elif ConvertFrom == 'jpy':
                ConversionTranslate = self.jpy.convertToUsd(Amount)
                Conversion = self.pound.convertFromUsd(ConversionTranslate)

        elif ConvertTo == 'cny':
            if ConvertFrom == 'usd':
                Conversion = self.cny.convertFromUsd(Amount)

            elif ConvertFrom == 'aud':
                ConversionTranslate = self.aud.convertToUsd(Amount)
                Conversion = self.cny.convertFromUsd(ConversionTranslate)

            elif ConvertFrom == 'pound':
                ConversionTranslate = self.pound.convertToUsd(Amount)
                Conversion = self.cny.convertFromUsd(ConversionTranslate)
            
            elif ConvertFrom == 'jpy':
                ConversionTranslate = self.jpy.convertToUsd(Amount)
                Conversion = self.cny.convertFromUsd(ConversionTranslate)

        elif ConvertTo == 'jpy':

            if ConvertFrom == 'usd':
                Conversion = self.jpy.ConvertFromUsd(Amount)

            elif ConvertFrom == 'aud':
                ConversionTranslate = self.aud.convertToUsd(Amount)
                Conversion = self.jpy.convertFromUsd(ConversionTranslate)
            
            elif ConvertFrom == 'pound':
                ConversionTranslate = self.pound.convertToUsd(Amount)
                Conversion = self.jpy.convertFromUsd(ConversionTranslate)
            

            elif ConvertFrom == 'cny':
                ConversionTranslate = self.cny.convertToUsd(Amount)
                Conversion = self.jpy.convertFromUsd(ConversionTranslate)

        return Conversion


    def main(self):
        print(" ")
        print("Welcome to the currency converter!")
        print(" ")
        print(f"Available currencies are: {self.AvailableCurrencies}")

        while True:
            ConvertFrom = input("Enter the currency you would like to convert from: ")
            print(" ")
            ConvertFrom = ConvertFrom.lower()

            if ConvertFrom not in self.AvailableCurrencies:
                print("Error. That currency isn't available.")
                print(" ")
                print(f"Available currencies are: {self.AvailableCurrencies}")
                print(" ")
                continue
            break

        while True:
            ConvertTo = input("Enter the currency you would like to convert to: ")
            print(" ")
            ConvertTo = ConvertTo.lower()

            if ConvertTo not in self.AvailableCurrencies:
                print("Error. That currency isn't available.")
                print(" ")
                print(f"Available currencies are: {self.AvailableCurrencies}")
                print(" ")
                continue
            break

        while True:
            print(f"How much {ConvertFrom} do you want to convert into {ConvertTo}?")
            Amount = input(" >")
            try:
                Amount = int(Amount)
                if Amount == 0:
                    print("Can't convert from 0! Try again!")
                    print(" ")
                break
            except:
                print("Invalid input! Please enter as a number!")
                print(" ")

        Conversion = self.Get_Conversion(ConvertTo, ConvertFrom, Amount)
        print(f"{Amount} {ConvertFrom} = ${Conversion} {ConvertTo}")

        
App()
