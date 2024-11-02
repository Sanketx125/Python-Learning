
a = int(input("Enter a height : "))


aski = 97  # printing lower case latters


for i in range ( 1, a+1):
    for j in range( i):
        print(" ",chr(aski)," ", end=" ")
        aski = aski + 1
    print("\n")



aski = 65  # printing upper case latters

for i in range ( 1, a+1):
    for j in range( i):
        print(" ",chr(aski)," ", end=" ")
        aski = aski + 1
    print("\n")

