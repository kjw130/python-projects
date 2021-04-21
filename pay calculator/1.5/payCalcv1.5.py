wksInYear = 52
def rate():
    while True:
        try:
            rate.userPayrate = float(input("What is your payrate?"))
            break
        except ValueError:
            print("Please enter your payrate as a number!")
    
def hourlyPay():
    if calculatePay.casorcont == "y":

        hourlyPay.casualPay = rate.userPayrate / 1.25
        hourlyPay.saturdayPay = hourlyPay.casualPay * 0.50 + hourlyPay.casualPay
        hourlyPay.sundayPay = hourlyPay.casualPay * 0.50 + hourlyPay.casualPay * 0.25 + hourlyPay.casualPay
        
        print("On Saturday you will earn " + str(hourlyPay.saturdayPay) + " per hour")
        print("On Sunday you will earn " + str(hourlyPay.sundayPay) + " per hour")
    
    elif calculatePay.casorcont == "n":

        hourlyPay.saturdayPay = rate.userPayrate * 0.25 + rate.userPayrate
        hourlyPay.sundayPay = rate.userPayrate * 0.50 + rate.userPayrate
        
        print("On Saturday you will earn " + str(hourlyPay.saturdayPay) + " per hour")
        print("On Sunday you will earn " + str(hourlyPay.sundayPay) + " per hour")

def publicHoliday():
    publicHol = rate.userPayrate * 2
    if calculatePay.casorcont == "y":
        pubHol = input("Are you working on a public holiday this week? [Y/N]")
        pubHol = pubHol.lower()
        while True:
            if pubHol == "y":
                while True:
                    try:
                        pub = float(input("How many hours of public holiday time?"))
                        break
                    except ValueError:
                        print("Please enter your hours as a number!")

                while True:
                    try:
                        casHr = float(input("How many hours are you working during the week?"))
                        break
                    except ValueError:
                        print("Please enter your hours as a number!")

                while True:
                    try:
                        totalSaturdayHours = float(input("How many hours are you working on saturday?"))
                        break
                    except ValueError:
                        print("Please enter your hours as a number!")

                while True:
                    try:
                        totalSundayHours = float(input("How many hours are you working on Sunday?"))
                        break
                    except ValueError:
                        print("Please enter your hours as a number!")

                pubp = pub * publicHol
                publicHoliday.totalWeekHrs = casHr + totalSaturdayHours + totalSundayHours + pub
                casWkPay = rate.userPayrate * casHr
                casSatPay = hourlyPay.saturdayPay * totalSaturdayHours
                casSunPay = hourlyPay.sundayPay * totalSundayHours
                publicHoliday.casTot = casWkPay + casSatPay + casSunPay + pubp
                break

            elif pubHol == "n":
                while True:
                    try:
                        casHr = float(input("How many hours are you working during the week?"))
                        break
                    except ValueError:
                        print("Please enter your hours as a number!")

                while True:
                    try:
                        totalSaturdayHours = float(input("How many hours are you working on saturday?"))
                        break
                    except ValueError:
                        print("Please enter your hours as a number!") 

                while True:
                    try:
                        totalSundayHours = float(input("How many hours are you working on Sunday?"))
                        break
                    except ValueError:
                        print("Please enter your hours as a number!")

                publicHoliday.totalWeekHrs = casHr + totalSaturdayHours + totalSundayHours
                casWkPay = rate.userPayrate * casHr
                casSatPay = hourlyPay.saturdayPay * totalSaturdayHours
                casSunPay = hourlyPay.sundayPay * totalSundayHours
                publicHoliday.casTot = casWkPay + casSatPay + casSunPay
                break
                
            elif pubHol != "y" or "n":
                pubHol = (input("Please enter y or n!"))
                pubHol = pubHol.lower()
                continue

    elif calculatePay.casorcont == "n":
            pubHol = input("Are you working on a public holiday this week? [Y/N]")   
            pubHol = pubHol.lower()
            while True:
                if pubHol == "y":
                    while True:
                        try:
                            pub = float(input("How many hours of public holiday time?"))
                            break
                        except ValueError:
                            print("Please enter your hours as a number!")
                            
                    while True:
                        try:
                            casHr = float(input("How many hours are you working during the week?"))
                            break
                        except ValueError:
                            print("Please enter your hours as a number!")

                    while True:
                        try:
                            totalSaturdayHours = float(input("How many hours are you working on saturday?"))
                            break
                        except ValueError:
                            print("Please enter your hours as a number!")

                    while True:
                        try:
                            totalSundayHours = float(input("How many hours are you working on Sunday?"))
                            break
                        except ValueError:
                            print("Please enter your hours as a number!")

                    pubp = pub * publicHol
                    publicHoliday.totalWeekHrs = casHr + totalSaturdayHours + totalSundayHours + pub
                    casWkPay = rate.userPayrate * casHr
                    casSatPay = hourlyPay.saturdayPay * totalSaturdayHours
                    casSunPay = hourlyPay.sundayPay * totalSundayHours
                    publicHoliday.casTot = casWkPay + casSatPay + casSunPay + pubp
                    break
                        
                elif pubHol == "n":

                    while True:
                        try:
                            casHr = float(input("How many hours are you working during the week?"))
                            break
                        except ValueError:
                            print("Please enter your hours as a number!")

                    while True:
                        try:
                            totalSaturdayHours = float(input("How many hours are you working on saturday?"))
                            break
                        except ValueError:
                            print("Please enter your hours as a number!") 

                    while True:
                        try:
                            totalSundayHours = float(input("How many hours are you working on Sunday?"))
                            break
                        except ValueError:
                            print("Please enter your hours as a number!")

                    publicHoliday.totalWeekHrs = casHr + totalSaturdayHours + totalSundayHours 
                    casWkPay = rate.userPayrate * casHr
                    casSatPay = hourlyPay.saturdayPay * totalSaturdayHours
                    casSunPay = hourlyPay.sundayPay * totalSundayHours
                    publicHoliday.casTot = casWkPay + casSatPay + casSunPay
                    break
                    
                elif pubHol != "y" or "n":
                    pubHol = input("please answer y or n!")
                    continue

def calculateOvertime():
    #This function will take the users existing hours, and check if it is above 38. If the users hours are above 38, it will apply overtime rates to the exceeding amount.
    #If my hours arent above 38, it sets the pay function to be zero, which prevents the output of nothing from breaking the code.
    
    if calculatePay.casorcont == "y":
        while True:
            p = publicHoliday.totalWeekHrs - 38
            overrate = hourlyPay.casualPay * 0.25 + hourlyPay.casualPay * 2
            rr = ((hourlyPay.casualPay * 0.50 + hourlyPay.casualPay * 0.25 + hourlyPay.casualPay) * 3)

            if publicHoliday.totalWeekHrs > 38 and publicHoliday.totalWeekHrs < 42:
                calculateOvertime.pay = ((publicHoliday.totalWeekHrs - 38) * (hourlyPay.casualPay * 0.50 + hourlyPay.casualPay * 0.25 + hourlyPay.casualPay)) + publicHoliday.casTot - rate.userPayrate * p
                break

            elif publicHoliday.totalWeekHrs > 41:
                calculateOvertime.pay = (((publicHoliday.totalWeekHrs - 41) * overrate) + rr) + publicHoliday.casTot - rate.userPayrate * p  # sundayPay*3
                break

            else:
                calculateOvertime.pay = publicHoliday.casTot
                p = 0

                break
        else:
            calculateOvertime.pay = publicHoliday.casTot
            p = 0
    
    if calculatePay.casorcont == "n":
        while True:
            p = publicHoliday.totalWeekHrs - 38
            overrate = rate.userPayrate * 0.25 + rate.userPayrate * 2
            rr = ((rate.userPayrate * 0.50 + rate.userPayrate * 0.25 + rate.userPayrate) * 3)

            if publicHoliday.totalWeekHrs > 38 and publicHoliday.totalWeekHrs < 42:
                calculateOvertime.pay = ((publicHoliday.totalWeekHrs - 38) * (rate.userPayrate * 0.50 + rate.userPayrate * 0.25 + rate.userPayrate)) + publicHoliday.casTot - rate.userPayrate * p
                break

            elif publicHoliday.totalWeekHrs > 41:
                calculateOvertime.pay = (((publicHoliday.totalWeekHrs - 41) * rate.userPayrate) + rr) + publicHoliday.casTot - rate.userPayrate * p  # sundayPay*3
                break

            else:
                calculateOvertime.pay = publicHoliday.casTot
                p = 0
                break
        else:
            calculateOvertime.pay = publicHoliday.casTot
            p = 0

def incomeTax():
    incomeTax.yearPay = calculateOvertime.pay * wksInYear

    if incomeTax.yearPay <= 18200:
        incomeTax.tax = 0
    if incomeTax.yearPay <= 45000 and incomeTax.yearPay > 18200:
        incomeTax.tax = (incomeTax.yearPay - 18200) * 0.19
    if incomeTax.yearPay <= 120000 and incomeTax.yearPay >= 45000:
        incomeTax.tax = (incomeTax.yearPay - 45000) * 0.325 + 5092      
    if incomeTax.yearPay <= 180000 and incomeTax.yearPay > 120000:
        incomeTax.tax = (incomeTax.yearPay - 120000) * 0.37 + 29467      
    elif incomeTax.yearPay > 180000:
        incomeTax.tax = (incomeTax.yearPay - 180000) * 0.45 + 51667

def calculate_medicare_levy():
    medicare_levy = incomeTax.yearPay * 0.02
    return medicare_levy

def casFunc():

    rate()
    hourlyPay()
    publicHoliday()
    calculateOvertime()

    incomeTax()
    medicare_levy = calculate_medicare_levy()

    atax = (incomeTax.yearPay - incomeTax.tax) - medicare_levy
    wkatax = (atax / wksInYear) 

    print("You will earn $" + str(calculateOvertime.pay) + " this week, before tax.")
    print("You will earn $" + str(wkatax) + " this week, after tax.")
    print("On this payrate, you will earn $" + str(incomeTax.yearPay) + " a year, before tax.")
    print("On this payrate you will earn $" + str(atax) + " a year, after tax.")
    print("tax includes a medicare levy of $" + str(medicare_levy))

def contFunc():

    rate()
    hourlyPay()
    publicHoliday()
    calculateOvertime()

    incomeTax()
    medicare_levy = calculate_medicare_levy()

    atax = (incomeTax.yearPay - incomeTax.tax) - medicare_levy
    wkatax = (atax / wksInYear)

    print("You will earn $" + str(calculateOvertime.pay) + " this week, before tax.")
    print("You will earn $" + str(wkatax) + " this week, after tax.")
    print("On this payrate, you will earn $" + str(incomeTax.yearPay) + " a year, before tax.")
    print("On this payrate you will earn $" + str(atax) + " a year, after tax.")
    print("tax includes a medicare levy of $" + str(medicare_levy))
    
def calculatePay():  # This needs to be my main loop,,,,
    
    calculatePay.casorcont = input("are you casual? [Y/N]")
    calculatePay.casorcont = calculatePay.casorcont.lower()
    while True:
        if calculatePay.casorcont == "y":
            casFunc()
            break

        elif calculatePay.casorcont == "n":
            contFunc()
            break

        elif calculatePay.casorcont != "y" or "n":
            calculatePay.casorcont = (input("Please write Y or N!"))
            calculatePay.casorcont = calculatePay.casorcont.lower()
            continue

calculatePay()
