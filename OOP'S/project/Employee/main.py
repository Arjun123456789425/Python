from Contract_Employee import ContractEmployee
from Permanent_Employee import PermanentEmployee

print('Permanent Employee')
empp = PermanentEmployee('Arjun', 60000)
empp.display_details()
empp.calculate_salary()

print('Contract Employee')
cmpp = ContractEmployee('Rahul', 25000)
cmpp.display_details()
cmpp.calculate_salary()