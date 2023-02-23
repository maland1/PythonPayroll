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
    print("6. Summary Report")
    print("7. Payroll Report")
    print("8. Export to Excel")
    print("9. Exit\n")


# user input for the menu
def getInput():
    while True:
        choice = fnc.validInt(input("\nPlease choose an option: "), 9)

        # simple switch statement
        match choice:
            case 1:
                empView() # complete
            case 2:
                empAdd() # complete
            case 3:
                empEdit() # complete
            case 4:
                empDelete() # complete
            case 5:
                empPayrollDetails()
            case 6:
                empSummaryReport()
            case 7:
                empPayrollReport()
            case 8:
                empExcelExport()
            case 9:
                fnc.endMSG() # complete
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

        # continuous loop until user exits
        continueEntry()


# adding new employee function
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

        # continuous loop until user exits
        continueEntry()


# editing existing records function
def empEdit():
    while True:
        userChoice = fnc.validInt(input("\nPlease enter Employee ID: "))
        try:
            # checking if record exists
            if findRecord(userChoice):
                print("Enter Employee's New Details: \n")
                # gets user input for new employee information
                locFirstName = fnc.validString(input("Enter Employee First Name: "))
                locSurname = fnc.validString(input("Enter Employee Surname: "))
                locAddress = fnc.validString(input("Enter Employee Address: "))
                locEmail = fnc.validString(input("Enter Employee Email: "))
                locMobile = fnc.validString(input("Enter Employee Mobile: "))
                locStartDate = fnc.validDate(input("Enter Employee Start Date: "))
                locEndDate = fnc.validDate(input("Enter Employee End Date: "))

                # building SQL query + using tuples for parameters
                addQuery = "UPDATE employee SET firstName = %s, surname = %s, address = %s, email = %s, mobile = %s, startDate = %s, endDate = %s WHERE empID = %s"
                addArray = (locFirstName, locSurname, locAddress, locEmail, locMobile, locStartDate, locEndDate, userChoice)

                # executing SQL query and committing the changes to the DB
                dbCursor.execute(addQuery, addArray)
                db.commit()
                print("\nEmployee details updated.")

            else:
                continue

        except Exception as err:
            print(f"Error occurred: {str(err)}")

        # continuous loop until user exits
        continueEntry()

# deleting existing records function
def empDelete():
    while True:
        # gets user input for empID and sets up the SQL query
        userChoice = fnc.validInt(input("\nPlease enter Employee ID: "))
        delQuery = "DELETE FROM employee WHERE empID ="

        try:
            # Firing SQL query and deleting relevant records
            if findRecord(userChoice):
                userCheck = input("Are you sure you want to delete this record? (y/n) ")
                if userCheck == "n":
                    break
                elif userCheck == "y":
                    dbCursor.execute(delQuery + str(userChoice))
                    db.commit()
                else:
                    print("Invalid input. Please enter (y/n) ")
                    continue
            else:
                continue
        except Exception as err:
            print(f"Error occurred: {str(err)}")


# employee payroll data function
def empPayrollDetails():
    # TODO: Fix SQL query - need to be on PC
    while True:
        userChoice = fnc.validInt(input("\nPlease enter Employee ID: "))
        try:
            if findRecord(userChoice):
                locHours = fnc.validInt(input("Enter the Hours Worked: "))
                locPayRate = fnc.validInt(input("Enter the Rate of Pay: "))
                locTaxRate = fnc.validInt(input("Enter the Rate of Tax: "))
                locDate = fnc.currentDate()

                payrollQuery = "INSERT INTO payroll()"
                print("Details for Employee have been written to database.")

                while True:
                    contChoice = input("\nDo you wish to print a payslip? (y/n) ").lower()
                    # sends user back to main menu
                    if contChoice == "n":
                        continueEntry()
                    # kicks user back to details input
                    elif contChoice == "y":

                        ### payslip code here
                        break
                    # error handling & keeps user here until correct entry
                    else:
                        print("Invalid input. Please enter (y/n) ")
                        continue
            pass
        except Exception as err:
            print(f"Error occurred: {str(err)}")



# printing payroll data function
def empSummaryReport():
    # TODO: Report formatting and setup
        filePath = "C\\temp\\Employees.txt"
        try:

            pass
        except Exception as err:
            print(f"Error occurred: {str(err)}")


# exporting data to a report format
def empPayrollReport():
    while True:
        try:
            pass
        except Exception as err:
            print(f"Error occurred: {str(err)}")


# exporting data to Excel
def empExcelExport():
    while True:
        try:
            pass
        except Exception as err:
            print(f"Error occurred: {str(err)}")


# function for looping options
def continueEntry():
    while True:
        contChoice = input("\nDo you wish to continue? (y/n) ").lower()
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

# function for checking if record exists
def findRecord(id):
    # setting up and firing SQL query to find employee
    findQuery = "SELECT empID FROM employee WHERE empID = '" + str(id) + "';"
    dbCursor.execute(findQuery)
    rowCount = dbCursor.fetchall()

    if rowCount != 1:
        print("Employee records not found.")
    else:
        print("Employee records found.")

        # Firing SQL query and assigning response to a variable
        dbCursor.execute(viewQuery + str(userChoice))
        resultArray = dbCursor.fetchall()

        # Printing the relevant data received
        for row in resultArray:
            print(f"\nFirst Name:\t" + str(row[0]))
            print(f"Surname:\t" + str(row[1]))
            print(f"Address:\t" + str(row[2]))
            print(f"Email:\t\t" + str(row[3]))
            print(f"Mobile:\t\t" + str(row[4]))
            print(f"Start Date:\t" + str(row[5]))
            print(f"End Date:\t" + str(row[6]))

# initialising the program
menuDisplay()
getInput()