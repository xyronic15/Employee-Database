from employee import *
from Departments import *
from exceptions import *
from update import *

def addEmp(emp_dict):
    num_emp = input("Enter number")

    for i in range(num_emp):
        # ask for first and last name
        # ask for all the appropriate info

        # make a new employee obj
        # add it to the dictionary
        pass

    pass

def updateEmp():
    # ask for how many emps being updated
    update_count = int(input("How many employees do you want to update?"))

    for i in range(0, update_count):
        update_id = int(input("Please input the id of the employee you are updating: "))
        new_salary = int(input("Please input their new salary: "))
        new_department = int(input("Please input their new department: "))
        updateEmployee(update_id, new_salary=new_salary, new_department=new_department)
    # for loop
    # ask for the id
    # access dict and get the employee using the id
    # ask for the new salary and department
    # employee.update(salary, dept

# def deleteEmp():
#   emp_id =int(input("Enter the Employee ID:"))
#   if int(int(emp_id)) not in emp_dict.keys():
#     print("Entry not found")
#   elif:
#     print("Employee has been deleted successfully")


def readEmpById(emp_dict, dep_dict):
    """Function that takes a user input for ID and looks for it in the employee dictionary"""

    try:
        # ask for the ID of the employee
        emp_id = input("Enter an employee's ID: ")

        # raise errors
        if not emp_id.isnumeric():
            raise ValueError("Not an integer")
        if int(emp_id) not in emp_dict.keys():
            raise InvalidIDException(f"Employee ID {emp_id} not found")
        
        # get the employee from the dictionary and call their display method
        emp_dict[int(emp_id)].display_employee(dep_dict)

    except ValueError as e:
        print(e)
    except InvalidIDException as e:
        print(e)
    except Exception as e:
        print(e)

    print("\n")

def readAllEmp(emp_dict, dep_dict):
    """Function that iterates over employee dictionary and runs their display methods"""

    # loop through each employee object in the dict
    for employee in emp_dict.values():
        # call their display method
        employee.display_employee(dep_dict)
        print("\n")

def createDep(dep_dict, emp_dict):
    """Function creates a new department object and stores it in the department dict"""
    
    # generate a new id for the department
    dep_id = list(dep_dict.keys())[-1] + 1

    try:
        # ask the user for the name, budget, and phone number of the department
        name = input("Enter the department's name: ")
        if len(name) == 0:
            raise Exception("No name given")
        
        budget = input("Enter the department's budget: ")
        if not budget.isnumeric():
            raise ValueError("Invalid budget")
        
        phone_number = input("Enter a phone number: ")
        if len(phone_number) == 0:
            raise Exception("No number given")

        # Create the department object and add it to the dictionary
        dep_dict[dep_id] = Department(dep_id, name, int(budget), phone_number, [])

        # # print out the new department
        dep_dict[dep_id].display_department(emp_dict)

    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

def updateDep(dep_dict, emp_dict):
    """Function updates a department object by id"""

    # print out the names and id's of all the departments so that the user can choose
    print("List of departments:")
    for key, dep in dep_dict.items():
        print(f"ID:{key}, Department name: {dep.name}")
    print("")

    try:
        # ask for the ID of the employee
        dep_id = input("Enter a department's ID: ")

        # raise errors
        if not dep_id.isnumeric():
            raise ValueError("Not an integer")
        if int(dep_id) not in dep_dict.keys():
            raise InvalidIDException(f"Department ID {dep_id} not found")

        # ask the user for the name, budget, and phone number of the department
        name = input("Enter the department's new name if applicable: ")
        if len(name)==0:
            name = None
        
        budget = input("Enter the department's new budget if applicable: ")
        if not budget.isnumeric() and len(budget)!=0:
            raise ValueError("Invalid budget")
        elif len(budget)==0:
            budget = None
        
        phone_number = input("Enter a new phone number if applicable: ")
        if len(phone_number) == 0:
            phone_number = None

        # Update the department object
        dep_dict[int(dep_id)].update_department(name, budget, phone_number)

        # print out the updated department
        dep_dict[int(dep_id)].display_department(emp_dict)

    except ValueError as e:
        print(e)
    except InvalidIDException as e:
        print(e)
    except Exception as e:
        print(e)

def readDepById(dep_dict, emp_dict):
    """Function reads a department object by id"""

    # print out the names and id's of all the departments so that the user can choose
    print("List of departments:")
    for key, dep in dep_dict.items():
        print(f"ID:{key}, Department name: {dep.name}")
    print("")

    try:
        # ask for the ID of the employee
        dep_id = input("Enter a department's ID: ")

        # raise errors
        if not dep_id.isnumeric():
            raise ValueError("Not an integer")
        if int(dep_id) not in dep_dict.keys():
            raise InvalidIDException(f"Department ID {dep_id} not found")

        # print out the chosen department
        dep_dict[int(dep_id)].display_department(emp_dict)

    except ValueError as e:
        print(e)
    except InvalidIDException as e:
        print(e)
    except Exception as e:
        print(e)

def removeDepById(dep_dict, emp_dict):
    """Function removes a department object by id"""

    # print out the names and id's of all the departments so that the user can choose
    print("List of departments:")
    for key, dep in dep_dict.items():
        print(f"ID:{key}, Department name: {dep.name}")
    print("")

    try:
        # ask for the ID of the employee
        dep_id = input("Enter a department's ID: ")

        # raise errors
        if not dep_id.isnumeric():
            raise ValueError("Not an integer")
        if int(dep_id) not in dep_dict.keys():
            raise InvalidIDException(f"Department ID {dep_id} not found")

        # # print out the chosen department
        # dep_dict[int(dep_id)].display_department(emp_dict)

        # get the employees of the department and remove them from the department
        emp_ids = dep_dict[int(dep_id)].employees
        # print(emp_ids)
        for id in emp_ids:
            print(id)
            print(dep_dict[int(dep_id)].remove_employee(id, emp_dict))
        
        # remove the department
        dep_dict.pop(int(dep_id))

    except ValueError as e:
        print(e)
    except InvalidIDException as e:
        print(e)
    except Exception as e:
        print(e)