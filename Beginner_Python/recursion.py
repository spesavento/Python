#Recursion = where a function calls itself one or more times in order to solve a problem

#Example:
#n! n factorial
#Does n * (n-1)! work to explain it? Only sometimes. 5*4! works but 0*(-1)! does not

# n! {n*(n-1)! if n >= 1 or 1 if n = 0}
#By this definition, for 3!:
#3 >= 1 so 3*2!
#2 >= 1 so 2*1!
#1 >= 1 so 1*0!
#0 == 0 so 1
#A recursive function in code:
def fact(n): #assume n is positive
    if n >= 1:
        return n*fact(n-1) #calls function within function
    else:
        return 1
    
print(fact(0))
print(fact(1))
print(fact(4))  #4 * fact(3) --> 4 * 3 * fact(2) --> until f(0) is 1, function no longer called 

#Fibonacci sequence
# 1 1 2 3 5 8 ..
#Make a recursive function fib that finds the fibonacci number Fn given the index n
#Fn = Fn-1 + Fn-2

def fib(n): #assume n > 1 cause it starts at 1
    if n >= 3:  #Because first 2 numbers return 1
        return fib(n-2) + fib(n-1)  #recursive case
    else:
        return 1   #base case

#Terminology! 
#In a recursive function, the condition where is doesn't call itself is called a base case (the else statement here).
print(fib(3))
print(fib(5))
print(fib(6))

#Binary Search Tree
#A binary tree is a tree data structure made up of nodes in which each node has a value, a left pointer and a right pointer.
#The root node is the top node
#It has a left and right pointer to a subtree
#This continues until a leaf node, at the bottom, where it's left and right pointers are empty (None)

# If the root node holds the value we print it;
# Otherwise we can call the search function on the child nodes of the current node. 
# If the current node has no children we just return without a result.

#Pseudo code
#def search(value_to_find, current_node): 
#    if current_node.value == value_to_find:
#        print('value found:', current_node.value) 
#    elif current.node.has_children:
#        search(value, current_node.left) search(current_node.right)

#Note: In Python, recursion is less efficient than iteration
#To improve performance, there are some features such as tail recursion
#tail recursion - where the calculation is performed BEFORE the recursive case. 
# The result is then passed to the recursive step, which results in the last statement in the function just calling the recursive function.

#res = n * factorial(n-1) #would NOT be tail recursive because it multiplies n by the recursive function
#return tail_factorial(n - 1, accumulator * n) #would be, recursive function is the last statement

def tail_factorial(n, accumulator=1): 
    if n == 0:
        return accumulator 
    else:
        return tail_factorial(n - 1, accumulator * n) 

print(tail_factorial(5))

#accumulator * n 
#n -> 5 - 1 = 4  accumulator -> 1 * 5 = 5
#n -> 4 - 1 = 3  accumulator -> 5 * 4 = 20
#n -> 3 - 1 = 2  accumulator -> 20 * 3 = 60
#n -> 2 - 1 = 1  accumulator -> 60 * 2 = 120
#n is 1 so it's return accumulator now 


