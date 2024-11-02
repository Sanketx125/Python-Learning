

# functions (user define functions) :
'''
--function is a block of code that can use multiple time.
--it can removes extra code and complexity in program.
--def - defining function and passing values is called arguments of function'''

def addition( x , y):
    c = x + y
    return c

a = float(input("Enter first no.  : "))
b = float(input("Enter second no. : "))

result = addition( a , b)

print(result)


#=======================================================================================
# pass function :
'''
-- pass function is used when new trying nothing in our program 
-- for example we write as any if_else condtion and we write only else body not if this time this program not run but we 
   write a pass function the it can run writhout showing error.

'''
if 1 > 5:
    pass
else :
    print("wrong")

    

#                  * Exercise *
#-------------------------------------------------------------------------------------
'''                  
                1. addtion of n numbers using function.
                2. calculator using function and match case function.
                3. greatest number of given three numbers.
                4. patterns.
                5. '''


