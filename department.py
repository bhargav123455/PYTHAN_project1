from python_project_1.employee import Employee

class Department(Employee) :
    def __init__(self, emp_id,name,age,salary,department ):
        super().__init__(emp_id, name,age, salary)
        self.department =department

    def display(self):
            print(f"id:{self.emp_id},Name:{self.name},age:{self.age}, department:{self.department}")
