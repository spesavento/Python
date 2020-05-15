#Textbook - 2019_A Beginner's Guide to Python

#Strings in Python are immutable. If you modify a string, you are creating a new string

#Embedded quotes are easy! Just switch between '' and ""
print("It's the day")
print('She said "hello" to everyone')

#You can also use triple quotes for multi-line strings
z = """
Hello 
    World
"""
z
#Notice the \n new lines. Any spaces and new lines are part of the string

#Find the class/type of a string using type()
my_variable = 'Bob'
type(my_variable)

#Concatenate strings
string_1 = 'Good'
string_2 = " day"
string_3 = string_1 + string_2
string_3 #single string
print('Hello ' + 'World')

#Length of a string
print(len(string_3)) #'Good day'

#Accessing a character
my_string = 'Hello World' 
print(my_string[4])  #Index starts from 0! 
"World"[:3]



#Accessing multiple characters
print(my_string[4]) # characters at position 4 
print(my_string[1:5]) # from position 1 to 5 
print(my_string[:5]) # from start UP TO position 5, not including
print(my_string[2:]) # from position 2 to the end

#Repeating Strings
print('*' * 4) #multiply a sting
print('Hi' * 10)

#split string.split(' ') split where there is a space or given character
title = 'The Good, The Bad, and the Ugly' 
print('Source string:', title)
print(title.split(' ')) #now all spaces are replaced
print(title.split(','))
type(title.split(' '))


#counting strings  using string.count(' ')
my_string = 'Count, the number       of spaces'
print("my_string.count(' '):", my_string.count(' '))

#replacing strings
welcome_message = 'Hello World!' 
print(welcome_message.replace("Hello", "Goodbye"))

#substrings
print('Edward Alun Rawlings'.find('Alun')) #starting position of string
print('Edward John Rawlings'.find('Alun')) #-1 if not found
'Hello World'.find('o') #returns the start position of the first match

some_string = 'Hello World'
print('Testing a String')
print('-' * 20)
print('some_string', some_string) 
print("some_string.startswith('H')", some_string.startswith('H')) #True or False?
print("some_string.startswith('h')", some_string.startswith('h')) 
print("some_string.endswith('d')", some_string.endswith('d')) 
print('some_string.istitle()', some_string.istitle()) 
print('some_string.isupper()', some_string.isupper()) 
print('some_string.islower()', some_string.islower()) 
print('some_string.isalpha()', some_string.isalpha())

print('some_string.upper()', some_string.upper()) 
print('some_string.lower()', some_string.lower()) 
print('some_string.title()', some_string.title()) 
print('some_string.swapcase()', some_string.swapcase())
print('     Hello World    '.strip())

#String formatting using curly brackets {}
format_string = "Hello {}"
print(format_string.format('Phoebe'))

# Allows multiple values to populate the string 
name = "Sara"
age = 24
print("{} is {} years old".format(name, age))

#for lists of strings, you can format them in a string using indeces
format_string = "Hello {1} {0}, you got {2}%" 
print(format_string.format('Smith', 'Carol', 75)) 
'Hello {1}, you got {0}%'.format(75, 'Sara')

#To make it easier, you can use named placeholders. 
# Can use named substitutions, order is not significant 
format_string = "{artist} sang {song} in {year}" 
print(format_string.format(artist='The Red Hot Chili Peppers', song='"By the Way"', year=2002))

#Indicate the length of your placeholder with a colon : followed by the length
print('|{:25}|'.format('25 characters width')) #reserves 25 characters/blank spaces for within the brackets
# < left aligned
# > right aligned
# ^ centered
print('|{:<25}|'.format('left aligned')) #default
print('|{:>25}|'.format('right aligned')) 
print('|{:^25}|'.format('centered'))

#Thousands seperator
print('{:,}'.format(1234567890))

#Altenate formatting - through the string library Templates
import string
template = string.Template('$artist sang $song in $year')  #use $ on the keys
#use the .substitute to fill in the string.Template
print(template.substitute(artist='Freddie Mercury', song='The Great Pretender', year=1987)) #note: you must provide all the variables (3 keys --> 3 variables)
# If you DON'T have all the variables to match the keys, use .safe_substitute()
print(template.safe_substitute(artist='David Bowie', song='Rebel Rebel')) 

#Exercises 
#1. Explore replacing a string
#   Create a string with words separated by ',' and replace the commas with spaces; 
#   for example replace all the commas in 'Denyse,Marie,Smith,21,London,UK' with spaces. 
#    Now print out the resulting string.
my_string = 'Hello,my,name,is,Sara'
my_string.replace(',', ' ')

#2. Handle user input 
#   The aim of this exercise is to write a program to ask the user for two strings and 
#   concatenate them together, with a space between them and store them into a new 
#   variable called new_string.
#   • Print out the value of new_string.
#   • Print out how long the contents of new_string is.
#   • Now convert the contents of new_string to all upper case.
#   • Now check to see if new_string contains the string 'Albus' as a substring.

s1 = input('Input string 1: ').strip()
s2 = input('Input string 2: ').strip()
cat_s = s1 + ' ' + s2
new_string = cat_s
print(new_string)
print(len(new_string))
new_string.upper()
new_string.find('Albus') #-1 so not found

