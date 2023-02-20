from abc import ABC, abstractmethod

class Employee :
    def __init__(self, emp_id,name,age,salary ):
        self.emp_id =emp_id
        self.name =name
        self.age = age
        self.salary =salary
        

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age

    def get_salary(self):
        return self.__salary

    @abstractmethod
    def display(self):
        pass