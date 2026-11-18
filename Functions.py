# defining a function to add 2 numbers

def display_sum(num1,num2):
 sum =num1 + num2
 print('The sum of',num1,'and',num2,'is',sum)


#a function will have a function name:manditory
#2input(s)
#3 Body of the function(what the function actually does):mandatory
#4 Output
# while we define input variables in the function definition,we are creating
#new variables with scope within the function.
#invoking the function
# display_sum(8.6,7)
# display_sum('happy ','diwali')

# def display_sum_custom():
#     print("we will display the sum of the two numbers you enter")
#     num1= float(input('Enter the first number:'))
#     num2= float(input('Enter the second number:'))
#     sum=num1+num2
#     print('The sum of',num1,'and',num2,'is',sum)

# # display_sum_custom()

# def detail_custom():
#     user =input('Enter your name:')
#     print(user,'Good morning'',','How are you')
   
# # detail_custom()
# #####
# num=5
# print('Multiplication table of 5')
# print('_________-______-__________')
# for i in range(1,11):
#   print(i,'*',num,'=',(i*num))


# #Function to display multiplication_table of any number 

# def display_multiplication_table():
#    print('We will display the multiplication table of the number you enter')
#    num = int(input('Enter the number:'))
#    print('-----------------------------------')
#    for i in range(1,11):
#     print(i,'*',num,'=',(i*num))
# display_multiplication_table()    

########################
# calculate_sum = 0
# calculate_avg =0
# find_large=0
# find_small=0

   
  
# s1 = int(input('Enter first score: '))
# s2 = int(input('Enter second score: '))
# s3 = int(input('Enter third score: ')) 
# s4 = int(input('Enter fourth score: ')) 
# s5 = int(input('Enter fifth score: '))
# scores = [s1, s2, s3, s4, s5]


# def calculate_sum():
#     add=  sum(scores)
#     print('sum is:',add)

# def calculate_avg(): 

#      avg= sum(scores)/len(scores)
#      print('Average is', avg)

# def find_large():
#    largest=max(scores)
#    print('largest mark is',largest)

# def find_small():
#    smallest = min(scores)
#    print('smallest score is',smallest)   
        

# calculate_sum()
# calculate_avg()
# find_large()
# find_small()
# def calculate_sum_1(score_list):
#    sum=0
#    for i in range(len(score_list)):
#       sum = sum + score_list[i]
#       print(f'total score = {sum}')
#       return sum                        #output of the function

# def calculate_sum_2(score_list):
#    sum=0
#    for score in score_list:
#       sum=sum+score
#       print(f'total score = {sum}')
#       return sum  

# scores =[20,30,20,30,40]
# total_1 =calculate_sum_1(scores)   #whenever there is an output,we can assign it to a variable
# print(f'total score is{total_1}')

# total_2 =calculate_sum_2(scores)
# print(f'total score is{total_2}')

# def check_even(i_num):
#    if(i_num % 2 ==0):
#       return True
#    else:
#       print('odd')
#       result=check_even(81)
#       print(result)
# 

###############################################################################################################
##############OPTIONAL ARGUMENTS ###############

def calculate_exponent(num,exp =2):     #here,exp is an optional input
   print(num**exp)

# calculate_exponent(5,)   
# calculate_exponent(5,3)
# calculate_exponent(0)

def create_wish(name,wish='Good day'):
  print(f'{name},{wish}')

# create_wish('Arjun')
# create_wish('Arjun','Good morning')
# create_wish(wish ='good afternoon',name ='Arjun')

def divide(num,den):
  result = num/den
  print(f'The answer is{result}')
# divide(40,5) 
# divide('a','b')  # Type error  or Runtime error

#Exception handling
#We write the specific crieteria so that code flow is not interrupted.
#we write potential runtime errors making code inside'try' block and the
#exception will be caught by the 'except' block.
  
# def divide(num,den):
#   try:
#     result =num/den
#     print(f'the answer is {result}')
#   except:
#     print('there is  problem')
#     print('You reached the end of the function')
# divide(54,7)    
# divide('a','b')
# divide(50,0)

#Rewriting the function with exception block displaying the error message

# def divide_new(num,den):
#  try:
#       result =num/den
#       print(f'the answer is {result}')
#  except Exception as e:
#    print(f'There is a problem:{e}')
# print('The End')   

def divide_new(num,den):
 try:
      result =num/den
      print(f'the answer is {result}')
 except TypeError:
   print('Please make sure you are entering numbers')
 except ZeroDivisionError:
   print('Please make sure to give non-zero values to denominator')
 except Exception as e:
   print(f'There is a problem: {e}')
 print('The End')   
divide_new(3,0) 