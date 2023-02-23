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
                empPayroll()
            case 6:
                empReport()
            case 7:
                fnc.endMSG()
                exit()


# viewing existing records function
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


# Adding new employee function
def empAdd():
    while True:
        try:
            print("Enter Employee Details: \n")
            # gets user input for new employee information
            locFirstName = fnc.validString(input("Enter Employee First Name: "))
            locSurname = fnc.validString(input("Enter Employee Surname: "))
            locAddress = fnc.validString(input("Enter Employee Address: "))
            locEmail = fnc.validString(input("Enter Employee Email: "))
            locMobile = fnc.validString(input("Enter Employee Mobile: "))
            locStartDate = fnc.validDate(input("Enter Employee Start Date: "))
            locEndDate = fnc.validDate(input("Enter Employee End Date: "))

            # building SQL query + using tuples for parameters
            addQuery = "INSERT INTO employee(firstName, surname, address, email, mobile, startDate, endDate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            addArray = (locFirstName, locSurname, locAddress, locEmail, locMobile, locStartDate, locEndDate)

            # executing SQL query and committing the changes to the DB
            dbCursor.execute(addQuery, addArray)
            db.commit()
            print("\nEmployee details added to database.")

        except Exception as err:
            print(f"Error occurred: {str(err)}")

        while True:
            contChoice = input("\nDo you wish to add another employee? (y/n) ").lower()
            # sends user back to main menu
            if contChoice == "n":
                menuDisplay()
                return
            # kicks user back to details input
            elif contChoice == "y":
                break
            # error handling & keeps user here until correct entry
            else:
                print("Invalid input. Please enter (y/n) ")
                continue
        pass


# editing existing records function
def empEdit():
    # TODO: "UPDATE" SQL query and continuous loop
    pass


# deleting existing records function
def empDelete():
    while True:
        # gets user input for empID and sets up the SQL query
        userChoice = fnc.validInt(input("\nPlease enter Employee ID: "))
        delQuery = "DELETE FROM employee WHERE empID ="

        try:
            # Firing SQL query and deleting relevant records
            dbCursor.execute(delQuery + str(userChoice))
            db.commit()

        except Exception as err:
            print(f"Error occurred: {str(err)}")
    pass


# employee payroll data function
def empPayroll():
    # TODO: Sort out payroll
    pass


# printing payroll data function
def empReport():
    # TODO: Report formatting and setup
    pass

# initialising the program
menuDisplay()
getInput()