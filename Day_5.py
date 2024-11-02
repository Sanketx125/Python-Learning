

# input()     fucntion:
'''
--the input fuction used for giving the input from user
--we can also pass the comment in it.
--for example,
'''
a = input('enter value : ')
print(a)


'''
--we can accept diffent types of data by useing input function
--for example, for accepting diffent values
'''

# int value
a = int(input("Enter integer value : "))
print(type(a))

# str value
a = str(input("Enter string value : "))
print(type(a))

# eval 
'''
--if we can not specify the type of data which can accept but using this method python can auto identify the data
--for example, 
'''

a = eval(input("Enter value : "))
print(a ,'  -  ', type(a))
