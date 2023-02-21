# importing SQL connector
import mysql.connector as sqlConn
import functions as fnc

# database login details
db = sqlConn.connect(
    host="localhost",
    user="user",
    passwd="easy2guess",
    database="mydb"
)
# defining DB cursor
dbCursor = db.cursor()


# displays all the options to screen
def menuDisplay():
    print("\n\tMAIN MENU\n")
    print("1. View an Employee")
    print("2. Add an Employee")
    print("3. Change Employee Details")
    print("4. Delete an Employee")
    print("5. Enter Payroll Details")
    print("6. Reports")
    print("7. Exit\n")


# user input for the menu
def getInput():
    while True:
        choice = fnc.validInt(input("\nPlease choose an option: "), 7)

        # simple switch statement
        match choice:
            case 1:
                empView()
            case 2:
                empAdd()
            case 3:
                empEdit()
            case 4:
                empDelete()
            case 5:
                payrollDetails()
            case 6:
                printReport()
            case 7:
                fnc.endMSG()
                exit()


# function
def empView():
    while True:
        # gets user input for empID and sets up the SQL query
        userChoice = fnc.validInt(input("\nPlease enter Employee ID: "))
        viewQuery = "SELECT firstName, surname, address, email, mobile, startDate, endDate FROM employee where empID ="

        try:
            # Firing SQL query and assigning response to a variable
            dbCursor.execute(viewQuery + str(userChoice))
            resultArray = dbCursor.fetchall()

            if not resultArray:
                print(f"No employees with the ID {userChoice} found.")
                continue

            # Printing the relevant data received
            for row in resultArray:
                print(f"\nFirst Name:\t" + str(row[0]))
                print(f"Surname:\t" + str(row[1]))
                print(f"Address:\t" + str(row[2]))
                print(f"Email:\t\t" + str(row[3]))
                print(f"Mobile:\t\t" + str(row[4]))
                print(f"Start Date:\t" + str(row[5]))
                print(f"End Date:\t" + str(row[6]))

        except Exception as err:
            print(f"Error occurred: {str(err)}")
            continue

        while True:
            contChoice = input("\nDo you wish to view another employee's records? (y/n) ").lower()
            # sends user back to main menu
            if contChoice == "n":
                menuDisplay()
                return
            # kicks user back to empID choice
            elif contChoice == "y":
                break
            # error handling & keeps user here until correct entry
            else:
                print("Invalid input. Please enter (y/n) ")
                continue


def empAdd():
    pass


def empEdit():
    pass


def empDelete():
    pass


def payrollDetails():
    pass


def printReport():
    pass

# initialising the program
menuDisplay()
getInput()