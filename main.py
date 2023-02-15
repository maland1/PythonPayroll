# Numerical variables
rateOfTax = 0.15


def startMSG():
    print("\nWelcome to SI Payroll Software!")


def endMSG():
    print("\nThank you for using SI Payroll, have a nice day!")


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


# simple bonus calcs
def bonusCheck(hours):
    if hours > 50:
        return 100
    elif hours > 45:
        return 60
    elif hours > 40:
        return 50
    else:
        return 0


# simple calcs for gross pay
def grossCalcs(payRate, hours):
    return payRate * hours


# simple tax calcs
def taxCalcs(gross, taxRate):
    return gross * taxRate


# simple net pay calcs
def netCalcs(gross, tax, bonus):
    return (gross - tax) + bonus


def printWages(value):
    print("\nEmployee name: \t{}".format(value[0]))
    print("Hours worked: \t{}".format(value[1]))
    print("Rate of Pay: \t{:.2f}".format(value[2]))
    print("Rate of Tax: \t{:.0%}".format(rateOfTax))
    print("Gross Pay: \t\t{:.2f}".format(value[4]))
    print("Tax Paid: \t\t{:.2f}".format(value[5]))
    print("Bonus: \t\t\t{}".format(value[3]))
    print("Net Pay: \t\t{:.2f}".format(value[6]))


# prints opening message
startMSG()

for i in range(5):  # loops through 5 times
    # list includes every variable
    detailList = []

    print(f"\nEmployee {i + 1}")

    # getting inputs for name, hours and pay rate
    detailList.append(validString(input("Enter Employee Name: ")))
    detailList.append(validInt(input("Enter Hours Worked: ")))
    detailList.append(validFloat(input("Enter Rate of Pay: ")))

    detailList.append(bonusCheck(detailList[1]))
    detailList.append(grossCalcs(detailList[2], detailList[1]))
    detailList.append(taxCalcs(detailList[3], rateOfTax))
    detailList.append(netCalcs(detailList[4], detailList[5], detailList[3]))

    # passing the list to the print function
    printWages(detailList)

# prints closing message
endMSG()
