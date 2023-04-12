class Department:
    def __init__(self, name, budget, phone_number):
        self.name = name
        self.budget = budget
        self.phone_number = phone_number
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
        employee.department = self
    
    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                employee.department = None
                return True
        return False
    
    def update_employee(self, emp_id, first_name=None, last_name=None, date_of_employment=None, salary=None):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                if first_name is not None:
                    employee.first_name = first_name
                if last_name is not None:
                    employee.last_name = last_name
                if date_of_employment is not None:
                    employee.date_of_employment = date_of_employment
                if salary is not None:
                    employee.salary = salary
                return True
        return False
    
    def display_department(self):
        print("Department:", self.name)
        print("Budget:", self.budget)
        print("Phone Number:", self.phone_number)
        print("Employees:")
        for employee in self.employees:
            print("  -", employee.first_name, employee.last_name)

hr_dept = Department("Human Resources", 1000000, "555-1234")
tech_dept = Department("Technology", 5000000, "555-5678")
