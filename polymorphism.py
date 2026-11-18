# class Person:
#     def __init__(self,Name,Age):
#         self.Name =Name
#         self.Age =Age

#     def display_details(self):
#        print('Person name:',self.Name)
#        print('person Age:',self.Age)      

# class Emloyee(Person):
#     def __init__(self, Name, Age,emp_id,salary,joining_date):
#         super().__init__(Name, Age)
#         self.emp_id =emp_id
#         self.salary =salary
#         self.joining_date=joining_date

#     def display_details(self):
#         print('Employee name:',self.Name)
#         print('Employee Age:',self.Age)   
#         print('Employee ID:',self.emp_id)
#         print(self.salary)
#         print(self.joining_date)


# class Father(Person):
#     def __init__(self, Name, Age,No_of_Children):
#         super().__init__(Name, Age)  
#         self.No_of_Children =No_of_Children
    
#     def display_details(self):
#         print(self.Name)
#         print(self.Age)    
#         print(self.No_of_Children)

# class Son(Person):
#     def __init__(self, Name, Age,father_name):
#         super().__init__(Name, Age)    
#         self.father_name =father_name  
#     def display_details(self): 
#         print('Son name:',self.Name)
#         print('Age:',self.Age)      
#         print('Father Name:',self.father_name)

# class Husband(Person):
#     def __init__(self, Name, Age,wife_name,marriage_date):
#         super().__init__(Name, Age) 
#         self.wife_name =wife_name
#         self.marriage_date =marriage_date 

#     def display_details(self): 
#         print(self.Name)
#         print(self.Age)
#         print(self.wife_name) 
#         print(self.marriage_date)

# person=Person('Abhi',27) 
# person.display_details()       

# emp = Emloyee('Arjun',24,'CC',50000,'30 -3-2028')    
# emp.display_details()    

# father = Father('Rahul',26,4)
# father.display_details()

# son =Son('Ronaldo',42,'Messi') 
# son.display_details()      

# hus =Husband('Arjun',24,'lovely','20-3-2028',)
# hus.display_details()    


# class Employee:
#     def calculate_salary(self):
#         print('Calculating employee salary')

# class Fulltime_Employee(Employee) :
#     def calculate_salary(self):
#         print("Full-time employee receives a fixed monthly salary")



# class Parttime_Employee(Employee):
#     def calculate_salary(self):
#         print('Part-time employee salary is based on working hours')  

# class Freelancer(Employee):
#     def calculate_salary(self):
#         print('Freelancer salary based on completing thr projects')    


# full = Fulltime_Employee()
# full.calculate_salary()         

# part =Parttime_Employee()
# part.calculate_salary()

# free =Freelancer()
# free.calculate_salary()

####################################################

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_holder, account_type, balance):
        self.account_holder = account_holder     
        self._account_type = account_type       
        self.__balance = balance                 
        

    def calculate_Intrest():
        pass             

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise  'Balance cannot be negative!'
        self.__balance = amount


    def deposit(self, amount):
        if amount <= 0:
            print(" Deposit amount must be greater than zero.")
            return
        self.balance = self.balance + amount
        print('Deposited:',amount)
        print(' Updated Balance:',self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print(" Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print(" Transaction failed: Insufficient funds!")
            return
        self.balance = self.balance - amount
        print(' Withdrew ',amount)
        print( 'Updated Balance:',self.balance) 

    def display_details(self):
        print("\n--- Account Information ---")
        print('Account Holder:',self.account_holder)
        print('Account Type:', self._account_type)
        print('Current Balance:',self.__balance)   

class Savings_account(BankAccount):
    def __init__(self, account_holder, account_type, balance):
        super().__init__(account_holder,'Savings', balance)
        

    def calculate_interest(self,):
     interest = self.balance * 0.05
     return interest        

class CurrentAccount(BankAccount):
    def __init__(self, account_holder):
        super().__init__(account_holder,'Current',)

    def calculate_interest(self):
        interest = self.balance * 0.02
        return interest    

ashbi =Savings_account('Ashbi',10000)             
rahul= CurrentAccount('Rahul',20000)

print(ashbi.deposit(5000))
print(ashbi.withdraw(2000))

print(rahul.deposit(3000))
print(rahul.withdraw(5000))


                 


                 
      
      
        
       