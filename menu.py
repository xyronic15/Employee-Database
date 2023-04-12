# will allow us to select what operation to perform

# must have the option to create, update, and delete employees
# ---> will pass an employee number to each

menuDict = {1: "Add employees", 2: "Update employees", 3: "Delete employees"}

print("The following operations may be executed: ")
print(f"1: {menuDict[1]")
print(f"2: {menuDict[2]")
print(f"3: {menuDict[3]")
print("exit")

admin_choice = input("Select an operation to perform: ")

while admin_choice != "exit":

    # Add employees
    if admin_choice == '1':
        try:
            # needs a link
            from link import *
            addEmp(num)
        except:
            print("Operation not found.")

    # Update employees
    elif admin_choice == '2':
        try:
            # needs a link
            from link import * 
            updateEmp(num)
        except:
            print("Operation not found.")

    # Delete employees
    elif admin_choice == '3':
        try:
            # needs a link
            from link import * 
            deleteEmp(num)
        except:
            print("Operation not found.")

    # Exit the program
    elif admin_choice == 'exit':
        break

    # Exit the program
    else:
        admin_choice = input("Select an operation to perform: ")
