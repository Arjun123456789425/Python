#########################################
########  FILE HANDLING ############
#
filepath ='E:/PGP_AIML/Python/input.py'
relative_filepath ='input.py'

# file = open(filepath,'r')     #assign a file in reading mode 
# content =file.read()         #contents of the file is assigned to 'content'
# print(content)

# file_1 = open( relative_filepath,'r')
# content_1 = file_1.read()
# print(content_1)


# def read_file_relFilepath():
#     file_1 = open(relative_filepath,'r')
#     content_1 = file_1.read()
#     print(content_1)

# file.read()will return all the values as a single string

def read_line_by_line():
    file_1 = open(relative_filepath,'r')
    content_1 = file_1.readline()
    print(content_1)
# read_line_by_line() 
def read_lines():
    file =open(relative_filepath,'r')
    # read all the lines and populates the list 'content
    content = file.readlines()
    print(content)
    for line in content :
        print(line)
        print(type(content))
        file.close()
# read_lines()        
######################################################################
#WRITE

write_path ='students.txt'

#opens a file in writing mode 
#if the file didn't exist earlier,now, it will be created 
#and opened in writing mode

def write_file():
    file =open(write_path,'w')
    file.write('gowtham\n')
    file.close()
write_file()    

# def write1_file():
    
#     file =open(write_path,'w')
   
#     file.write('Akash\n')
#     file.write('Arjun\n')
#     file.write('gowtham\n')
#     file.close()
def append_file():
    file =open(write_path,'a')    
    file.write('Akash\n')
    file.close()
append_file()    


#this method of file assignment is preffered more
def append_to_file(file_path, content):
    file = open(file_path, 'a')
    file.write('\n')
    file.write(content)
    file.close()
append_to_file("students.txt", "Arjun")




    