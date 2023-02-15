
def validString(userInput):
    while True:
        try:
            if userInput != "":
                return userInput
            else:
                raise Exception
        except:
            print("Invalid entry, please enter a valid string.")


def validInt(userInput):
    while True:
        try:
            if int(userInput) < 1:
                raise Exception
            else:
                return int(userInput)
        except:
            print("Invalid entry, please provide a valid integer.")


def validFloat(userInput):
    while True:
        try:
            if float(userInput) < 1:
                raise Exception
            else:
                return float(userInput)
        except:
            print("Invalid entry, please provide a valid float.")
