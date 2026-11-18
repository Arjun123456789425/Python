# # # #List is a datatype used to store a collection of values
# # # #since it is a combination of other data types (int,float,string,boolean)
# # # #we call it a derived data types

# # # #There is no restriction in terms of data types in a list.
# # # A list can contains various types and so it is hetrogenious.

# # # #Declaring a list
# # # lst_name =[]   #Empty list
# # # print(type(lst_name))

# lst_name2 =['Arjun','Akash','Gautham']  #list with some valuesin it
# # # print(type(lst_name2))

# # # #method 2
# # # lst_name3 = list()  #just a list
# # # print(type(lst_name3))
# # # #Fetching values using index from list
# # # print('1',lst_name2[0])
# # # print('2',lst_name2[1])
# # # print('3',lst_name2[2])

# # # #List containing multiple datatypes
# # # #personal info as a list :name,age,graduation,year,university,height
# # amar_info =['Amar',22,2026,'CUSAT',171.5,lst_name2]
# # print(type(amar_info))
# # print(amar_info[0])    #
# # print(type(amar_info[0]))
# # print(amar_info[1])
# # print(type(amar_info[1]))
# # print(amar_info[2])
# # print(type(amar_info[2]))
# # print(amar_info[3])
# # print(type(amar_info[3]))
# # print(amar_info[4])
# # print(type(amar_info[4]))
# # print(amar_info[5])
# # print(type(amar_info[5]))

# # #####

# lst_1 =[1,2,3]
# lst_3 =[False,True,False]
# lst_1.sort(reverse=True)
# lst_name2.sort(reverse=True)    #sort yhe other way (descending)
# lst_name2.extend(lst_1)
# print(lst_name2)
# lst_3.append(lst_1)   #list 1 ws added as the last value of list 3
# print(lst_3)          
# lst_1.reverse()
# print(lst_1)
# lst_3.count(False)  # checks the count of value 'False'
# lst_3.count(True)
# print(lst_3.count(False),lst_3.count(True),lst_3.count('X'))  #output is 2 1 0 

#  #value at the last index
# print(lst_3[-1])

# #Fetching number of items in the list 
# len(lst_3)
# print('Total number of elements in :',lst_3, 'is',len(lst_3))

# #Value of the index
# print(lst_3)

# print('after clear')
# print(lst_3)
# print('********************************')
# print(lst_1)

# lst_1.insert(2,100)    # inserting 100 at index 2
# print(lst_1)           # out put [1, 2, 100, 3]

# lst_1.remove(2)  #remove(the value we want to remove)
# print(lst_1)

# lst_1.pop()
# print(lst_1)

###TUPLE
tuple_1=()
tuple_2 =(2026,'nov',27.5,False,[8,True,(9,8)])
print(type(tuple_2))
print(type(tuple_1))
print(tuple_2[2])
print(tuple_2.count('nov'))
print(tuple_2.index('nov'))
#once the tuple is created it can't bre mutable while lists are mutable.

del(tuple_2)
print(tuple_2)   #deleting a tuple