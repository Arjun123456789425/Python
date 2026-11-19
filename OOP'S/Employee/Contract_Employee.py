from Employee import Employee

class ContractEmployee(Employee):
    def calculate_salary(self):
        total = self.retrieve_salary * 1.05
        print('Total Salary:', total)
        return total