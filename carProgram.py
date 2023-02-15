# importing generic functions from file
import functions as fnc

# setting up delivery charge variable for ease of changing
delivCharge = 0.05


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
def printCalc(value):
    print("\nCar Make:\t{}".format(value[0]))
    print("\nCar Model:\t{}".format(value[1]))
    print("\nCost Price:\t{}".format(value[2]))
    print("\nDelivery Charge:\t{}".format(value[4]))
    print("\nProfit Margin:\t{}".format(value[5]))
    print("\nSale Price:\t{}".format(value[6]))

# setting up list for print function
opelList = []

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

# calls the closing message function
fnc.endMSG()