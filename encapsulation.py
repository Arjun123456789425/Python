# class BankAccount:
#     def __init__(self,owner_name,bank_balance,account_type):
#         self.owner =owner_name
#         self.__bank_balance = bank_balance
#         self._account_type =account_type
#         #to get the private attribute
#     @property
#     def  bank_balance(self):
#       return self.__bank_balance

#     #To update the private attribute
#     @bank_balance.setter
#     def bank_balance(self,deposit_amt):
#        if deposit_amt <=0:
#           raise 'Deposit amount cannot be zero or negative value'
#        self.__bank_balance = self.__bank_balance + deposit_amt


#     @property
#     def  account_type(self):
#           return self._account_type
    
#     @account_type.setter
#     def account_type(self,typ_acc):
#         if typ_acc == 0:
#             raise 'Account type cannot be empty or zero'
#         self._account_type=typ_acc

    

# bank =BankAccount('ABC',12000,'savings')        
 
# print(bank._account_type)
# print(bank.bank_balance)

# # Syntax:class.setter function =new value
# bank.bank_balance = 123
# print(bank.bank_balance)

# bank.account_type='Current'
# print(bank.account_type)

# class Employee:
#     def __init__(self,employee_name,department,salary):
#         self.emloyee_name = employee_name
#         self._department = department
#         self.__salary = salary

#     @property
#     def salary(self):
#         return self.__salary

#     @salary.setter    
#     def salary(self,amt):
#         if amt <=0:
#             raise 'Salary cannot be negative'
#         self.__salary  = self.__salary + amt

# class Manager(Employee):
#     def display_details(self):
#         print('Emloyee:', self.emloyee_name)
#         print('Department:', self._department)
#         print('Salary:', self.salary)

# manager =Manager('Arjun','Testing',25500) 
# manager.display_details()

# manager.salary=10000
# print('updated salary is:',manager.salary)

class Vehicle:  
    def __init__(self, vehicle_name, rental_type, rental_price):
        self.vehicle_name = vehicle_name
        self._rental_type = rental_type
        self.__rental_price = rental_price

    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self, price):
        if price <= 0:
            raise ValueError('Rental price cannot be negative')
        self.__rental_price = price

    def display_details(self):
        print('Vehicle name:', self.vehicle_name)
        print('Rental type:', self._rental_type)


class Car(Vehicle):
    def calculate_rent(self, days):
        return self.rental_price * days

    def display_details(self):
        print('Vehicle name:', self.vehicle_name)
        print('Rental type:', self._rental_type)
        print('Rental price:', self.rental_price)  


class Bike(Vehicle):
    def calculate_rent(self, days):
        return self.rental_price * days

    def display_details(self):
        print('Vehicle name:', self.vehicle_name)
        print('Rental type:', self._rental_type)
        print('Rental price:', self.rental_price)

bike= Bike('interceptor','Daily',3500)
bike.display_details()
print('Updated rent is:',bike.calculate_rent(5))

print('***************************************************')

car=Car('pagani','Daily',20000)
car.display_details()
print('Updated rent is:',car.calculate_rent(8))








              


      




    