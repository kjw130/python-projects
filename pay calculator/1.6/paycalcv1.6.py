wksInYear = 52

def rate():
    while True:
        try:
            rate.userPayrate = float(input("What is your payrate?"))
            split()
            break
        except ValueError:
            print("Please enter your payrate as a number!")

def split():

    if calculatePay.casorcont == "y":
        split.hourlyRate = rate.userPayrate/1.25

    if calculatePay.casorcont == "n":
        split.hourlyRate = rate.userPayrate

def hourlyPay():
    if calculatePay.casorcont == "y":

        split.hourlyRate = rate.userPayrate / 1.25
        hourlyPay.saturdayPay = split.hourlyRate * 0.50 + split.hourlyRate
        hourlyPay.sundayPay = split.hourlyRate * 0.50 + split.hourlyRate * 0.25 + split.hourlyRate
        
        print("On Saturday you will earn " + str(hourlyPay.saturdayPay) + " per hour")
        print("On Sunday you will earn " + str(hourlyPay.sundayPay) + " per hour")
    
    elif calculatePay.casorcont == "n":

        hourlyPay.saturdayPay = rate.userPayrate * 0.25 + rate.userPayrate
        hourlyPay.sundayPay = rate.userPayrate * 0.50 + rate.userPayrate
        
        print("On Saturday you will earn " + str(hourlyPay.saturdayPay) + " per hour")
        print("On Sunday you will earn " + str(hourlyPay.sundayPay) + " per hour")

def publicHoliday():
    
        publicHoliday.pubHol = input("Are you working on a public holiday this week? [Y/N]")
        publicHoliday.pubHol = publicHoliday.pubHol.lower()

        while True:
            if publicHoliday.pubHol == "y":
                while True:
                    try:
                        publicHoliday.pub = float(input("How many hours of public holiday time?"))
                        break
                    except ValueError:
                        print("Please enter your hours as a number!")
            elif publicHoliday.pubHol == "n":
                break

            elif publicHoliday.pubHol != "y" or publicHoliday.pubHol != "n":
                publicHoliday.pubHol = input("please answer y or n!")
                publicHoliday.pubHol = publicHoliday.pubHol.lower()
                continue  
            
            break

def askUserTheirHours():
    while True:
        try:
            askUserTheirHours.casHr = float(input("How many hours are you working during the week?"))
            break
        except ValueError:
            print("Please enter your hours as a number!")

    while True:
        try:
            askUserTheirHours.totalSaturdayHours = float(input("How many hours are you working on saturday?"))
            break
        except ValueError:
            print("Please enter your hours as a number!")

    while True:
        try:
            askUserTheirHours.totalSundayHours = float(input("How many hours are you working on Sunday?"))
            break
        except ValueError:
            print("Please enter your hours as a number!")

def calculations():
    calculations.publicHol = rate.userPayrate * 2

    if publicHoliday.pubHol == "y":

        pubp = publicHoliday.pub * calculations.publicHol

    elif publicHoliday.pubHol == "n":
        pubp = 0
        publicHoliday.pub = 0 
    
    calculations.totalWeekHrs = askUserTheirHours.casHr + askUserTheirHours.totalSaturdayHours + askUserTheirHours.totalSundayHours + publicHoliday.pub
    weekPay = (rate.userPayrate * askUserTheirHours.casHr) + (hourlyPay.saturdayPay * askUserTheirHours.totalSaturdayHours) + (hourlyPay.sundayPay * askUserTheirHours.totalSundayHours)

    calculations.casTot = weekPay + pubp
        
def calculateOvertime():
    #This function will take the users existing hours, and check if it is above 38. If the users hours are above 38, it will apply overtime rates to the exceeding amount.
    #If my hours arent above 38, it sets the pay function to be zero, which prevents the output of nothing from breaking the code.
  
    p = calculations.totalWeekHrs - 38

    if calculatePay.casorcont == "y":
        calcTheOtRate = split.hourlyRate * 0.50 + split.hourlyRate * 0.25 + split.hourlyRate
        setRateforWhenUserIsDoingOver41Hrs = ((split.hourlyRate * 0.50 + split.hourlyRate * 0.25 + split.hourlyRate) * 3)
        over41hoursrate = split.hourlyRate * 0.25 + split.hourlyRate * 2

    if calculatePay.casorcont == "n":
        calcTheOtRate = split.hourlyRate * 0.50 + split.hourlyRate
        setRateforWhenUserIsDoingOver41Hrs = ((split.hourlyRate * 0.50 + split.hourlyRate) * 3)
        over41hoursrate = split.hourlyRate * 2

    if calculations.totalWeekHrs >= 38:
        while True:
    
            if calculations.totalWeekHrs > 38 and calculations.totalWeekHrs <= 41:
                calculateOvertime.pay = ((calculations.totalWeekHrs - 38) * (calcTheOtRate)) + calculations.casTot - rate.userPayrate * p
                break

            elif calculations.totalWeekHrs >= 42:

                calculateOvertime.pay = (((calculations.totalWeekHrs - 41) * over41hoursrate) + setRateforWhenUserIsDoingOver41Hrs) + calculations.casTot - rate.userPayrate * p 
                break

            else:
                calculateOvertime.pay = calculations.casTot
                p = 0
                break
    else:
        calculateOvertime.pay = calculations.casTot
        p = 0

def incomeTax():
    incomeTax.yearPay = calculateOvertime.pay * wksInYear

    if incomeTax.yearPay <= 18200:
        incomeTax.tax = 0
    elif incomeTax.yearPay > 18200 and incomeTax.yearPay <= 45000:
        incomeTax.tax = (incomeTax.yearPay - 18200) * 0.19
    elif incomeTax.yearPay  >= 45000 and incomeTax.yearPay <= 120000:
        incomeTax.tax = (incomeTax.yearPay - 45000) * 0.325 + 5092      
    elif incomeTax.yearPay > 120000 and incomeTax.yearPay <= 180000:
        incomeTax.tax = (incomeTax.yearPay - 120000) * 0.37 + 29467      
    elif incomeTax.yearPay > 180000:
        incomeTax.tax = (incomeTax.yearPay - 180000) * 0.45 + 51667

def lowTaxOffSet():
    if incomeTax.yearPay <= 18200:
        lowTaxOffSet.lowOffSet = 0

    elif incomeTax.yearPay > 18200 and incomeTax.yearPay <= 37500:
        if incomeTax.tax >= 700:
            lowTaxOffSet.lowOffSet = 700

        #This is because the tax paid cannot be less than zero
        #If the user is only paying $200 in tax, they can only get a maximum of $200 tax offset, rather than the set $700
        elif incomeTax.tax <= 700:
            lowTaxOffSet.lowOffSet = incomeTax.tax 
            
    elif incomeTax.yearPay >= 37501 and incomeTax.yearPay <= 45000:
        lowTaxOffSet.lowOffSet = 700 - ((incomeTax.yearPay - 37500)*0.05)
    elif incomeTax.yearPay >= 45001 and incomeTax.yearPay <= 66667:
        lowTaxOffSet.lowOffSet = 325 - ((incomeTax.yearPay - 45000)*0.015)
    elif incomeTax.yearPay >= 66668:
        lowTaxOffSet.lowOffSet = 0

def middleTaxOffSet():
    if incomeTax.yearPay <= 18200:
        middleTaxOffSet.middleOffSet = 0
        
    elif incomeTax.yearPay > 18200 and incomeTax.yearPay <= 37000:
        if incomeTax.tax <= 700:
            middleTaxOffSet.middleOffSet = 0

        elif incomeTax.tax > 700 and incomeTax.tax < 955:
            middleTaxOffSet.middleOffSet = incomeTax.tax - 700

        elif incomeTax.tax >= 955:
            middleTaxOffSet.middleOffSet = 255

    elif incomeTax.yearPay >= 37001 and incomeTax.yearPay <= 48000:
        middleTaxOffSet.middleOffSet = 255 + ((incomeTax.yearPay-37000)* 0.075)
    elif incomeTax.yearPay >= 48001 and incomeTax.yearPay <= 90000:
        middleTaxOffSet.middleOffSet = 1080
    elif incomeTax.yearPay >= 90001 and incomeTax.yearPay <= 126000:
        middleTaxOffSet.middleOffSet = 1080 - ((incomeTax.yearPay - 90001)*0.03)
    elif incomeTax.yearPay >= 126000:
        middleTaxOffSet.middleOffSet = 0 
    
def taxOffSet():
    lowTaxOffSet()
    middleTaxOffSet()
    taxOffSet.totalOffSet = lowTaxOffSet.lowOffSet + middleTaxOffSet.middleOffSet
    
def calculate_medicare_levy():
    if incomeTax.yearPay >= 28501:
        calculate_medicare_levy.medicare_levy = incomeTax.yearPay * 0.02
    elif incomeTax.yearPay <= 28500:
        calculate_medicare_levy.medicare_levy = 0
    
def mainFunc():

    rate()

    hourlyPay()

    publicHoliday()

    askUserTheirHours()

    calculations()

    calculateOvertime()

    incomeTax()

    calculate_medicare_levy()

    taxOffSet()

    
    taxAfterOffSet = incomeTax.tax - taxOffSet.totalOffSet 
    atax = (incomeTax.yearPay - taxAfterOffSet) - calculate_medicare_levy.medicare_levy
    wkatax = (atax / wksInYear) 
    
    print("You will earn $" + str(calculateOvertime.pay) + " this week, before tax.")
    print("You will earn $" + str(wkatax) + " this week, after tax.")
    print("On this payrate, you will earn $" + str(incomeTax.yearPay) + " a year, before tax.")
    print("On this payrate you will earn $" + str(atax) + " a year, after tax.")
    print("tax includes a medicare levy of $" + str(calculate_medicare_levy.medicare_levy))
    print("this calculation also includes tax offsets of $" + str(lowTaxOffSet.lowOffSet) + " for low income")
    print("and an offset of $" + str(middleTaxOffSet.middleOffSet) + " for low/middle income")
    
def calculatePay(): 
    
    calculatePay.casorcont = input("are you casual? [Y/N]")
    calculatePay.casorcont = calculatePay.casorcont.lower()

    while True:
        if calculatePay.casorcont == "y" or calculatePay.casorcont == "n":           
            break

        elif calculatePay.casorcont != "y" or calculatePay.casorcont != "n":
            calculatePay.casorcont = (input("Please write Y or N!"))
            calculatePay.casorcont = calculatePay.casorcont.lower()
            continue

    mainFunc()
    
calculatePay()