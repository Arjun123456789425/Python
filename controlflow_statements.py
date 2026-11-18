# # # #checking wether the number is bigger than 50
# # # ###########
# # # # number = input('please Enter a number:')
# # # # number =int(number)#convert inpu as a number

# # # # if(number > 50):
# # # #     print('The number is bigger than 50')

# # # # else:
# # # #     print('The number entered is smaller than 50') 


# # # # print('End of the program')  

# # # # number > 50 #the number entered is bigger than 50
# # # # number <= 50 # the number entered is not bigger than 50

# # # #########################
# # # # num =input('Enter the number:')
# # # # num =int(num)

# # # # if(num % 2 ==0):
# # # #     print(num,'is an Even number')

# # # # else:
# # # #     print(num,'is an odd number')

# # # temp = input('Enter the Temprature:')
# # # temp = float(temp)

# # # if( temp >= 35):
# # #   print('Very hot day')
# # # elif(temp >= 25):
# # #     print('Warm Day')
# # # elif(temp >= 15):
# # #       print('Cold day')
# # # else:
# # #       print('Freezing day')

# # #################################
# # ##############################
# # ####Iterative Statements#########

# # #For Loop : When no of iterations are known
# # #While Loop : used When no of iterations are unknown.but,stopping condition is known.

# # #print your name 10 times
# # # for i in range(10):   #we are giving no of iterations
# # #     print(i,":Arjun")  #iterative(repetative)task

# # # print('Using step operator')              range(start,end,step): 
# # #if step is not mentioned ,it takes step = 1
# # # for i in range(10,3,-1):
# # #   print(i,":Arjun")

# # # print('Odd numbers between 20 and 50')
# # # for i in range(21,50,2):
# # #     print(i,'is an odd number between 20 and 50') 
# # for i in range(20,50):
# #     if i % 2 != 0:
# #         print(i)

# ##### WHILE LOOP ######
# #

# ###############

# # num=21
# # while(num <50):  # Odd no between 20 and 50
# #     print(num, end=',')
# #     num=num+2

# # ###############
# # num =int(input('Enter a number'))


# #logical operators in control flow statements

# age = int(input('please enter you age:'))
# valid_id=input('Do you have a valid ID card(y/n:)')
# if (valid_id =='y'):
#     valid_id = True


#     print('We are checking your eligibility')

#     if(age >=18):
#         if(valid_id):
#             print('You are eligible for vote')
#         else:
#             print('You are not eligible to vote')
#             print('You need a valid id card to be eligible')

#     else:
#             print('You are not eligible to vote')
#             print('You should be 18 or above to be eligible')

#             print('---------------------------------------')   


#             if((age >= 18)and (valid_id)):
#                  print('You are eligible for voe')
#             else:  
#                    print('You are not eligible for voe')    

