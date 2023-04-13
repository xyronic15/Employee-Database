class Department:
    def __init__(self, id, name, budget, phone_number, employees):
        self.id = id
        self.name = name
        self.budget = budget
        self.phone_number = phone_number
        self.employees = employees
    
    def add_employee(self, employee):
        self.employees.append(employee.emp_id)
        employee.department = self.id
    
    def remove_employee(self, emp_id, emp_dict):
        for employee in self.employees:
            if employee == emp_id:
                self.employees.remove(employee)
                emp_dict[emp_id].dept = None
                return True
        return False
    
    def update_department(self, name=None, budget=None, phone_number=None):
        if name is not None:
            self.name = name
        if budget is not None:
            self.budget = budget
        if phone_number is not None:
            self.phone_number = phone_number
    
    def display_department(self, emp_dict):
        print("Department:", self.name)
        print("Budget:", self.budget)
        print("Phone Number:", self.phone_number)
        print("Employees:")
        for employee in self.employees:
            print("  -", emp_dict[employee].first_name[0], emp_dict[employee].last_name[0])
        print()

# hr_dept = Department("Human Resources", 1000000, "555-1234")
# tech_dept = Department("Technology", 5000000, "555-5678")
