class Employee:
    
    def __init__(self, emp_id, first_name, last_name, emp_date, salary, dept):
        self.emp_id = emp_id, # int, every employee must have a unique id
        self.first_name = first_name, # str
        self.last_name = last_name, # str
        self.emp_date = emp_date, # datetime obj
        self.salary = salary, # int
        self.dept = dept # int

    def __add__():
        # adds employee, assigns unique id num
        pass

    def __remove__():
        # asks for id num, removes emp from database
        pass

    def __update__():
        # asks for id num, and which info they want to update
        pass

    def display_employee(self, dep_dict):
        """Function displays the employee's full name, emp_date, salary and department"""
        print(f"Full name: {self.first_name[0]} {self.last_name[0]}")
        print(f"Date of Employment: {self.emp_date[0]}")
        print(f"Current salary: {self.salary[0]}")
        print(f"Department: {dep_dict[self.dept].name}")
