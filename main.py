# String variables
empName = ""

# Numerical variables
hoursWorked = 0
rateOfPay = 0.00
rateOfTax = 0.15
taxPaid = 0.00
grossPay = 0.00
netPay = 0.00
bonus = 0


# getting user inputted data
def getEmployeeDetails():
    for i in range(5):
        # loops through 5 times
        while True:
            empName = str(input("\nEnter employee name: "))
            if len(empName) >= 3 and empName.isalpha():
                break
            print("Input invalid, please enter a name with at least 3 characters and consisting only of letters.")

        # Will ask for hours until valid answer is given
        while True:
            try:
                hoursWorked = int(input("Enter hours worked: "))

                if hoursWorked > 0:
                    break
                print("Input invalid, please enter a non-negative number.")

            except ValueError:
                print("Input invalid, please enter a valid number.")

        # Will ask for pay rate until valid answer is given
        while True:
            try:
                rateOfPay = float(input("Enter hourly pay rate: "))

                if rateOfPay > 0:
                    break
                print("Input invalid, please enter a non-negative number.")

            except ValueError:
                print("Input invalid, please enter a valid number.")


        # simple calcs for gross pay and tax
        grossPay = hoursWorked * rateOfPay
        taxPaid = grossPay * rateOfTax

        # checking bonus amount
        def bonusCheck(x):
            if x > 50:
                bonus = 100
                return bonus
            elif x > 45:
                bonus = 60
                return bonus
            elif x > 40:
                bonus = 50
                return bonus

        netPay = (grossPay - taxPaid) + bonus

        def printWages(x):
            print("Employee num: \t{}".format(i + 1))
            print("Employee name: \t{}".format(x))
            print("Hours worked: \t{}".format(hoursWorked))
            print("Rate of Pay: \t{:.2f}".format(rateOfPay))
            print("Rate of Tax: \t{:.0%}".format(rateOfTax))
            print("Gross Pay: \t\t{:.2f}".format(grossPay))
            print("Tax Paid: \t\t{:.2f}".format(taxPaid))
            print("Bonus: \t\t\t{}".format(bonus))
            print("Net Pay: \t\t{:.2f}".format(netPay))


def validString(x):
    while True:
        try:

            if x == "":
                raise Exception
            else:
                return x
        except:
            print("Invalid entry, please enter a valid string.")


def validInt():
    while True:
        try:
            val = int(input(x))
            if val < 1:
                raise Exception
            else:
                return val
        except:
            print("Invalid entry, please provide a valid integer.")


def validFloat(x):
    while True:
        try:
            val = float(input(x))
            if val < 1:
                raise Exception
            else:
                return val
        except:
            print("Invalid entry, please provide a valid float.")


# Calling all the functions with the respective input values
getEmployeeDetails()
