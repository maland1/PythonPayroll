from datetime import datetime as dTime


# function to print generic welcome message
def startMSG():
    print("\nWelcome to Soft Ireland software package.")


# function to print generic closing message
def endMSG():
    print("\nThank you for using Soft Ireland!")


def confirmation(filePath):
    print("\nData has been written to " + filePath)


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
            userInput = input("Please try again: ")


# function to validate integers
def validInt(userInput, maxVal=0):
    while True:
        try:
            # checks if maxval is less than the given input - which will then throw an error
            if int(userInput) < 1 or (0 < maxVal < int(userInput)):
                raise Exception
            else:
                return int(userInput)

        except:
            print("Invalid entry, please provide a valid integer.")
            userInput = input("Please try again: ")


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
            userInput = input("Please try again: ")


# validating date inputs in the correct format
def validDate(userInput):
    while True:
        try:
            # setting up the code to validate whether an input is in the correct format
            properDate = dTime.strptime(userInput, '%Y-%m-%d').date()
            return properDate

        except ValueError:
            print("Invalid date format. Enter in the format (YYYY-MM-DD).")
            userInput = input("Please try again: ")


def currentDate():
    date = dTime.today()
    return date