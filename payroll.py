# importing SQL connector, csv and generic functions
import csv
import mysql.connector as sqlConn
import functions as fnc

# defining base filepath
filePath = "C:\\temp\\"

# database login details
db = sqlConn.connect(
    host="localhost",
    user="root",  # ensure user/pass are "root" (doesn't work with that login on my machine) user="user", passwd="easy2guess",
    passwd="root",
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
                empView()  # complete
            case 2:
                empAdd()  # complete
            case 3:
                empEdit()  # complete
            case 4:
                empDelete()  # complete
            case 5:
                empPayrollDetails()  # complete
            case 6:
                empSummaryReport()  # complete
            case 7:
                empPayrollReport()  # complete
            case 8:
                empExcelExport()  # complete
            case 9:
                fnc.endMSG()  # complete
                db.close()
                exit()


# viewing existing records function
def empView():
    while True:
        # gets user input for empID and sets up the SQL query
        userChoice = fnc.validInt(input("\nPlease enter Employee ID: "))
        viewQuery = "SELECT firstName, surname, address, email, mobile, startDate, endDate FROM employee WHERE empID ="

        try:
            # Firing SQL query and assigning response to a variable
            dbCursor.execute(viewQuery + str(userChoice))
            resultList = dbCursor.fetchall()

            if not resultList:
                print(f"No employees with the ID {userChoice} found.")
                continue

            # Printing the relevant data received
            for row in resultList:
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
        while True:
            contChoice = input("\nDo you wish to view another employee record? (y/n) ").lower()
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
            addQuery = "INSERT INTO employee(firstName, surname, address, email, mobile, startDate, endDate) VALUES (" \
                       "%s, %s, %s, %s, %s, %s, %s)"
            addTuple = (locFirstName, locSurname, locAddress, locEmail, locMobile, locStartDate, locEndDate)

            # executing SQL query and committing the changes to the DB
            dbCursor.execute(addQuery, addTuple)
            db.commit()
            print("\nEmployee details added to database.")

        except Exception as err:
            print(f"Error occurred: {str(err)}")

        # continuous loop until user exits
        while True:
            contChoice = input("\nDo you wish to add another employee record? (y/n) ").lower()
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


# editing existing records function
def empEdit():
    while True:
        userChoice = fnc.validInt(input("\nPlease enter Employee ID: "))
        try:
            # checking if record exists
            if findRecord(userChoice):
                print("\nEnter Employee's New Details: ")
                # gets user input for new employee information
                locFirstName = fnc.validString(input("Enter Employee First Name: "))
                locSurname = fnc.validString(input("Enter Employee Surname: "))
                locAddress = fnc.validString(input("Enter Employee Address: "))
                locEmail = fnc.validString(input("Enter Employee Email: "))
                locMobile = fnc.validString(input("Enter Employee Mobile: "))
                locStartDate = fnc.validDate(input("Enter Employee Start Date: "))
                locEndDate = fnc.validDate(input("Enter Employee End Date: "))

                # parameterised SQL query and Tuple for insertion
                addQuery = "UPDATE employee SET firstName = %s, surname = %s, address = %s, email = %s, mobile = %s, startDate = %s, endDate = %s WHERE empID = %s"
                addTuple = (
                    locFirstName, locSurname, locAddress, locEmail, locMobile, locStartDate, locEndDate, userChoice)

                # executing SQL query and committing the changes to the DB
                dbCursor.execute(addQuery, addTuple)
                db.commit()
                print("\nEmployee details updated.")

            else:
                continue

        except Exception as err:
            print(f"Error occurred: {str(err)}")

        finally:
            # continuous loop until user exits
            while True:
                contChoice = input("\nDo you wish to edit another record? (y/n) ").lower()
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


# deleting existing records function
def empDelete():
    while True:
        # gets user input for empID and sets up the SQL query
        userChoice = fnc.validInt(input("\nPlease enter Employee ID: "))
        delQuery = "DELETE FROM employee WHERE empID ="
        payrollDelQuery = "DELETE FROM payroll WHERE empID ="

        try:
            # Firing SQL query and deleting relevant records
            if findRecord(userChoice):
                userCheck = input("Are you sure you want to delete this record? (y/n) ")
                if userCheck == "n":
                    return
                elif userCheck == "y":
                    dbCursor.execute(delQuery + str(userChoice))
                    db.commit()
                    dbCursor.execute(payrollDelQuery + str(userChoice))
                    db.commit

                    print("Employee ID {} and all associated records have been deleted.".format(userChoice))
                else:
                    print("Invalid input. Please enter (y/n) ")
                    continue
            else:
                continue
        except Exception as err:
            print(f"Error occurred: {str(err)}")

        finally:
            # continuous loop until user exits
            while True:
                contChoice = input("\nDo you wish to delete another record? (y/n) ").lower()
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


# employee payroll data function
def empPayrollDetails():
    while True:
        userChoice = fnc.validInt(input("\nPlease enter Employee ID: "))
        try:
            # if record exists for selected ID, then continue
            if findRecord(userChoice):
                locHours = fnc.validInt(input("Enter the Hours Worked: "))
                locPayRate = fnc.validFloat(input("Enter the Rate of Pay: "))
                locTaxRate = fnc.validFloat(input("Enter the Rate of Tax: "))
                locDate = fnc.currentDate()

                # parameterised SQL query and Tuple for insertion
                payrollQuery = "INSERT INTO payroll(empID, hoursWorked, rateOfPay, taxRate, dateCreated) VALUES (%s, %s, %s, %s, %s)"
                payrollTuple = (userChoice, locHours, locPayRate, locTaxRate, locDate)

                # inserting and saving changes
                dbCursor.execute(payrollQuery, payrollTuple)
                db.commit()
                print("Details for Employee have been written to database.")

                while True:
                    contChoice = input("\nDo you wish to print a payslip? (y/n) ").lower()
                    # sends user back to main menu
                    if contChoice == "n":
                        pass
                    # sends user to payslip printing
                    elif contChoice == "y":
                        # getting employee name and ID
                        payslipQuery = "SELECT empID, firstName, surname FROM employee WHERE empID ="
                        dbCursor.execute(payslipQuery + str(userChoice))
                        locNames = dbCursor.fetchall()

                        # simple calculations
                        locGross = locHours * locPayRate
                        locTaxPaid = (locGross * locTaxRate)/100
                        locNett = locGross - locTaxPaid

                        # forming final tuple for passing into print function (also fixing tuple formatting)
                        converter = locNames + list([locHours, locPayRate, locGross, locTaxPaid, locNett])
                        payslipList = [item for t in converter if isinstance(t, tuple) for item in t] + [item for item in converter if not isinstance(item, tuple)]
                        printPayslip(payslipList)
                        break
                    # error handling & keeps user here until correct entry
                    else:
                        print("Invalid input. Please enter (y/n) ")
                        continue

        except Exception as err:
            print(f"Error occurred: {str(err)}")

        finally:
            # continuous loop until user exits
            while True:
                contChoice = input("\nDo you wish to enter more payroll data? (y/n) ").lower()
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


# printing payroll data function
def empSummaryReport():
    summaryName = "Employees.txt"
    fullSummary = "{}{}".format(filePath, summaryName)
    with open(fullSummary, "w") as file:
        try:
            # initial formatting of file and headings
            tab = "============"
            sep = "------------"
            file.write("Employee Summary:")
            file.write("\n{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}\n".format(tab, tab, tab, tab, tab, tab))
            file.write("\n{:<18}{:<18}{:<18}{:<18}{:<18}{:<18}{:<18}".format("Employee ID", "Employee Name", "Address", "Email", "Mobile", "Start Date", "End Date"))
            file.write("\n{:<18}{:<18}{:<18}{:<18}{:<18}{:<18}{:<18}".format(sep, sep, sep, sep, sep, sep, sep))

            # getting values for insertion
            summaryQuery = "SELECT empID, firstName, surname, address, email, mobile, startDate, endDate FROM employee"
            dbCursor.execute(summaryQuery)
            result = dbCursor.fetchall()

            for row in result:
                file.write("\n{:<18}{:<18}{:<18}{:<18}{:<18}{:<18}{:<18}".format(str(row[0]), str((row[1] + ' ' + row[2])), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7])))

            print("The file {} has been created in {}".format(fileName, filePath))
            x = input("Press any key to continue.")
            # closing the function
            menuDisplay()
            return

        except Exception as err:
            print(f"Error occurred: {str(err)}")


def grossCalc(hrs, pay):
    gross = hrs * pay
    return gross


def taxCalc(gross, taxR):
    taxPaid = gross * (taxR / 100)
    return taxPaid


def netCalc(gross, tax):
    netPay = gross - tax
    return netPay


# exporting data to a report format
def empPayrollReport():
    while True:
        userChoice = fnc.validInt(input("\nPlease enter Employee ID: "))
        try:
            # if record exists for selected ID, then continue
            if findRecord(userChoice):
                while True:
                    contChoice = input("\nDo you wish to create a report for this employee? (y/n) ").lower()
                    # sends user back to main menu
                    if contChoice == "n":
                        x = input("Press any key to continue.. ")
                        menuDisplay()
                        return
                    # starts payroll function
                    elif contChoice == "y":
                        # fetching data for the heading section
                        headerQuery = "SELECT empID, firstName, surname FROM employee where empID ="
                        dbCursor.execute(headerQuery + str(userChoice))
                        headerList = dbCursor.fetchone()

                        # fetching data for the body section
                        bodyQuery = "SELECT * FROM payroll where empID ="
                        dbCursor.execute(bodyQuery + str(userChoice))
                        payDataList = dbCursor.fetchall()

                        # defining the head and body formatting
                        header = "\tEmployee ID: {:<16} || First Name: {:<12} || Last Name: {:<12}\n".format(headerList[0], headerList[1], headerList[2])
                        body = "{:<14} || {:<14} || {:<14} || {:<14} || {:<14} || {:<14} || {:<14}".format("Hours Worked", "Rate of Pay", "Gross Pay", "Tax Rate", "Tax Paid", "Nett Pay", "Date")

                        fileName = "Payroll Report - "
                        fullFile = "{}{}{}.txt".format(filePath, fileName, headerList[1] + " " + headerList[2])
                        with open(fullFile, "w") as file:
                            # writing header and body to file
                            file.write(header)
                            file.write("~" * 118 + "\n")

                            file.write(body + "\n")
                            file.write("~" * 118 + "\n")

                            for data in payDataList:
                                tempGross = grossCalc(data[2], data[3])
                                tempTax = taxCalc(tempGross, data[4])
                                tempNet = netCalc(tempGross, tempTax)
                                date = str(data[5])

                                # Formats the row to align with the body headings
                                row = "{:<14} || {:<14} || {:<14.2f} || {:<14.2f} || {:<14.2f} || {:<14.2f} || {:<14}".format(
                                     data[2], data[3], tempGross, data[4], tempTax, tempNet, date)

                                # For each row, write the formatted row and end with a new line
                                file.write(row + "\n")

                        print("\nSuccessfully created payroll report at {}".format(fullFile))

                    # error handling & keeps user here until correct entry
                    else:
                        print("Invalid input. Please enter (y/n) ")
                        continue
                pass

        except Exception as err:
            print(f"Error occurred: {str(err)}")


# exporting data to Excel
def empExcelExport():
    excelName = "payroll.csv"
    fullExcel = "{}{}".format(filePath, excelName)
    with open(fullExcel, "w", newline="") as file:
        try:

            # formatting the CSV export query and firing it
            excelQuery = "SELECT * FROM mydb.employee, mydb.payroll WHERE employee.empID = payroll.empID ORDER BY payroll.empID;"
            dbCursor.execute(excelQuery)
            excelResult = dbCursor.fetchall()

            # defines and writes every row to the file
            writer = csv.writer(file)
            for row in excelResult:
                writer.writerow(row)

            print("\nData exported to CSV file in the directory {}".format(fullExcel))

        except Exception as err:
            print(f"Error occurred: {str(err)}")


# function for checking if record exists
def findRecord(id):
    # setting up and firing SQL query to find employee
    findQuery = "SELECT empID FROM employee WHERE empID = '" + str(id) + "';"
    dbCursor.execute(findQuery)
    rowCount = dbCursor.fetchall()

    if rowCount == 0:
        print("Employee records not found.")
    else:
        print("\nEmployee records found.")

        # additional query for this part
        viewQuery = "SELECT firstName, surname, address, email, mobile, startDate, endDate FROM employee where empID ="
        # Firing SQL query and assigning response to a variable
        dbCursor.execute(viewQuery + str(id))
        resultList = dbCursor.fetchall()

        # Printing the relevant data received
        for row in resultList:
            print(f"\nFirst Name:\t" + str(row[0]))
            print(f"Surname:\t" + str(row[1]))
            print(f"Address:\t" + str(row[2]))
            print(f"Email:\t\t" + str(row[3]))
            print(f"Mobile:\t\t" + str(row[4]))
            print(f"Start Date:\t" + str(row[5]))
            print(f"End Date:\t" + str(row[6]))

        # ensuring it does not get stuck in a loop
        return resultList


# printing to text file
def printPayslip(data):
    fileName = "{}payslip{}{}.txt".format(filePath, data[1] + data[2], fnc.currentDate())
    with open(fileName, "w") as file:
        tab = "-----------------"
        file.write(
            "\n{:<18}{:<18}{:<18}{:<18}{:<18}{:<18}{:<18}\n".format("Employee Number", "Employee Name", "Hours Worked", "Rate of Pay",
                                                                    "Gross Pay", "Tax Paid", "Nett Pay"))
        file.write("\n{:<18}{:<18}{:<18}{:<18}{:<18}{:<18}{:<18}\n".format(tab, tab, tab, tab, tab, tab, tab))
        file.write("{:<18}{:<18}{:<18}{:<18,.2f}{:<18,.2f}{:<18,.2f}{:<18,.2f}\n".format(data[0], data[1] + " " + data[2], data[3],
                                                                                         data[4], data[5], data[6], data[7]))


# initialising the program
menuDisplay()
getInput()
