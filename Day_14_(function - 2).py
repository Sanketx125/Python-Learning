
"""                              * FUNCTION ARGUMENTS *                                 """


def avarage(a ,b):                         # a & b are arguments.
    print("the avarage : ", (a+b)/2)

avarage( 2, 4 )


# there are three types of arguments :
'''
    1. default argument's
    2. Keyword argument's
    3. Required argument's   - it is mandetory to give the arguments in function
    4. variable length argument's
'''


# Default argument :
#---------------------

def avarage(a= 3 ,b= 9):                         # argument a&b with default value 3 & 9.
    return (a+b)/2

c = avarage()
print("using return : ",c)


# Keyword argument :
#---------------------

def avarage(a ,b):                         
    print("the avarage : ", (a+b)/2)

avarage( 2, 4 )
avarage ( b = 13, a = 3)             # keyword aregument


# required argument :
#---------------------

def avarage(a ,b = 12):    # here a is required argument it is mandetory to give value but not in case b.                      
    print("the avarage : ", (a+b)/2)

avarage( 2 )  



# variable length argument : YOU CAN PASS MULTIPLE ARGUMENTS.
#---------------------------

def avarage( *numbers ):    # *numbers theke all the value as tuble you can check this by using type() function.
    print( type(numbers))
    sum = 0    
    for i in numbers:
        sum = sum + i                    
    print("the avarage : ", sum / len(numbers))

avarage (1,2,3,4,5)             # 


'''

            def fun( *number )
            
            1. *number              : uset to take data in tuple
            2. **number             : used to take data in dictionary.
'''
