#Delete Employee
def deleteemp ():  
i =int(input("Enter the Employee ID:"))
if i == emp_id:
    del employee[emp_id]
    print("Employee has been deleted successfully")
else:
    print ("Entry not found")
#Delete Department
def deletedep ():
i =int(input("Enter the Department ID:"))
if i == dep_id:
    del dep[dep_id]
    print("Employee has been deleted successfully")
else:
    print ("Entry not found")