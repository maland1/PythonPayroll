# function to print generic welcome message
def startMSG():
    print("\nWelcome to Soft Ireland software package.")


# function to print generic closing message
def endMSG():
    print("\nThank you for using Soft Ireland!")


# function to validate strings
def validString(userInput):
    while True:
        try:
            if userInput != "":
                return userInput
            else:
                raise Exception
        except:
            print("Invalid entry, please enter a valid string.")


# function to validate integers
def validInt(userInput):
    while True:
        try:
            if int(userInput) < 1:
                raise Exception
            else:
                return int(userInput)
        except:
            print("Invalid entry, please provide a valid integer.")


# function to validate floats
def validFloat(userInput):
    while True:
        try:
            if float(userInput) < 1:
                raise Exception
            else:
                return float(userInput)
        except:
            print("Invalid entry, please provide a valid float.")
