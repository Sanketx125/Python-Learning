# Loops in Python :
'''
--looping is nothing but repeating or interating a single statements again & again.
--in other way loop is block of code that can run repeatedly.
--there are two types of loop:
                               1. for loop
                               2. while loop
                               3. nested loops
--we can also add conditions in looping.
'''
name = 'sanket'
for i in name:
    print(i)
    if ( i == 'k'):
        print("this is somthing special")

colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
    print(color)
    for i in color:
        print(i,end="_")

# range(start : stop : step) function :
'''
--range function is very important in python.
--by default start with zero and ends with stop-1
--by default step is one'''

for i in range( 1 , 10): # it go 0-9
    print(i)

print("\n-------------------------------\n")
for i in range ( 1, 20, 2):
    print(i)