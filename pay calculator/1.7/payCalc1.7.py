wksInYear = 52

def rate():
    while True:
        try:
            print("What is your payrate?")
            rate.userPayrate = float(input("> "))
            split()
            break
        except ValueError:
            print("Please enter your payrate as a number!")


def split():
    if calculatePay.casorcont == "y":
        split.hourlyRate = rate.userPayrate / 1.25

    if calculatePay.casorcont == "n":
        split.hourlyRate = rate.userPayrate


def hourlyPay():
    if calculatePay.casorcont == "y":

        hourlyPay.saturdayPay = split.hourlyRate * 0.50 + split.hourlyRate
        hourlyPay.sundayPay = split.hourlyRate * 0.50 + split.hourlyRate * 0.25 + split.hourlyRate

    elif calculatePay.casorcont == "n":

        hourlyPay.saturdayPay = rate.userPayrate * 0.25 + rate.userPayrate
        hourlyPay.sundayPay = rate.userPayrate * 0.50 + rate.userPayrate

    print(f"On Saturday you will earn{hourlyPay.saturdayPay} per hour")
    print(f"On Sunday you will earn{hourlyPay.sundayPay} per hour")


def publicHoliday():
    print("Are you working on a public holiday this week? [Y/N]")
    publicHoliday.pubHol = input("> ")
    publicHoliday.pubHol = publicHoliday.pubHol.lower()

    while True:
        if publicHoliday.pubHol == "y":
            print("How many hours of public holiday time?")
            
            while True:
                try:

                    publicHoliday.pub = float(input("> "))
                    break

                except ValueError:
                    print("Please enter your hours as a number!")

        elif publicHoliday.pubHol == "n":
            break

        elif publicHoliday.pubHol != "y" or publicHoliday.pubHol != "n":
            print("Please answer y or n!")
            publicHoliday.pubHol = input("> ")
            publicHoliday.pubHol = publicHoliday.pubHol.lower()
            continue

        break


def askUserTheirHours():

    print("How many hours are you working during the week?")
    while True:
        try:
            askUserTheirHours.casHr = float(input("> "))
            break
        except ValueError:
            print("Please enter your hours as a number!")

    print("How many hours are you working on saturday?")
    while True:
        try:
            askUserTheirHours.totalSaturdayHours = float(input("> "))
            break
        except ValueError:
            print("Please enter your hours as a number!")

    print("How many hours are you working on Sunday?")
    while True:
        try:
            askUserTheirHours.totalSundayHours = float(input("> "))
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
    weekPay = (rate.userPayrate * askUserTheirHours.casHr) + (
            hourlyPay.saturdayPay * askUserTheirHours.totalSaturdayHours) + (
                      hourlyPay.sundayPay * askUserTheirHours.totalSundayHours)

    calculations.casTot = weekPay + pubp


def calculateOvertime():
    p = calculations.totalWeekHrs - 38

    if calculatePay.casorcont == "y":
        calcTheOtRate = split.hourlyRate * 0.50 + split.hourlyRate * 0.25 + split.hourlyRate
        setRateforWhenUserIsDoingOver41Hrs = (
                (split.hourlyRate * 0.50 + split.hourlyRate * 0.25 + split.hourlyRate) * 3)
        over41hoursrate = split.hourlyRate * 0.25 + split.hourlyRate * 2

    if calculatePay.casorcont == "n":
        calcTheOtRate = split.hourlyRate * 0.50 + split.hourlyRate
        setRateforWhenUserIsDoingOver41Hrs = ((split.hourlyRate * 0.50 + split.hourlyRate) * 3)
        over41hoursrate = split.hourlyRate * 2

    if calculations.totalWeekHrs >= 38:

        while True:
            
            if 38 < calculations.totalWeekHrs <= 41:
                calculateOvertime.pay = ((calculations.totalWeekHrs - 38) * (calcTheOtRate
                )) + calculations.casTot - rate.userPayrate * p
                break

            elif calculations.totalWeekHrs >= 42:

                calculateOvertime.pay = (((calculations.totalWeekHrs - 41) * 
                    over41hoursrate) + setRateforWhenUserIsDoingOver41Hrs) + calculations.casTot - rate.userPayrate * p
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

    elif 18200 < incomeTax.yearPay <= 45000:
        incomeTax.tax = (incomeTax.yearPay - 18200) * 0.19

    elif 45000 <= incomeTax.yearPay <= 120000:
        incomeTax.tax = (incomeTax.yearPay - 45000) * 0.325 + 5092

    elif 120000 < incomeTax.yearPay <= 180000:
        incomeTax.tax = (incomeTax.yearPay - 120000) * 0.37 + 29467

    elif incomeTax.yearPay > 180000:
        incomeTax.tax = (incomeTax.yearPay - 180000) * 0.45 + 51667


def lowTaxOffSet():
    if incomeTax.yearPay <= 18200:
        lowOffSet = 0

    elif 18200 < incomeTax.yearPay <= 37500:
        if incomeTax.tax >= 700:
            lowOffSet = 700
        # This is because the tax paid cannot be less than zero If the user is only paying $200 in tax, they can only
        # get a maximum of $200 tax offset, rather than the set $700
        elif incomeTax.tax <= 700:
            lowOffSet = incomeTax.tax

    elif 37501 <= incomeTax.yearPay <= 45000:
        lowOffSet = 700 - ((incomeTax.yearPay - 37500) * 0.05)

    elif 45001 <= incomeTax.yearPay <= 66667:
        lowOffSet = 325 - ((incomeTax.yearPay - 45000) * 0.015)

    elif incomeTax.yearPay >= 66668:
        lowOffSet = 0
        
    return lowOffSet


def middleTaxOffSet():
    if incomeTax.yearPay <= 18200:
        middleOffSet = 0

    elif 18200 < incomeTax.yearPay <= 37000:
        if incomeTax.tax <= 700:
            middleOffSet = 0

        elif 700 < incomeTax.tax < 955:
            middleOffSet = incomeTax.tax - 700

        elif incomeTax.tax >= 955:
            middleOffSet = 255

    elif 37001 <= incomeTax.yearPay <= 48000:
        middleOffSet = 255 + ((incomeTax.yearPay - 37000) * 0.075)

    elif 48001 <= incomeTax.yearPay <= 90000:
        middleOffSet = 1080

    elif 90001 <= incomeTax.yearPay <= 126000:
        middleOffSet = 1080 - ((incomeTax.yearPay - 90001) * 0.03)

    elif incomeTax.yearPay >= 126000:
        middleOffSet = 0

    return middleOffSet


def taxOffSet():
    lowOffSet = lowTaxOffSet()
    middleOffSet = middleTaxOffSet()
    totalOffSet = lowOffSet + middleOffSet

    return totalOffSet


def calculate_medicare_levy():
    if incomeTax.yearPay >= 28501:
        medicare_levy = incomeTax.yearPay * 0.02
    elif incomeTax.yearPay <= 28500:
        medicare_levy = 0

    return medicare_levy


def calculatePay():
    print(("are you casual? [Y/N]"))
    calculatePay.casorcont = input("> ")
    calculatePay.casorcont = calculatePay.casorcont.lower()

    while True:
        if calculatePay.casorcont == "y" or calculatePay.casorcont == "n":
            break

        elif calculatePay.casorcont != "y" or calculatePay.casorcont != "n":
            calculatePay.casorcont = (input("Please write Y or N!"))
            calculatePay.casorcont = calculatePay.casorcont.lower()
            continue


def results():
    totalOffSet = taxOffSet()
    medicare_levy = calculate_medicare_levy()

    taxAfterOffSet = incomeTax.tax - totalOffSet
    atax = (incomeTax.yearPay - taxAfterOffSet) - medicare_levy
    wkatax = (atax / wksInYear)

    print(f"You will earn ${calculateOvertime.pay} this week, before tax.")
    print(f"You will earn $ {wkatax} this week, after tax.")
    print(f"On this payrate, you will earn ${incomeTax.yearPay} a year, before tax.")
    print(f"On this payrate you will earn ${atax} a year, after tax.")
    print(f"This calculation includes a medicare levy of ${medicare_levy}, and a tax offset of ${totalOffSet}")
    

def mainFunc():

    calculatePay()

    rate()

    hourlyPay()

    publicHoliday()

    askUserTheirHours()

    calculations()

    calculateOvertime()

    incomeTax()

    results()


mainFunc()