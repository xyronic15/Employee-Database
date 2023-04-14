from employee import Employee
import datetime
import json

def updateEmployee(id: int, new_salary:int = None, new_department:int = None, emp_dict:dict = None, dep_dict:dict = None):

    old_dep = emp_dict[id].department

    # updates to employees
    if new_salary != None:
        emp_dict[id].salary = new_salary
    if new_department != None:
        dep_dict[old_dep].remove_employee(id, emp_dict)
        emp_dict[id].department = new_department
        dep_dict[new_department].add_employee(id)
    
# loads json from a file and returns a list of employees
def loadEmps(file_name:str):

    with open(file_name, "rt") as f:
        content = f.read()
        data = json.loads(content) # List of dicts

    employees = list(map(lambda employee: Employee(**employee), data))
    return employees

# Writes updates to json file.
def writeToFileEmps(file_name:str, employees: list):

    updated_employees = list(map(lambda employee: employee.to_json(), employees))

    with open(file_name, "wt") as f:
        updated_data = json.dumps(updated_employees)
        f.write(updated_data)

# Takes an id number and the list of employees returns the corresponding employee object
def findEmpByID(id:int, employees:list):

    matched_employees = list(filter(lambda employee: employee.id == id, employees))

    if len(matched_employees) == 0:
        raise Exception("That employee does not exist")
    if len(matched_employees) > 1:
        raise Exception(f"Conflicting employee ids: {matched_employees}")

    matched_employee = matched_employees[0]

    return matched_employee

# updateEmployee(3, 55000, 3)