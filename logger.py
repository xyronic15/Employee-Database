import json
from employee import Employee
from Departments import Department

def read_employees():
    """Function that reads from an existing JSON file containing all of the employees. Returns a list fo employee objects"""

    # try reading an existing file or raise exception
    try:
        # open the file
        with open('data/employees.json', "r") as f:
            data = json.load(f)

            # iterate through each entry and make employee objects
            employees = dict(map(create_employee_obj, data))

            return employees
    except Exception as e:
        print(e)

def read_departments():
    """Function that reads from an existing JSON file containing all of the departments"""
    
    # try reading an existing file or raise exception
    try:
        # open the file
        with open('data/departments.json', "r") as f:
            data = json.load(f)

            # iterate through each entry and make dept objects
            departments = dict(map(create_dept_obj, data))

            return departments
    except Exception as e:
        print(e)

def log_employees():
    """Function that passes through a list of employees and adds them to the employees JSON file"""
    pass

def log_departments():
    """Function that passes through a list of employees and adds them to the employees JSON file"""
    pass


# list comprehension functions

def create_employee_obj(data):
    """Function that reads from the data passed from the JSON and makes an employee object"""

    employee = Employee(data["id"], data["first_name"], data["last_name"], data["emp_date"], data["salary"], data["department"])

    return data["id"], employee

def create_dept_obj(data):
    """Function that reads from the data passed from the JSON and makes an employee object"""

    department = Department(data["name"], data["budget"], data["phone_number"])

    return data["id"], department