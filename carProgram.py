# importing generic functions from file
import functions as fnc

# set variables
delivCharge = 0.05
filePath = "C:\\temp\\Opel.txt"
# setting up list for print function
opelList = []


# does the delivery cost calcs
def deliveryCalcs(cost, delivery):
    return cost * delivery


# does the profit calcs
def profitCalcs(cost, profitMarg):
    return cost * (profitMarg/100)


# does the sales cost calcs
def salesCalcs(cost, delivery, profitMarg):
    return cost + delivery + profitMarg


# prints calculations to console
def printCalc(pValue):
    print("\nCar Make:\t{}".format(pValue[0]))
    print("Car Model:\t{}".format(pValue[1]))
    print("Cost Price:\t{}".format(pValue[2]))
    print("Delivery Charge:\t{}".format(pValue[4]))
    print("Profit Margin:\t{}".format(pValue[5]))
    print("Sales Price:\t{}".format(pValue[6]))


def textPrint(path, pValue):
        with open(path, "a") as file:
            s = "-------------"
            file.write("\n{:<18}{:<18}{:<18}{:<18}{:<18}{:<18}\n".format("Car Make", "Car Model", "Cost Price", "Delivery Charge", "Profit Margin", "Sales Price"))
            file.write("\n{:<18}{:<18}{:<18}{:<18}{:<18}{:<18}\n".format(s, s, s, s, s, s))
            file.write("{:<18}{:<18}{:<18,.2f}{:<18,.2f}{:<18,.2f}{:<18,.2f}\n".format(pValue[0], pValue[1], pValue[2], pValue[4], pValue[5], pValue[6]))


# getting user inputs
def inputDetails():

    try:
        # getting initial user input
        opelList.append(fnc.validString(input("Enter Car Make: ")))
        opelList.append(fnc.validString(input("Enter Car Model: ")))
        opelList.append(fnc.validFloat(input("Enter Car Cost: ")))
        opelList.append(fnc.validFloat(input("Enter Profit Margin: ")))

        # getting the calculated values
        opelList.append(deliveryCalcs(opelList[2], delivCharge))
        opelList.append(profitCalcs(opelList[2], opelList[3]))
        opelList.append(salesCalcs(opelList[2], opelList[4], opelList[5]))
    except:
        print("Error e001 - Error getting user input.")


# calls the opening message function
fnc.startMSG()

print("Please enter details as described below:\n")

# calls user input function
inputDetails()

# printing values to screen
printCalc(opelList)
# printing data to txt file and displaying confirmation
textPrint(filePath, opelList)
fnc.confirmation(filePath)

# calls the closing message function
fnc.endMSG()
