#Two types of functions in Python:
# 1. built-in functions
# 2. user-defined functions

# def function_name(parameter list): 
#      """docstring"""
#      statement 
#      statement(s)

# def is a keyword for a function definition 
# function_name is lowercase and can be separated with '_'
# It is common to use 4 spaces (not a tab) to indent the body of a function

def print_msg(): 
    print('Hello World!')
    
print_msg()
 
def print_my_msg(msg): 
    print(msg)
 
print_my_msg('Hello World')

#Whenever a return statement is encountered within a function then that function will 
# terminate and return any values following the return keyword.
# print just prints a value to the screen, return value can be stored in a variable
def square(n):
    return n * n

result = square(4)
print(result)

def swap(a, b):
    return b, a

a = 2
b = 3
x, y = swap(a, b)
print(str(x) + ',', y) #concat + must have same types

def get_integer_input(message): 
    """
    This function will display the message to the user and request that they input an integer.
    If the user enters something that is not a number then the input will be rejected
    and an error message will be displayed.
    The user will then be asked to try again.
    """
    value_as_string = input(message)
    while not value_as_string.isnumeric(): #while value is not numeric
        print('The input must be an integer') 
        value_as_string = input(message) 
        return int(value_as_string)

age = get_integer_input('Please input your age: ') 
print('age is', age)

#Terminology
#A parameter is a variable defined as part of the function header and is used to make data available within the function itself.
#An argument is the actual value or data passed into the function when it is called. The data will be held within the parameters.

def greeter(name, message): 
    print('Welcome', name, '-', message)
    
greeter('Eloise', 'Hope you like Rugby')

#default parameter values:
#If parameters are not often used, you can have a default which can always be overwritten
#In the function below, name is mandatory and message is optional
def greeter_default(name, message = 'Live Long and Prosper'): 
    print('Welcome', name, '-', message)

greeter_default('Eloise')
greeter_default('Eloise', 'Hope you like Python') #overwrites the default

#IMPORTANT: 
# Once one parameter has a default value ALL remaining parameters to the RIGHT of that parameter must also have default values.
# You could not do "def greeter(message = 'Live Long and Prosper', name):"

# Named Arguments
def greeter_name(name, title = 'Dr',prompt = 'Welcome', message = 'Live Long and Prosper'):
    print(prompt, title, name, '-', message)

#To only assign a few arguments, use the names if they are out of order
greeter_name(message = 'We like Python', name = 'Lloyd')
greeter_name('Lloyd', message = 'We like Python') #name is already

# Arbitrary Arguments
def greeter_arb(*args): 
    print(args)
    print(len(args))
    for name in args:
        print('Welcome', name)

greeter_arb('John', 'Denise', 'Phoebe', 'Adam', 'Gryff', 'Jasmine')

#Positional and Keyword Arguments
#Some functions have a variable number of positional or keyword arguments. 
# Such functions have two arguments *args and **kwargs (for positional arguments and keyword arguments).

def my_function(*args, **kwargs): 
    for arg in args:
        print('arg:', arg) 
    for key in kwargs.keys():
        print('key:', key, 'has value: ', kwargs[key])

my_function('John', 'Denise', daughter='Phoebe', son='Adam')
my_function('Paul', 'Fiona', son_number_one='Andrew', son_number_two='James', daughter='Joselyn')

## Exercises
#Take the number_guess_game and split it into functions
#1. You could create a function to obtain input from the user.
#2. You could create another function that will implement the main game playing loop.
#3. You could also provide a function that will print out a message indicating if the
#   player won or not.
#4. You could create a function to print a welcome message when the game starts up.

import random

def welcome_func():
    print("Welcome to the number guess game")
    number_to_guess = random.randint(1,10)
    return number_to_guess

def user_input():
    guess = int(input('Please guess a number between 1 and 10: '))
    return guess

def play_game(number_to_guess):
    guess_count = 0
    while guess_count < 4:
        user_guess = user_input()
        guess_count += 1
        if user_guess == number_to_guess:
            return 1, guess_count
        elif user_guess < number_to_guess:
            print("Your guess was lower than the number")
        else:
            print("Your guess was higher than the number")     
    return 0, guess_count #if didn't win

def win_lose(win, guesses, number_to_guess):
    if(win == 1): #if they won
        print("Well done you won!")
        print("You took {0} goes to win the game.".format(guesses))
    else:
        print("Sorry. You ran out of guesses. The number was {0}.".format(number_to_guess))

def finish_game():
    print("Game Over")
        
number_to_guess = welcome_func()
win,guesses = play_game(number_to_guess)
win_lose(win, guesses, number_to_guess)
finish_game()
