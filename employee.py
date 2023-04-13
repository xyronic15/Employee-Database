from Departments import Department
from dataclasses import dataclass, asdict
# import datetime

@dataclass
class Employee:
    id: int
    first_name: str
    last_name: str 
    date: str
    salary: int
    department: int

    def to_json(self):
        return asdict(self)
    
    def display_employee(self, dep_dict):
        """Function displays the employee's full name, date, salary and department"""
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Date of Employment: {self.date}")
        print(f"Current salary: {self.salary}")
        print(f"Department: {dep_dict[self.department].name}")
