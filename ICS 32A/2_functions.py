#built-in functions include type(), len(), int(), str()

#def is short for function definition
#use def and return to make your function 

def gimme_five(): 
    return 5

gimme_five()

gimme_five() + (gimme_five() * 3)

type(gimme_five)

def square(n):
    return n * n

square(3)

def multiply(n, m):
    return n * m

multiply(3, 5)


### Doctstrings describe what functions do in Python
def square2(n):
    'Computes the square of a numeric argument'
    return n * n
#longer docstring

def squared(n):
    '''
    Computes the square of a numeric argument, while failing when
    given an argument that is not numeric.
    '''
    return n * n

# Functions must be defined before they are used

def square3(n):
    return n * n

def cube(n):
    return n * n * n

def read_number():
    return int(input('Enter a number: '))

num = read_number()
print('The square of', num, 'is', square3(num))
print('The cube of', num, 'is', cube(num))

test_strip = '  helloooo '.strip()
test_strip
test_strip2 = 'oohiiioooo'.strip('o')
test_strip2

def read_name():
    while True:  #while True = loop indefinitely until a return or a break statement
        #recall .strip takes away the front and end trailing
        first_name = input('What is the first name? ').strip()

        if first_name == '':
            print("You'll need to enter a first name")
        else:
            last_name = input('What is the last name? ').strip()
            
            if last_name == '':
                print("You'll need to enter a first name")   
            else:  
                return last_name + ', ' + first_name

name = read_name()
name 

##Local and Global scopes

#x,y,z are global
#a,b,c and parameter_sum are local
x = 10
y = 20
z = 30

def foo(a,b,c):
    parameter_sum = a + b + c
    return x + y + z + parameter_sum


### Functions defined inside of functions
def read_and_sum_numbers():
    def read_number():
        return int(input('Enter a number, use 0 to stop: '))

    total = 0

    while True:
        number = read_number()

        if number == 0:
            return total

        total += number

read_and_sum_numbers()

