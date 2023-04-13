from Departments import Department
from dataclasses import dataclass, asdict
import datetime

@dataclass
class Employee:
    id: int
    first_name: str
    last_name: str 
    date: datetime.date 
    salary: int
    department: int

    def to_json(self):
        return asdict(self)
    
    def display_employee(self, dep_dict):
        """Function displays the employee's full name, date, salary and department"""
        print(f"Full name: {self.first_name[0]} {self.last_name[0]}")
        print(f"Date of Employment: {self.date[0]}")
        print(f"Current salary: {self.salary[0]}")
        print(f"Department: {dep_dict[self.department].name}")
