## Statically-typed languages
# languages whose types are checked BEFORE the program runs. A program can't run with type errors, because those pre-execution checks will fail
## Dynamically-typed languages
# languages whose types are checked DURING a program's execution. These errors will manifest themselves as run-time errors while the program runs
 
# In languages like C++ and Java, for example, mostly check types before execution, but also allow some of those checks (in the form of casts) to be deferred until the program runs.

# Python is Dynamic!
# the types won't be checked until the program is executing, by which time those types will be clear (e.g., a variable's "type" at any given time would simply be the type of object currently stored in that variable).
# However, Python has type annotations that can be used to communicate type information to people reading the code

# in a function, you can follow the input parameters with a ": int", ": str" or whatever type
# then to specify the return type you do a "-> int", "-> bool", etc
def len_at_least(s: str, min_length: int) -> bool:
    'Returns True if the length of s is at least the given minimum'  #docstring
    return len(s) >= min_length

# annotate types of variables
age: int
#at this point, age would give an error because it's not defined yet
age = 42

# possibilities:
# int, str
# two possible options --> "int or float"
# specify tuple types in parenthesis like (int, str)
# specify list type in brackets like [int] or [int or float

#below takes a list of integers and/or floats and calculates the sum

def sum_numbers(nums: [int or float]) -> int or float:
    'Computes the sum of the numbers in the given list'

    total = 0

    for num in nums:
        total += num

    return total

sum_numbers([1,2,3,4,5])

# remember that in Python, type annotations are not actually checked. They won't cause an error if they are wrong
# below, both num1 and num2 are actually integers, but it will still run
def sum_two_num(num1: str, num2: int) -> int:
    'Sums two numbers'
    return num1 + num2

sum_two_num(4, 5)

