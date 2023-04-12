# will allow us to select what operation to perform

# must have the option to create, update, and delete employees
# ---> will pass an employee number to each

from utils import *

menuDict = {1: "Add employees", 2: "Update employees", 3: "Delete employees"}

# Display the print options

def menuOptions(): 
    print("The following operations may be executed: ")
    print(f"1: {menuDict[1]}")
    print(f"2: {menuDict[2]}")
    print(f"3: {menuDict[3]}")
    print("exit")

def failure():
    print("Operation not found.", end="\n\n")
    menuOptions()
    admin_choice = input("Select an operation to perform: ")
    return admin_choice
    
menuOptions()
admin_choice = input("Select an operation to perform: ")

while admin_choice != "exit":

    # Add employees
    if admin_choice == '1':
        try:
            ######### UPDATE ME #########
            # I need a link :D
            addEmp()
        except:
            admin_choice = failure()

    # Update employees
    elif admin_choice == '2':
        try:
            ######### UPDATE ME #########
            # I need a link :D
            updateEmp()
        except:
            admin_choice = failure()

    # Delete employees
    elif admin_choice == '3':
        try:
            ######### UPDATE ME #########
            # I need a link :D
            deleteEmp()
        except:
            admin_choice = failure()

    # Exit the program
    elif admin_choice == 'exit':
        break

