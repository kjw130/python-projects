wksInYear = 52

userPayrate = float(input("What is your payrate?"))

def hourlyPay():
    global saturdayPay
    global sundayPay
    global publicHol
    global yearPay
    global casualPay

    if casorcont == "y":
        casualPay = userPayrate / 1.25
        saturdayPay = casualPay * 0.50 + casualPay
        sundayPay = casualPay * 0.50 + casualPay * 0.25 + casualPay
        publicHol = userPayrate * 2
    
        print("On Saturday you will earn " + str(saturdayPay) + " per hour")
        print("On Sunday you will earn " + str(sundayPay) + " per hour")

    if casorcont == "n":
        saturdayPay = userPayrate * 0.25 + userPayrate
        sundayPay = userPayrate * 0.50 + userPayrate
        publicHol = userPayrate * 2
        
        print("On Saturday you will earn " + str(saturdayPay) + " per hour")
        print("On Sunday you will earn " + str(sundayPay) + " per hour")

def casFunc():
    global yearPay
    while True:
        try:
            hourlyPay()

            publicHoliday()

            calculateOvertime()

            yearPay = pay * wksInYear
            incomeTax()

            atax = (yearPay - tax) - medicareLevy
            print(atax)
            print(tax)
            wkatax = (atax / wksInYear) 

            print("You will earn $" + str(pay) + " this week, before tax.")
            print("You will earn $" + str(wkatax) + " this week, after tax.")
            print("On this payrate, you will earn $" + str(yearPay) + " a year, before tax.")
            print("On this payrate you will earn $" + str(atax) + " a year, after tax.")
            print("tax incldudes a medicare levy of $" + str(medicareLevy))
 
            break

        except ValueError:
            print("Please enter your payrate as a number.")
            print()

def contFunc():
    global yearPay
    while True:
        try:
            # Math to calculate hourly pay.
            hourlyPay()

            publicHoliday()

            calculateOvertime()

            yearPay = pay * wksInYear

            incomeTax()

            atax = (yearPay - tax) - medicareLevy
            print(tax)
            wkatax = (atax / wksInYear)

            print("You will earn $" + str(pay) + " this week, before tax.")
            print("You will earn $" + str(wkatax) + " this week, after tax.")
            print("On this payrate, you will earn $" + str(yearPay) + " a year, before tax.")
            print("On this payrate you will earn $" + str(atax) + " a year, after tax.")
            print("tax incldudes a medicare levy of $" + str(medicareLevy))

            break

        except ValueError:
            print("Please enter your payrate as a number.")
            print()

def publicHoliday():
    global pubp
    global totalWeekHrs
    global casHr
    global totalSaturdayHours
    global totalSundayHours
    global casTot
    if casorcont == "y":
        while True:
            try:
                pubHol = input("Are you working on a public holiday this week? [Y/N]")
                pubHol = pubHol.lower()
                if pubHol == "y":

                    pub = float(input("How many hours of public holiday time?"))
                    casHr = float(input("How many hours are you working during the week?"))
                    totalSaturdayHours = float(input("How many hours are you working on saturday?"))
                    totalSundayHours = float(input("How many hours are you working on Sunday?"))
                    pubp = pub * publicHol
                    totalWeekHrs = casHr + totalSaturdayHours + totalSundayHours + pub

                    casWkPay = userPayrate * casHr
                    casSatPay = saturdayPay * totalSaturdayHours
                    casSunPay = sundayPay * totalSundayHours
                    casTot = casWkPay + casSatPay + casSunPay + pubp
                    break
                elif pubHol == "n":
                    casHr = float(input("How many hours are you working during the week?"))
                    totalSaturdayHours = float(input("How many hours are you working on saturday?"))
                    totalSundayHours = float(input("How many hours are you working on Sunday?"))
                    totalWeekHrs = casHr + totalSaturdayHours + totalSundayHours
                    casWkPay = userPayrate * casHr
                    casSatPay = saturdayPay * totalSaturdayHours
                    casSunPay = sundayPay * totalSundayHours
                    casTot = casWkPay + casSatPay + casSunPay
                    break
            except ValueError:
                print("please answer y or n!")

    elif casorcont == "n":
        while True:
            try:
                pubHol = input("Are you working on a public holiday this week? [Y/N]")
                pubHol = pubHol.lower()
                if pubHol == "y":
                    pub = float(input("How many hours of public holiday time?"))
                    casHr = float(input("How many hours are you working during the week?"))
                    totalSaturdayHours = float(input("How many hours are you working on saturday?"))
                    totalSundayHours = float(input("How many hours are you working on Sunday?"))
                    pubp = pub * publicHol
                    totalWeekHrs = casHr + totalSaturdayHours + totalSundayHours + pub
                    casWkPay = userPayrate * casHr
                    casSatPay = saturdayPay * totalSaturdayHours
                    casSunPay = sundayPay * totalSundayHours
                    casTot = casWkPay + casSatPay + casSunPay + pubp
                    print(casTot)
                    break
                elif pubHol == "n":
                    
                    casHr = float(input("How many hours are you working during the week?"))
                    totalSaturdayHours = float(input("How many hours are you working on saturday?"))
                    totalSundayHours = float(input("How many hours are you working on Sunday?"))

                    totalWeekHrs = casHr + totalSaturdayHours + totalSundayHours 
                    casWkPay = userPayrate * casHr
                    casSatPay = saturdayPay * totalSaturdayHours
                    casSunPay = sundayPay * totalSundayHours
                    casTot = casWkPay + casSatPay + casSunPay
                    print(casTot)
                    break

            except ValueError:
                print("please answer y or n!")

def calculateOvertime():
    global pay
    global p
    if casorcont == "y":
        while True:
            p = totalWeekHrs - 38
            overrate = casualPay * 0.25 + casualPay * 2
            rr = ((casualPay * 0.50 + casualPay * 0.25 + casualPay) * 3)

            if totalWeekHrs > 38 and totalWeekHrs < 42:
                pay = ((totalWeekHrs - 38) * (casualPay * 0.50 + casualPay * 0.25 + casualPay)) + casTot - userPayrate * p
                break

            elif totalWeekHrs > 41:
                pay = (((totalWeekHrs - 41) * overrate) + rr) + casTot - userPayrate * p  # sundayPay*3
                break

            else:
                pay = casTot
                p = 0

                break
        else:
            pay = casTot
            p = 0
    
    if casorcont == "n":
        while True:
            p = totalWeekHrs - 38
            overrate = userPayrate * 0.25 + userPayrate * 2
            rr = ((userPayrate * 0.50 + userPayrate * 0.25 + userPayrate) * 3)

            if totalWeekHrs > 38 and totalWeekHrs < 42:
                pay = ((totalWeekHrs - 38) * (userPayrate * 0.50 + userPayrate * 0.25 + userPayrate)) + casTot - userPayrate * p
                break

            elif totalWeekHrs > 41:
                pay = (((totalWeekHrs - 41) * userPayrate) + rr) + casTot - userPayrate * p  # sundayPay*3
                break

            else:
                pay = casTot
                p = 0

                break
        else:
            pay = casTot
            p = 0   

def incomeTax():
    global medicareLevy
    global tax
    medicareLevy = yearPay * 0.02
    if yearPay <= 18200:
        tax = 0
    if yearPay <= 45000 and yearPay > 18200:
        tax = (yearPay - 18200) * 0.19
    if yearPay <= 120000 and yearPay >= 45000:
        tax = (yearPay - 45000) * 0.325 + 5092      
    if yearPay <= 180000 and yearPay > 120000:
        tax = (yearPay - 120000) * 0.37 + 29467      
    elif yearPay > 180000:
        tax = (yearPay - 180000) * 0.45 + 51667
        
def calculatePay(): 
    global casorcont
    casorcont = input("are you casual? [Y/N]")
    casorcont = casorcont.lower()
    loop = True
    while loop == True:
        if casorcont == "y":
            casFunc()
            loop = False

        elif casorcont == "n":
            contFunc()
            loop = False

        elif casorcont != "y" or "n":
            casorcont = (input("Please write Y or N!"))
            casorcont = casorcont.lower()
            continue

calculatePay()
