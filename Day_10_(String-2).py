# Methods of String : 
'''
--string is immutable in nature.
'''

string = 'SaNkEt'
print( string,"\n")
#1. len()  :- it is used to find length of string.
print( len(string) )

#2. upper()  :- convert all letters in strings into upper case
print( string.upper() )

#3. lower()   :- convert all letters in string into lower case
print( string.lower() , "\n\n")


s = '! ! _ help ! !! !!!'
print(s,'\n')

#4 rstrip()  :- strip the selected character in the string. (only back character not front)
print( s.rstrip("!") )

#5. replace() :- replace all selected latter into users string.      for eg. s.replace("seletcted str" , "new string")
print( s.replace('help', '_sanket_') )

#6. split() :- it convert string into list in the selected latter in the function  for eg. string.split( 'select spliting character in the str' )
a = s.split(' ')
print( a ," - ", type(a) )

a = 'i lOVE yoU ..a.u'

#7. capitalize() :- convert only frist latter in the string into upper case an then it also convert remaining inot lower case. if first letter is already in upper case then it cannot make in change in first latter..
print( a.capitalize())

#8. center()  :- align string into center as per the parameter  given
s = a.center(50)
print( len(a), '\n', s)
print( len(s) )

#9. count()  :- count the selected letter/stirng in a single/multiple string.
print( a.count('o'))

#10. endswith() :- check the given string is ends with selected character/string. it give output in boolean form.
print( a.endswith('u'))

#11. find() :- it can check the character/string and returns its index. if match is not found then it returns -1, and it also give first occurence index number.
string = ' baby love really hurts without you ohh baby'
print( string.find('baby'))
print( string.find('boby'))

#12. index() :- similar to find method but major difference is if string is not found then it returns error.
print( string.index('baby'))

#13. isalnum() :- it check the string is alphanumberic or not alphanumeric means it contains a-z , A-Z and 0-9 characters
a = 'sanket125'
print( a.isalnum() )

#14. isalpha() :- it check the string is alphabetical or not.
print( a.isalpha() )

#15. islower() :- it check all characters in lower case or not.
a = 'Sanket'
print( a.islower() )

#16. isspace() :- it check sting contains white spaces or not.
print( string.isspace())


'''
        THERE IS LOT OF STRING METHODS HAVING IN PYTHON YOU CAN CHECK IN INTERNET       '''