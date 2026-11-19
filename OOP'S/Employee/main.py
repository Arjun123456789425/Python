from Permanent_employee import PermanentEmployee

from Contract_Employee import ContractEmployee

print('Permanent Employee')
empp = PermanentEmployee('Arjun', 60000)
empp.display_details()
empp.calculate_salary()

print('Contract Employee')
cmpp = ContractEmployee('Rahul', 25000)
cmpp.display_details()
cmpp.calculate_salary()