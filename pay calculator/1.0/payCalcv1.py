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
                saturdayPay = casualPay*0.50
                sundayPay = casualPay*0.50 + casualPay*0.25

                satCas = casualPay + saturdayPay 
                sunCas = casualPay + sundayPay 

                print("On Saturday you will earn " + str(satCas) + " per hour")
                print("On Sunday you will earn " + str(sunCas) + " per hour")

                casHr = float(input("How many hours are you working during the week?"))
                satCasHr = float(input("How many hours are you working on saturday?"))
                sunCasHr = float(input("How many hours are you working on Sunday?"))  
    
                casWkPay = casPay * casHr
                casSatPay = satCas * satCasHr
                casSunPay = sunCas * sunCasHr
    
                casTot = casWkPay + casSatPay + casSunPay

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
                    print("You will earn $" + str(tot) + "This week!")
                    loop = False
                    break
                except ValueError:
                    print("Please enter your payrate as a number.")
                    print()

    elif casorcont != "y" or "n":
            casorcont = (input("Please write Y or N!"))
            casorcont = casorcont.lower()
            continue
        

