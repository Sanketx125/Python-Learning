# match cases :
'''
--this is similar to switch case in other languages.
--break statement is not menditory in python.'''

x = int(input("Enter a number : "))

match x:
    case 0:
        print(" x is zero. ")
    case 1:
        print(" x is one. ")
    case 2:
        print(" x is two. ")  
    case _ if ( x is not  [0,1,2]):
        print("ops, not identify")


#                   * Basic Exercise - calculator match case *