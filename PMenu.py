def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Exit")
     
    # Taking choice from user
    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_Employ()
         
    elif ch == 2:
        Remove_Employ()
         
    elif ch == 3:
        Promote_Employee()
         
    elif ch == 4:
        Display_Employees()
         
    elif ch == 5:
        exit(0)
         
    else:
        print("Invalid Choice")
        menu()