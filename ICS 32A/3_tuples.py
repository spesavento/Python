### LISTS and TUPLES

#A tuple is a data structure that contains an immutable sequence of values, whose types can be any mixture you'd like.
1, 2
('Boo', 11, 3.5) #parenthesis are optional, but help visually
#necessary in some cases - i.e.
type((1, 2))  #type function can take 1 or 3 argumentsd

#a tuple length is determined at the time it's created
len((5, 6))

#values in a tuple can't change
#tuples have indexes like ranges and strings do

point = (5, 6)
point[0]
point[1]

#But you cannot change the values like point[1] = 3

##Sequence assignment
#You can assign multiple values (as long as the left and right # variables match)
point = (5, 6)
x, y = point   #x, y, z = point wouldn't work because point only contains 2 values
x
y

a = 12
b = 9 
a, b = b, a
a
b

#you can use sequence assignment with objects other than tuples,
# however, it's more dangerous. You might not know how long the string is if inputted by a user
# the left side must match the number of characters
name = 'Boo'
a, b, c = name
a
b
c

### Lists
# A list in Python is a sequence of objects that you expect may change over its lifetime. New elements can be added, existing elements can be removed or rearranged, and so on

x = [1, 2, 3, 4]
x
type(x)
len(x)

#lists can be empty
nothing = []
len(nothing)

x[2]
x[0]

x
x[1] = 9
x

#indices can also be numbered negatively, with -1 being the last element and -2 being the second to last, etc.
x[-1] = 12
x
x[-3]

# *** negative indexing also works on ranges and tuples:
x = (1,4,5,2)
x[-1]
y = range(1, 4, 1)
y[-1]
y[-2]

#Use .append() to add an element to the end of a list
x = [1, 9, 3, 4]
x.append(15)
x
x.append([6, 7, 8])
x
#notice the whole list is added as the last element

# to add multiple elements, use the .extend() or +=
y = [1, 2, 3]
y.extend([4, 5, 6])
y
y += [7, 8, 9]
y

# remove elements
del y[4]
y

#The build in function list() can take anything that can be treated as a sequence
range(0, 10)
list(range(0, 10)) #takes a range
list((1, 2, 3))    #takes a tuple
list([1, 2, 3, 4]) #takes a list
list('Boo')

#### Slicing
x = list(range(1, 21, 2))
x

x[3:7]
#Negative indices can be used in either or both the start and stop positions. 
#DOES NOT INCLUDE STOP
x[4:-2]
x[-5:8]
x[-5:-1]
x[:5]  #doesn't include stop
x[4:]  #includes start
x[:]  #whole list

#so far, the step has been defaulted to 1
x[2:9:3]  #so from 5 up to 19 (include 17) by 3's
x[2:6:2]  #so from 5 up to 13 (include 11) by 2's

#a negative step
x[6:2:-1]  #start at 13 then down up to 5 (include 7) 
x[8:1:-2]
x[::-1]  #reverse the list

x[3:2]  #start at 3 then go down to 2 BUT index is undefined therefore positive 1, it's empty
x[3:2:-1]
