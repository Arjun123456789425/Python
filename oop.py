# student_1_name='Arjun'
# student_1_age=24
# print(student_1_name,student_1_age)
# student_2_name='Kalyan'
# student_2_age =24
# print(student_2_name,student_2_age)
# student_3_name='lovely'
# student_3_age =24
# print(student_3_name,student_3_age)
# student_4_name='kajal'
# student_4_age =24
# print(student_4_name,student_4_age)
# student_5_name='ajith'
# student_5_age =25
# print(student_5_name,student_5_age)

# class student:                    #class student created
#      def __init__(self,name,age):
#           self.name = name
#           self.age =age

# student_1=student('Arjun',20)     #student_1 is the object

# print(student_1.name,student_1.age)

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = student('Arjun', 20)
# s2 = student('Keerthi', 21)
# s3 = student('Rahul', 19)
# s4 = student('Ananya', 22)
# s5 = student('Kabir', 20)

# print(s1.name, s1.age)

          
# class Book:
#     def __init__(self,name,author,pages,year):     #constructor is a special type of function  that will be called 
#         self.name=name                             #when the class is initialized
#         self.author=author
#         self.pages=pages
#         self.year=year
# b1=Book('Dracula:','Bram stoker:',800,2002)   

# print(b1.name,b1.author,b1.pages,b1.year)
      
# class Employee:
#     #clas attribute
#     age=10

#     def __init__(self,Name,Salary,Id_no,job_role,joining_date):
#         self.name =Name
#         self.salary  = Salary
#         self.Id_no  = Id_no                     #instance attributes
#         self.job_role = job_role
#         self.joining_date=joining_date

#     def display_details(self):    #method()-Function vuild in a class
#         print( self.name,self.salary, self.Id_no, self.job_role, self.joining_date)


# E1=Employee('Rahul',20000,23,'HR', "23-2-2018")   
# E1.display_details()
# #Accesssing class attribute
# print(Employee.age)

# class Student:
#     count =0
#     def __init__(self,name,age,height):
#         self.name=name
#         self.age=age
#         self.height=height

#         Student.count =  Student.count + 1

#     def display_count(self):
#                 print(Student.count)  
#     def display_details(self):
#         print(self.name,self.age,self.height)

# s1 =Student('Arjun',23,'167 cm')
# s1.display_details()
# s1.display_count()


# class Animal:
#       def __init__(self,has_leg):
#             self.has_leg =has_leg
# class Dog(Animal):         
#          pass

# dog =Dog(has_leg='YES')

# print('The dog has 4 legs:',dog.has_leg)         

# class Animal:
#     def __init__(self, sleep, eat):
#         self.sleep = sleep
#         self.eat = eat

# class Dog(Animal):
#     def __init__(self, sleep,eat ):
#         super().__init__(sleep, eat)  
#         self.speaks = 'Bow'           

# class Cat(Animal):
#     def __init__(self, sleep, eat):
#         super().__init__(sleep, eat)  
#         self.speaks = 'Meow'          

# dog = Dog(sleep='yes', eat='yes')
# cat = Cat(sleep='yes', eat='yes')


# print(dog.sleep, dog.eat, dog.speaks)
# print(cat.sleep, cat.eat, cat.speaks)


# class Animal:
#     def __init__(self,name,age):
#         self.name =name
#         self.age=age
#     def eat(self):
#         print('The animal is eating')    

# class Dog(Animal):
   
    
#     def bark(self):
#         print('woof woof') 

# class Cat(Animal):
   
#     def meow(self):
#         print('meow meow')  

# dog = Dog('Kuttan', 3)
# cat = Cat('Rocky', 2)        

# print(dog.name,dog.age)
# dog.eat()
# dog.bark()
# print(cat.name, cat.age)
# cat.eat()
# cat.meow()


# class Person:
#     def __init__(self,name,age):
#          self.name =name
#          self.age =age
#     def display(self):
#          print(self.name,self.age)

# class Student(Person):
#      def __init__(self, name, age,course):
#           super().__init__(name, age)
#           self.course=course
#      def showcourse(self):  
#           print(self.course)

# person=Person('Arjun',24)
# student=Student('vimal',22,'Computer application')

# person.display()         
# student.display()        
# student.showcourse()

# from abc import ABC,abstractmethod
# class Bank(ABC):
#     @abstractmethod
#     def deposite(self):
#         pass
#     @abstractmethod
#     def loan(self):
#         pass

# class SBI(Bank):
#     def deposite(self):
#         print('Deposite is executed')

#     def loan(self):
#         print('Loan is applied')  

#     def profit(self):
#              print('profit')  
                

# sbi=SBI()
# sbi.deposite()
# sbi.loan()
# sbi.profit()

# from abc import ABC,abstractmethod
# class Shape(ABC):
#      def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         super().__init__()
#         self.length=length
#         self.width=width
#     def area(self): 
#         return self.length *self.width   

# class Circle(Shape):
#     def __init__(self,radious):   
#         self.radious=radious
#     def area(self):    
#         return 3.14 * self.radious * self.radious
    
# rectangle=Rectangle(4,5)
# print(rectangle.area())
# circle=Circle(2)
# print(circle.area())


