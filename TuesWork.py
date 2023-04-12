employees = []
totalEmployees = int(input("Get your number of employees:"))
empRange = range(0, totalEmployees + 1)

def get_employees():
    global employees
    global totalEmployees
    empID = 0

    while empID < totalEmployees:
        empID += 1
        #get the employee's name
        employeeName = input("Type your full name: ")

        #split the employee's name into first and last, then print
        employeeFirstName, employeeLastName = employeeName.split()
        employeeFirstName, employeeLastName = employeeFirstName.capitalize(), employeeLastName.capitalize()

        #capitalized laziness for printing all results
        employeeName = f"{employeeFirstName} {employeeLastName}"

        #get employee year of birth and age
        employeeAge = int(input("Enter your age: "))
        employeeYOB = 2023 - employeeAge

        #get the last two digits
        employeeYOB = str(employeeYOB)[-2:]

        #generate employee email
        employeeEmail = f"{employeeFirstName}.{employeeLastName}{(employeeYOB)}@company.com"
        print(employeeEmail)

        #print all results to screen
        print(f"{employeeName} is {employeeAge} and can be reached at {employeeEmail}.")

        employees.append({"Employee ID": empID, "Employee Last Name": employeeLastName, "Employee First Name": employeeFirstName, "Employee Age": employeeAge, "Employee Email": employeeEmail})

        if empID == totalEmployees:
            break

get_employees()

print(employees)

f = open("empDataLog.txt", "a")
f.write(str(employees))
f.close()
