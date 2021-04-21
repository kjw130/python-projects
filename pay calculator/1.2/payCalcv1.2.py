
def calculatePay():   
    global casPay
    global saturdayPay
    global sundayPay
    global publicHol
    global yearPay

    casorcont = input("are you casual? [Y/N]")
    casorcont = casorcont.lower()
    loop = True
    while loop == True:
        if casorcont == "y":
            
            while True:
                try:
                    casPay = float(input("What is your payrate?"))

                    #Math to calculate hourly pay.
                    casualPay = casPay/1.25
                    saturdayPay = casualPay*0.50 + casualPay
                    sundayPay = casualPay*0.50 + casualPay*0.25 + casualPay
                    publicHol = casPay*2

    
                    print("On Saturday you will earn " + str(saturdayPay) + " per hour")
                    print("On Sunday you will earn " + str(sundayPay) + " per hour")
                    
                    # Ask user if they are working on a public holiday.

                    def publicHoliday():
                        global totalWeekHrs
                        global casHr
                        global satCasHr
                        global sunCasHr
                        global casTot
                        while True:
                            try:
                                pubHol = input("Are you working on a public holiday this week? [Y/N]")
                                pubHol = pubHol.lower()
                                if pubHol == "y": 
                                    global pubp
                                    pub = float(input("How many hours of public holiday time?"))
                                    casHr = float(input("How many hours are you working during the week?"))
                                    satCasHr = float(input("How many hours are you working on saturday?"))
                                    sunCasHr = float(input("How many hours are you working on Sunday?"))
                                    pubp = pub*publicHol
                                                        
                                    totalWeekHrs = casHr + satCasHr + sunCasHr 
                                    casWkPay = casPay * casHr
                                    casSatPay = saturdayPay * satCasHr
                                    casSunPay = sundayPay * sunCasHr 
                                    casTot = casWkPay + casSatPay + casSunPay + pubp
                                    break
                                elif pubHol == "n":
                                    casHr = float(input("How many hours are you working during the week?"))
                                    satCasHr = float(input("How many hours are you working on saturday?"))
                                    sunCasHr = float(input("How many hours are you working on Sunday?"))
                                    totalWeekHrs = casHr + satCasHr + sunCasHr
                                    casWkPay = casPay * casHr
                                    casSatPay = saturdayPay * satCasHr
                                    casSunPay = sundayPay * sunCasHr 
                                    casTot = casWkPay + casSatPay + casSunPay 
                                    break
                            except ValueError:
                                print("please answer y or n!")

                    publicHoliday()

                    #This function calculates overtime, if the user is working over 38 hours.
                    
                    def calculateOvertime():
                        global pay
                                           
                        global p
                        while True:
                            try:
                                p = totalWeekHrs - 38
                                casOverrate = casualPay*0.25+casualPay*2
                                rr = ((casualPay*0.50 + casualPay*0.25 + casualPay)*3)

                                if totalWeekHrs > 38 and totalWeekHrs < 42:
                                    pay = ((totalWeekHrs-38)*(casualPay*0.50 + casualPay*0.25 + casualPay)) + casTot-casPay*p
                                    break
                                                                            
                                elif totalWeekHrs > 41: 
                                    pay = ((totalWeekHrs-41)*casOverrate)+ rr#sundayPay*3
                                    break
                                                    
                                else:
                                    pay = 0
                                    p = 0 
                                    break
                            except:
                                break

                    calculateOvertime()

                    cwk = casTot - casPay*p 
                    ypay = cwk + pay

                    yearPay = ypay*52

                    def incomeTax():
                        global tax
                        if yearPay <= 18200:
                            tax = 0
                        if yearPay <= 45000:
                            tax = (yearPay - 18200)*0.19 
                        if yearPay <= 120000:
                            tax = (yearPay - 45000)*0.325 + 5092
                                    

                    incomeTax()

                    atax = (yearPay - tax)
                    wkatax = (atax/52)

                    print("You will earn $" + str(ypay) + " this week, before tax.")
                    print("You will earn $" + str(wkatax) + " this week, after tax.")
                    print("On this payrate, you will earn $" + str(yearPay) + " a year, before tax.")
                    print("On this payrate you will earn $" + str(atax) + " a year, after tax.")

                    loop = False
                    break
                    
                except ValueError:
                    print("Please enter your payrate as a number.")
                    print()

        elif casorcont == "n":

            while True:
                try:
                    normalPay = float(input("What is your payrate? ")) 
                    
                    satMult = normalPay*0.25
                    sunMult = normalPay*0.50 

                    sat = normalPay + satMult
                    sun = normalPay + sunMult

                    print("On Saturday you will earn " + str(sat) + " per hour")
                    print("On Sunday you will earn " + str(sun) + " per hour")

                    Hr = float(input("How many hours are you working during the week?"))
                    satHr = float(input("How many hours are you working on saturday?"))
                    sunHr = float(input("How many hours are you working on Sunday?"))  
        
                    wkPay = Hr * normalPay
                    satPay = satHr * sat
                    sunPay = sunHr * sun

                    tot = wkPay + satPay + sunPay
                    yearPay = tot*52
        
                    atax = (yearPay - incomeTax(yearPay))
                    wkatax = (atax/52)
                    print(atax)
                    print(wkatax)

                    print("You will earn $" + str(tot) + " this week, before tax.")
                    print("You will earn $" + str(wkatax) + " this week, after tax.")
                    print("On this payrate, you will earn $" + str(yearPay) + " a year, before tax.")
                    print("On this payrate you will earn $" + str(atax) + " a year, after tax.")

                    loop = False
                    break
                except ValueError:
                    print("Please enter your payrate as a number.")
                    print()

        elif casorcont != "y" or "n":
            casorcont = (input("Please write Y or N!"))
            casorcont = casorcont.lower()
            continue

calculatePay()