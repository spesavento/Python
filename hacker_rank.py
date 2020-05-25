
### Say "Hello, World!" With Python ###
print("Hello, World!")

### Python If-Else ###
n = int(input().strip()) #n from 1 to 100
if n % 2 != 0 or (n >= 6 and n <= 20):  #odd or between 6 and 20
    print("Weird")
else:
    print("Not Weird")

### Arithmetic Operators ###
a = int(input())
b = int(input())
print(a + b, a - b, a * b, sep = '\n')

### Python: Division ###
a = int(input())
b = int(input())
print("{0}\n{1}".format(a//b, a/b))

### Loops ###
n = int(input())
for i in range(0, n): #0 up to n
    print(i**2)       #print i to the power of 2

### Print Function ###
n = int(input())
print(*range(1, n+1), sep = '')
#range vs. *range
print(range(1, 10)) #range(1, 10)
print(*range(1, 10)) #1 2 3 4 5 6 7 8 9

### Day 1: Data Types ###
i = 4
d = 4.0
s = 'HackerRank '
new_int = int(input())
new_dbl = float(input())
new_str = input()
print(i + new_int)
print(d + new_dbl)
print(s + new_str)

### Write a function ###
def is_leap(year):
    leap = False
    
    if year % 4 == 0: #if year divisible by 4, if might be
        #if divisible by 100 but not divisible by 400
        if year % 100 == 0 and year % 400 != 0:
            leap = False
        else:
            leap = True
    else: #if it's not divisible by 4, not leap year
        leap = False
    
    return leap

is_leap(1990)

### Day 2: Operators ###
def solve(meal_cost, tip_percent, tax_percent):
    #They want it ROUNDED up or down. Int() always rounds DOWN/floors. So use round() first, then int()
    print(int(round(meal_cost + meal_cost*(tip_percent/100) + meal_cost*(tax_percent/100), 0)))

meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
solve(meal_cost, tip_percent, tax_percent)

### Day 3: Intro to Conditional Statements ###
N = int(input())
if N % 2 != 0 or (N >=6 and N <= 20): #if N is odd
    print("Weird")
else:
    print("Not Weird")

### What's Your Name? ###
def print_full_name(a, b):
    print("Hello", a, b + "! You just delved into python.")
    #or
    print("Hello {first} {last}! You just delved into python.".format(first = a, last = b))

first_name = input()
last_name = input()
print_full_name(first_name, last_name)

### String Split and Join ###
def split_and_join(line):
    list_str = line.split(" ")
    return("-".join(list_str))

split_and_join('this is a string')
split_and_join('this is a  string') #two spaces --> two '-'
'this is a  string'.split(" ") 
split_and_join('  this is a string  '.strip())

### Mutations ###
def mutate_string(string, position, character):
    l = list(string) #['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a'] 
    l[5] = 'k' #['a', 'b', 'r', 'a', 'c', 'k', 'd', 'a', 'b', 'r', 'a'] 
    string2 = ''.join(l)
    print(string2)
    #or
    print(string[:position]) #[:5] = 0,1,2,3,4
    print(string[position+1:]) #[6:] = 6,7,8,..
    return string[:position] + character + string[position+1:]

mutate_string('abracadabra', 5, 'k')

### sWAP cASE ###
def swap_case(s):
    return s.swapcase()

swap_case('HackerRank.com presents "Pythonist 2".')

### List Comprehensions ###
x, y, z, n = (int(input()) for _ in range(4))
print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)])
    #i from 0, 1 j from 0, 1 and k from 0, 1 only print [i, j, k] if sum != n

### Lists ###
N = int(input()) #total number of commands
l: list = [] #create an empty list --> usually just l = [] 

for i in range(N):
    command = input()
    #break up the command
    c = command.split() #insert 0 5 --> ['insert', '0', '5']
    if(c[0] == 'print'):
        print(l)
    elif(c[0] == "insert"):
        l.insert(int(c[1]), int(c[2])) 
    elif(c[0] == "remove"):
        l.remove(int(c[1]))
    elif(c[0] == "append"):
        l.append(int(c[1]))
    elif(c[0] == "sort"):
        l.sort()
    elif(c[0] == "pop"):
        l.pop()
    else:
        l.reverse()
print(l)

### Day 4: Class vs. Instance ###
class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            self.age = 0 #set age to 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge #set age to the initialAge
    
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    
    def yearPasses(self):
        self.age += 1

itr1 = int(input()) #number of iterations
for _ in range(itr1):
    age = int(input())
    #make an instance object p by calling the Person class and initializing age for the constructor method
    p = Person(age)
    p.amIOld() #call accessor method .amIOld()
    for _ in range(0,3): #for 3 years
        p.yearPasses() #call mutator method
    p.amIOld()
    print("") #print extra new line

### Day 5: Loops ###
n = int(input())
for i in range(1,11): #from 1 UP to 11 (1-10)
    print(("{num} x {iter} = {mult}").format(num = n, iter = i, mult = n*i))

### Day 6: Let's Review ###
def even_odd(s1):
    even_ind = ""
    odd_ind = ""
    for i in range(len(s1)): #from 0 UP to 6 (0-5 indeces) for Hacker
    #error 1:'int' object is not iterable -- use for i in range(len(s1)):
        if(i % 2 == 0): #if even index
            even_ind += s1[i]
        else:
            odd_ind += s1[i]
    print("{even} {odd}".format(even = even_ind, odd = odd_ind))

num_strs = 2
for i in range(num_strs):
    user_str = input() #e.g. Hacker and Rank
    even_odd(user_str)

### Integers Come In All Sizes ###
from typing import Tuple
a1, b1, c1, d1 = (int(input()) for _ in range(4)) 

print(a1**b1 + c1**d1) #a^b + c^d

### Day 7: Arrays ###
n = int(input()) #number of iterations
arr = list(map(int, input().rstrip().split())) #create an array
#.rstrip() removes trailing whitespace, .lstrip() removes leading whitespace, .strip() removes both
#input: 1 4 3 2
#output: [1, 4, 3, 2]

for i in range(n, 0, -1):
    print(arr[i-1], end = " ") #end with space instead of default newline

### Day 8: Dictionaries and Maps ###
n = int(input()) #number of key-value pairs
phone_dict: dict = {} #create an empty dictionary --> usually just phone_dict = {}

#create the dictionary 
for i in range(n):
    user_input = input().split() #name and number e.g. ['sara', '555-5555']
    phone_dict[user_input[0]] = user_input[1]  #aDict[key] = value

#print
print(phone_dict)
print(len(phone_dict))
print(phone_dict.keys())
print(phone_dict.values())
print(phone_dict.items())
#delete with del phone_dict['sara']   -->  {'seonghun': '333-3333'}
#or
#delete and store in new variable with my_phone = phone_dict.pop('sara')  --> my_phone = '555-5555'
#update 
phone_dict['new'] = '999-9999' #add new key-value pair
#find a value
print(phone_dict.get('jane')) #automatically returns None (instead of error) if it can't find the key
print(phone_dict.get('jane', 'Not Found')) #now it returns Not Found if there is no matching key

name = input()
#method 1:
while name != 'end':  #while True would eventually need to end using control+z
    try:
        name = input() #input a key to find
        if phone_dict.get(name, 'Not found') == 'Not found':
            print('Not found')
        else:
            print("{0}={1}".format(name, phone_dict[name]))
    except:
        break


#method 2:
name = input()

while(name != 'end'):
    if name in phone_dict:
        print("{0}={1}".format(name, phone_dict[name]))
    else:
        print('Not found')
    name = input()


### Day 9: Recursion 3 ###
def factorial(n):
    if n > 1:
        return n * factorial(n-1) #3 * factorial(2) --> 2 * factorial(1) --> 1 === 3*2*1
    else:
        return 1

n = int(input())
result = factorial(n)
print(result)

### Tuples ###
n = int(input()) #input number of integers
integer_list = map(int, input().split()) #use map() to apply int to your list of strings i.e. input: 1 2 
t = tuple(integer_list) #a tuple is an immutable list
print(t)
print(hash(t))
#What is this number?
# A hash is an fixed sized integer that identifies a particular value. 
# Each value needs to have its own hash, so for the same value you will get the same hash even if it's not the same object.
hash("Look at me!") #-7163733115444731801
f = "Look at me!"
hash(f)             #-7163733115444731801
# In Python, dictionaries and sets use hash to enable a quick look-up of a value in a large collection of values
# In a list, if you want to check if a value x is in a list, you use "if x in values:" where it goes through each value in the list
# This can take a long time depending on the length of the list
# In a SET or DICTIONARY, python keeps track of the hash values, so when you type "if x in values:", it will get the hash value for x,
# then only compare x with the values that have the same hash as x.
# This means sets and dictionaries must have non-mutable objects (only hashable objects)

### Finding the percentage ###
#Store in a dictionary - N names and N marks for students.
#User enters a student's name, outputs the average percentage marks by student, to two decimal places.
n = int(input()) #number of key-value/student-mark pairs
student_marks = {} #create an empty dictionary

for _ in range(n):
    #asterisk (star) operator is used in Python with more than one meaning attached to it
    #input: sara 33 44 55 --> name = 'sara' , line = ['33', '44', '55']
    name, *line = input().split()
    scores = list(map(float, line)) #create a list of floats -> line = [33.0, 44.0, 55.0]
    student_marks[name] = scores #input this person and scores into a dictionary[key] = value

print(student_marks) #{'sara': [44.0, 55.0, 66.0], 'seonghun': [99.0, 100.0, 99.0], 'gee': [33.0, 1.0, 100.0]}
query_name = input() #the key/name to return the average score for

avg_score = sum(student_marks[query_name])/len(student_marks[query_name])
print(round(avg_score,2))
#ERROR -- round(_, 2) may give one decimal place if fewer than 2 decimal points
print(round(3.14159,2))
print(round(4.3,2))

print("{:.2f}".format(avg_score))

### Text Wrap ###
#using textwrap
import textwrap
def wrap(string, max_width):
    print(textwrap.wrap(string,max_width)) #['ABCD', 'EFGH', 'IJKL',...]
    return '\n'.join(textwrap.wrap(string,max_width))

string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width = 4
wrap(string, max_width)

#without textwrap
def wrap2(string, max_width):
    for j in range(0, len(string), max_width):
        print(j)
    print("total length is: {0}".format(len(string)))
    loop = [string[i:i+max_width] for i in range(0, len(string), max_width)]
    print(loop)
    #string[0:4] 0 1 2 3
    #string[24:27] = no error - gives 'YZ'
    print('\n'.join(loop))
    return
    
string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width = 4
wrap2(string, max_width)

print(textwrap.wrap("saraaaaaaaaaaa",8)) #every line is at most 8 characters
string = "This is a very very very very very long string."
print(textwrap.wrap(string,8)) #every line is at most 8 characters - keeps words together
print(textwrap.fill(string,8)) 

textwrap.fill(string, max_width)

