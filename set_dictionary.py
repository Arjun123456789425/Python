###SET##
# set1 = {}   #method 1   #this is not a set it is a dictionary
# set2 ={12,55,88,2026,True,'Bsnl',2026.0} #Declaring a set    #method 2
# set3 = set()   #method 3    #set
# print(type(set1))
# print(type(set2))
# print(type(set3))
# print(set2)  
#values were displayed but not in the order.
#set supports all data types ;hetrogenious
#duplicates are deleted
# roll ={1,2,3,4,5,6}
# roll_odd ={1,3,5}
# roll_even ={2,4,6}
# random = {1,5,9,4}
# random.add(2026)   # add this element in to the set
# print(random)
# print(random.difference(roll_odd))
# print(roll_odd.difference(random))
# print(roll.issuperset(roll_odd))     #True
# print(roll.issubset(roll_odd))       #False
# print(roll.issuperset(random))       #False

# print(roll.intersection(random))      #Common in both sets
# roll.discard(1)
# print(roll)
#set cannot acess data using index
#duplicates are not allowed 
#Mutable


###########################################################
##DICTIONARY##
# dict1 = {}
# dict2 ={'key1' : 'value1','key2' : 'value2','key3' : 'value3'}
# dict3 = dict()
# print(type(dict1))
# print(type(dict2))
# print(type(dict3))
# print(dict2) #Dictionary has a key-value pair
#a dictionaries keys and values can be of any datatype

# sample_dict ={1:'one',0:'Zero',1:'True',1:'ICT'}   #Keys are duplicated
# print(sample_dict)
#Keys will take the latest assigned value as its value
#{1: 'ICT', 0: 'Zero'} because 'ICT' is the latest value given to key 1
#duplicaion of keys are not allowed

#dictionary key =value associated with the key
# print(dict2('Key'))

# student_dict={'name':'Arjun','age':'20','university':'KTU','District':'Idukki'}
# print("whole dictionary:")
# print(student_dict)

student_dict={'name':'Arjun','mob':8590335709,'place':'kaimanam'}
print(student_dict)
# print('Values are:')
# print(student_dict.values())
# print('Items are:')
# print(student_dict.items())
