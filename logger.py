import json
from employee import Employee
from Departments import Department

def read_employees():
    """Function that reads from an existing JSON file containing all of the employees. Returns a list fo employee objects"""

    # try reading an existing file or raise exception
    try:
        # open the filee
        with open('data/employees.json', "r") as f:
            data = json.load(f)

            # iterate through each entry and make employee objects
            employees = dict(map(lambda employee: (employee["id"], Employee(**employee)), data))

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

def log_employees(employees):
    """Function that passes through a dict of employees and adds them to the employees JSON file"""

    # make a list of employee dictionaries
    data = list(map(create_employee_json, employees.items()))

    # turn the data into a json
    json_data = json.dumps(data, indent=2)

    # try writing file or raise exception
    try:
        # open the file
        with open('data/employees.json', "w") as f:
            
            # write the file
            f.write(json_data)

    except Exception as e:
        print(e)

def log_departments(departments):
    """Function that passes through a dict of departments and adds them to the departments JSON file"""

    # make a list of employee dictionaries
    data = list(map(create_dept_json, departments.items()))

    # turn the data into a json
    json_data = json.dumps(data, indent=2)

    # try writing file or raise exception
    try:
        # open the file
        with open('data/departments.json', "w") as f:
            
            # write the file
            f.write(json_data)

    except Exception as e:
        print(e)


# list comprehension functions

# def create_employee_obj(data):
#     """Function that reads from the data passed from the JSON and makes an employee object"""

#     employee = Employee(data["id"], data["first_name"], data["last_name"], data["emp_date"], data["salary"], data["department"])

#     return data["id"], employee

def create_dept_obj(data):
    """Function that reads from the data passed from the JSON and makes an employee object"""

    department = Department(data["id"], data["name"], data["budget"], data["phone_number"], data["employees"])

    return data["id"], department

def create_employee_json(data):
    """Function that takes one entry of employee and makes a dict ready for the json file"""

    employee = {"id": data[0], "first_name": data[1].first_name, "last_name": data[1].last_name, "emp_date": data[1].date, "salary": data[1].salary, "department": data[1].department}

    return employee

def create_dept_json(data):
    """Function that takes one entry of employee and makes a dict ready for the json file"""

    department = {"id": data[0], "name": data[1].name, "budget": data[1].budget, "phone_number": data[1].phone_number, "employees": data[1].employees}

    return department