from Employee import Employee

class PermanentEmployee(Employee):
    def calculate_salary(self):
        total = self.retrieve_salary * 1.2
        print('Total Salary:', total)
        return total