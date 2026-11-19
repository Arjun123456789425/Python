from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_name, salary):
        self.employee_name = employee_name
        self.__salary = salary

    @property
    def retrieve_salary(self):
        return self.__salary

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print('Name:', self.employee_name)
        print('Salary:', self.__salary)