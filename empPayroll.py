# Wage Calculator App
# importing functions
import functions as fnc
# Numerical variables
rateOfTax = 0.15


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


# prints the values to console
def printWages(value):
    print("\nEmployee name: \t{}".format(value[0]))
    print("Hours worked: \t{}".format(value[1]))
    print("Rate of Pay: \t{:.2f}".format(value[2]))
    print("Rate of Tax: \t{:.0%}".format(rateOfTax))
    print("Gross Pay: \t\t{:.2f}".format(value[4]))
    print("Tax Paid: \t\t{:.2f}".format(value[5]))
    print("Bonus: \t\t\t{}".format(value[3]))
    print("Net Pay: \t\t{:.2f}".format(value[6]))


# calls the opening message function
fnc.startMSG()

# setting up list for print function
detailList = []
for i in range(5):  # loops through 5 times

    del detailList[:]  # clearing the list at the start of each loop

    print(f"\nEmployee {i + 1}")

    # getting inputs for name, hours and pay rate
    detailList.append(fnc.validString(input("Enter Employee Name: ")))
    detailList.append(fnc.validInt(input("Enter Hours Worked: ")))
    detailList.append(fnc.validFloat(input("Enter Rate of Pay: ")))

    detailList.append(bonusCheck(detailList[1]))
    detailList.append(grossCalcs(detailList[2], detailList[1]))
    detailList.append(taxCalcs(detailList[3], rateOfTax))
    detailList.append(netCalcs(detailList[4], detailList[5], detailList[3]))

    # passing the list to the print function
    printWages(detailList)

# calls the closing message function
fnc.endMSG()
