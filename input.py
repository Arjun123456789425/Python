username = input('please enter your username:')  # we wait for the user to end vlue
password = input('please enter your password:')
print('the user name you entered is:', username)
print('the password you enteredis:', password)
print(type(username))
print(type(password))
#Alwys the output from the function input()is of datatype 'string'
#we have to explicitly convert into  numerical datatype if needed 
#float(variable_name) #float

Age = input('please enter your age:')  
height = input('please enter your height:')
print('the age you entered is: -', Age)
print('the height you enteredis: -', height )
# convert the types first
Age = int(Age)
height =float(height)
#print the types after conversion
print(type(Age))
print(type(height))

#######################
Name = input('please enter your name:')
DOB = input('please enter your dob:')
Course = input('please enter your course:')
place = input('please enter your place:')
College =input('please enter your college:')
print('My name is ',Name,',i was born in ',DOB,'and i completed my bachelors degree in ',Course)
print('.iam native to',place,',i completed my bachelors degree from',College,'.')
###############
#control flow statemnts



