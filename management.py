from employee import Employee
from department import Department

class EmployeeManagement:
    def __init__(self):
        self._employees = []

    def add_employee(self, employee):
        # print(employee)
        if isinstance(employee, Employee):
            # print(employee)
            self._employees.append(employee)

    def remove_employee(self, employee):
        if isinstance(employee, Employee):
            self._employees.remove(employee)


    def display_all_employees(self):
        for employee in self._employees:
            employee.display()
            print()

management = EmployeeManagement()

# add employees
emp1=Department(1,"Krish",33,60000,"IT")
emp2=Department(2,"Ram",25,6000,"CIVIL")
emp3=Department(3,"Rajuuu",27,400,"MECH")

# #add an employee
management.add_employee(emp1)
management.add_employee(emp2)
management.add_employee(emp3)
# print(management)

# #remove an employee
management.remove_employee(emp2)

# #display all employees again
# management.display_all_employees()

management.display_all_employees()
# print(management._employees)