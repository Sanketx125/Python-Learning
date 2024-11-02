

# Input function in python
'''
--input function is used for taking user input for computer.
--we can pass the string in this function which can print bye this function.
--everything accept by using input function is string.
--we need to use typecasting for changing the datatype of input function.'''

a = input()
print(a , " = ", type(a))

'''
--we need to using type casting method for accepting input function.
--for example ,
'''

a = int(input("Enter value : "))        # this can only access the integer values.

b = str(input("Enter value : "))        # accept string that accepts a-z, A-Z, 1,2,3,.... , and also accept all possible symbols

c = float(input("Enter value : "))      # it accept only float value. if we give the integer value then it auto convert into float.

