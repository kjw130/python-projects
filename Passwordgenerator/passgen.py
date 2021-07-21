import random

class Characters:
    def __init__(self):
        self.characterslist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10']

        self.special_characters = ['!', '@', '#', '$']


class Password:
    def __init__(self, length, specialchars):
        self.length = length
        self.specialchars = specialchars
        self.characters = Characters()
    
    def generate(self):
        random_max = len(self.characters.characterslist)
        if self.specialchars == "y":
            self.characters.characterslist.extend(self.characters.special_characters)
            random_max += len(self.characters.special_characters)
        
        password = ''
        for x in range(self.length):
            rand_number = random.randint(1,(random_max))
            password = password + self.characters.characterslist[rand_number]
            
        return password
        

class PassGen:
    def __init__(self):
        self.main()

    def y_n(self):
        while True:
            y_or_n = input("[Y|N] >")
            y_or_n = y_or_n.lower()

            if y_or_n == "y" or y_or_n == "n":
                return y_or_n
            else:
                continue

    def getlength(self):
        while True:
            print("What do you want the length of the password to be?")
            length = input("> ")

            try:
                int(length)
                length = int(length)
            except:
                print("Please enter as a number!")
                continue

            return length
        

    def main(self):
        while True:
            length = self.getlength()

            print("Do you want special characters in your password? For example: [!|@|#|$]")
            specialchars = self.y_n()

            genpassword = Password(length, specialchars)
            password = genpassword.generate()

            print(f"Your password is: {password}")
            print("Generate another password?")
            genanother = self.y_n()
            if genanother == "y":
                continue
            else:
                break


PassGen()