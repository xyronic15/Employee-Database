from employee import employee
from Departments import Department
def test_department():
    # Create department
    d = Department("Engineering", 100000, "555-1234")

    # Create employees
    e1 = employee("John", "Doe", "01/01/2022", 50000, d)
    e2 = employee("Jane", "Smith", "02/01/2022", 60000, d)

    # Display department
    d.display_department()

    # Update department
    d.update_department(budget=120000)
    assert d.budget == 120000

    # Remove employee
    assert d.remove_employee(e1.emp_id) == True

    # Update employee
    assert d.update_employee(e2.emp_id, first_name="Janet", salary=70000) == True

    # Display department
    d.display_department()

test_department()
