

# STRING :
'''
--everything in single ('---') and double ("----") quatation mark is string.
--("""-----""")  is used for multing sting.
--string is nothing but sequence of characters.
--we can access elements in strng by using index.
--the indexing is start from zero (0).
--index includes 0 and end with  (length of string)-1  .
'''

name = 'sanket'

multiline_string = '''
                        hello 
                          im the best..!
                            now im write a multiline string.'''

print("hello ", name, "\n\n")
print(multiline_string)

# length of string : use for finding lenght of string.

print( len(name))

# string slicing :

name = 'sanket_mane'

print(name[0])
print(name[1])
print(name[5])

for i in name:
    print(i,end=" ")


print("\n")
print(len(name))

print( name[0:6])    # sanket

print( name[0:4])    # sank

print( name[:4])     # sank

print(name[0:])      # sanket


# Negative slicing : 
'''
--negative slicing means 
                         eg.        name[s:e] 

                                 where,     s - starting index
                                            e - ending index
'''


print('''
                      * Negative sclicing *


       | positive indexing    |  0 |  1 |  2 |  3 |  4 | 5  |
       |----------------------|----|----|----|----|----|----|
       | string               |  s |  a |  n |  k |  e | t  |
       |----------------------|----|----|----|----|----|----|
       | Negative indxing     | -6 | -5 | -4 | -3 | -2 | -1 |
''')

name = 'sanket'

print(name[0 : -3])            # san

print(name[0 : len(name)-3])   # sanS

print(name[ -3: -1 ])          # ke

print(name[ len(name)-3 : len(name)-1 ])  # ke

















#                                   *  Quick Quize  *
'''
                          ----------------------------------------
                                      name = "example"
                                      
                                      print( name[-4 : -2] )
                                      
                                      
                                      output - ?

                          ----------------------------------------
                                      
                                      
'''