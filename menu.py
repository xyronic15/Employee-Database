# will allow us to select what operation to perform

# import Departments
# import constants
# import employee
# import test
from logger import *
from utils import *

# must have the option to create, update, and delete employees
# ---> will pass an employee number to each

# get the employees and department dicts from the json first
emp_dict = read_employees()
dep_dict = read_departments()

menuDict = {1: "Add employees", 2: "Update employees", 3: "Delete employees", 4: "Read employee by ID", 5: "Read all employees", 6: "Create a department", 7: "Update a department", 8: "Read a Department by ID", 9: "Remove a department"}

# Display the print options
def menuOptions(): 
    print("The following operations may be executed: ")
    
    # loop through all of the options
    for key, option in menuDict.items():
        print(f"{key}: {option}")

    print("exit")

def failure():
    print("Operation not found.", end="\n\n")
    menuOptions()
    admin_choice = input("Select an operation to perform: ")
    return admin_choice

admin_choice = ""

while admin_choice != "exit":

    # reset the choice every loop
    menuOptions()
    admin_choice = input("Select an operation to perform: ")

    # Add employees
    if admin_choice == '1':
        try:
            ######### UPDATE ME #########
            # I need a link :D
            addEmp(emp_dict)
        except:
            admin_choice = failure()

    # Update employees
    elif admin_choice == '2':
        try:
            ######### UPDATE ME #########
            # I need a link :D
            updateEmp()
        except:
            admin_choice = failure()

    # Delete employees
    elif admin_choice == '3':
        try:
            deleteEmp(emp_dict, dep_dict)
        except:
            admin_choice = failure()
    
    # Read employee by id
    elif admin_choice == "4":
        try:
            readEmpById(emp_dict, dep_dict)
        except:
            admin_choice = failure()
    
    #  Read all employees
    elif admin_choice == "5":
        try:
            readAllEmp(emp_dict, dep_dict)
        except:
            admin_choice = failure()
    
    #  Create a department
    elif admin_choice == "6":
        try:
            createDep(dep_dict, emp_dict)
        except:
            admin_choice = failure()
    
    #  Update a department
    elif admin_choice == "7":
        try:
            updateDep(dep_dict, emp_dict)
        except:
            admin_choice = failure()
    
    #  Read department by id
    elif admin_choice == "8":
        try:
            readDepById(dep_dict, emp_dict)
        except:
            admin_choice = failure()
    
    #  Delete a department by id
    elif admin_choice == "9":
        try:
            removeDepById(dep_dict, emp_dict)
        except:
            admin_choice = failure()

    # Exit the program
    elif admin_choice == 'exit':
        break

# Log the employees and departments at the end
log_employees(emp_dict)
log_departments(dep_dict)