#Delete Employee info from Employee Details
def deleteEmp ():  
emp_id =int(input("Enter the Employee ID:"))
if int(int(empd_id)) not in emp_dict.keys():
    print("Entry not found")
elif:
    print("Employee has been deleted successfully")
    
#Delete Employee info from Department Details
def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                employee.department = None
                return True
        return False
