import random
CorrectBokningsId = "admin"
CorrectPassword = "admin"


class User:
    def __init__(self, namn, password, age, email):
        self.__boknings_id = str(random.randint(100, 999))
        self.__password = password
        self.namn = namn
        self.age = age
        self.email = email

    def getboknings_id(self):
        return self.__boknings_id

    def setboknings_id(self,boknings_id):
        self.__boknings_id = boknings_id

    def getpassword(self):
        return self.__password

    def setpassword(self,password):
        self.__password = password

    def __str__(self):
        return self.__boknings_id + ", " + self.__password + ", " + self.namn + ", " + self.email

userlist = []

# Metoden används för inloggningen av låntagare kollar igenom listan av användare
def checkUser(u, p):
    for x in userlist:
         if (x.getboknings_id().upper() == u.upper()) and (x.getpassword().upper() == p.upper()):
            return True
    return False

while True:
    boknings_id = input("Ange ditt Boknings-ID: ")
    password    = input("Ange ditt lösenord: ")

    if (boknings_id.upper() == CorrectBokningsId.upper()) and (password.upper() == CorrectPassword.upper()):

        print("Välkommen " + boknings_id)

        Adminloopen = True

        while Adminloopen == True:

            huvudadminmenu = "Menysystemet för admin\n" \
                             "1 - Skapa ny användare\n" \
                             "2 - Radera användare\n" \
                             "3 - Lista användare\n" \
                             "Svar: "

            val = int(input(huvudadminmenu))

            if (val ==1):

                konto = User(input("Skriv in ditt namn: "), input("Skriv in önskat lösenord: "), input("Ange din ålder: "), input("Ange din epost: "))

                userlist.append(konto)

                menustr =   "Ett nytt konto är nu skapat med namnet : " + konto.namn +  "\n" \
                            "\o/ Välkommen till Bokningen \o/\n" \
                            "Ditt bokningsnummer är: " + konto.getboknings_id() + "\n" \
                            "Ditt lösenord är: " + konto.getpassword() + "\n";

                print(menustr)

            elif (val == 2):
                radera = input("Ange den användare som ska raderas. Ange dess användarID : ")
                for x in userlist:
                    if (x.getboknings_id() == radera):
                        userlist.remove(x)
            elif (val == 3):
                for x in userlist:
                    print(x)



    elif (checkUser(boknings_id, password)):
        while True:
            print("visa menysystemet låntagaren")
            # .... Visa meny för specifikt för låntagaren här ...
    else:
        print("Ditt bokningsnummer eller lösenord är felaktigt")
