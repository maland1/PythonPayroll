import functions as fnc


def custMaint():
    pass


def suppMaint():
    pass


def exitApp():
    print("Exiting application!")
    exit()

def menuDisplay():
    print("\n\tMAIN MENU\n")
    print("1. Customer Maintenance")
    print("2. Supplier Maintenance")
    print("3. Exit Application\n")


def getInput():
    while True:
        # control loop isn't working properly
        choice = fnc.validInt(input("Please choose an option: "), 3)

        if choice == 1:
            custMaint()
        elif choice == 2:
            suppMaint()
        elif choice == 3:
            exitApp()

fnc.startMSG()
menuDisplay()
getInput()
fnc.endMSG()