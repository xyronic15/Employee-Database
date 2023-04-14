from employee import *
from Departments import *
from exceptions import *
from update import *

def addEmp(employees, departments):
    num_employees = int(input("Enter the number of employees to add: "))
    
    for i in range(num_employees):
        # Get next employee ID
        next_id = list(employees.keys())[-1] + 1
        # print(next_id)

        # Get employee information
        first_name = input("Enter employee first name: ")
        last_name = input("Enter employee last name: ")
        date_of_employment = input("Enter employee date of employment (DD/MM/YYYY): ")
        while True:
            try:
                salary = float(input("Enter employee salary: "))
                break
            except ValueError:
                print("Invalid input, please enter a valid number.")

        # Get department ID
        print("Department options:")
        print("List of departments:")
        for key, dep in departments.items():
            print(f"ID:{key}, Department name: {dep.name}")
        print(departments)
        
        
        
        while True:

            dept_id = int(input("Enter a department's ID: "))
            try:
                departments[dept_id]
                break
            except:
                print("That department id is invalid")
                
        

        employee = Employee(next_id, first_name, last_name, date_of_employment, salary, dept_id)

        # Add employee to dictionary
        employees[next_id] = employee

        # Add employee to the department
        departments[dept_id].add_employee(next_id)


def updateEmp(emp_dict, dep_dict):
    # ask for how many emps being updated
    update_count = int(input("How many employees do you want to update?"))

    for i in range(0, update_count):
        update_id = int(input("Please input the id of the employee you are updating: "))
        new_salary = input("Please input their new salary if applicable: ")
        if len(new_salary) == 0 or not new_salary.isnumeric():
            new_salary = None
        else:
            new_salary = int(new_salary)
        
        new_department = input("Please input their new department id if applicable: ")
        if len(new_department) == 0 or not new_department.isnumeric():
            new_department = None
        else:
            new_department = int(new_department)

        updateEmployee(update_id, new_salary=new_salary, new_department=new_department, emp_dict=emp_dict, dep_dict=dep_dict)

def deleteEmp(emp_dict, dep_dict):
    emp_id =int(input("Enter the Employee ID:"))
    if int(int(emp_id)) not in emp_dict.keys():
        print("Entry not found")
    else:
        dep_id = emp_dict[int(emp_id)].department
        dep_dict[int(dep_id)].remove_employee(int(emp_id), emp_dict)
        emp_dict.pop(int(emp_id))
        print("Employee has been deleted successfully")

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