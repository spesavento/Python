#Syntax error is found before the program runs
#Run-time error is found when your program runs

#Python is an object-oriented programming language
#There are two kinds of methods in any object-oriented language: mutator and accessor methods. 

#type and class is the same thing is Python!
#These are the definition of the data and methods for a specific type of object.
#Examples include: int, float, str, list, dict

#Accessor Method
x = 'how are you'
y = x.upper() 
print(y)
x  #notice that the object that x refers to ('how are you') remains unchanges

#Mutator Method
myList = [1, 2, 3]
myList.reverse()
print(myList) #now object myList refers to [1,2,3] is changed  

#ALL classes contain accessor methods
#Without them, we could put values on objects, but never retrieve them

#SOME classes contain mutator methods
#I.e. the list class has the reverse method, but others (i.e. str, int, float class) have none.
#These classes are considered immutable

#Every class contains a special method called a constructor - creates an instance of an object by placing references to data within the object itself
#Consider a class called Dog
#CLASS = Dog    *note that class objects begin with an uppercase letter
#               think of a class as a blueprint from which you can make objects
#OBJECT = boyDog, girlDog
class Dog:
    # This (__init__  pronounced as the dunda init method) is the 
    # constructor for the class. It is a function called whenever a Dog
    # object/instance object is created. It allows you to set the attributes 
    #  The reference called 
    # "self" is created by Python and made to point to the space for the newly created object. 
    # Python does this automatically for us but we have to have "self" as the FIRST OR ONLY 
    # parameter to the __init__ method (i.e. the constructor).
    def __init__(self, name, month, day, year, speakText): 
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText
    # This is an accessor method that returns the speakText stored in the
    # object. Notice that "self" is a parameter. Every method has "self" as its
    # first parameter. The "self" parameter is a reference to the current
    # object or the instance object. The current object appears on the left hand side of 
    # the dot when the method is called.
    def speak(self):
        return self.speakText
    # Here is an accessor method to get the name
    def getName(self):
        return self.name
    # This is another accessor method that uses the birthday information to
    # return a string representing the date.
    def birthDate(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)
    # This is a mutator method that changes the speakText of the Dog object.
    def changeBark(self,bark):
        self.speakText=bark


boyDog = Dog("Mesa", 5, 15, 2004, "WOOOF") #name, birthday, sound of bark
girlDog = Dog("Sequoia", 5, 6, 2004, "barkbark")
#boyDog and girlDog are instance objects
#You can't do Dog.speak() or class.speak(),
#you have to do boyDog.speak() or instanceobject.speak()
print(boyDog.speak())
print(girlDog.speak())
print(boyDog.birthDate())
print(girlDog.birthDate())
boyDog.changeBark("woofywoofy")
print(boyDog.speak())

# Operator overloading
# int type knows what + means, str type knows what + means
# They called the x.__add__(y) for the type of x when you type x + y
# These operators that are already defined in Python are called "Magic Methods"
# BUT your class needs that defined, so you need to overload the operator of + 
# This means adding the x.__add__(y) method to your class

class Dogo:
    def __init__(self, name, month, day, year, speakText): 
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText
    def speak(self):
        return self.speakText
    def getName(self):
        return self.name
    def birthDate(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)
    def changeBark(self,bark):
        self.speakText=bark
    # When creating the new puppy we don’t know it’s birthday. Pick the
    # first dog’s birthday plus one year. The speakText will be the
    # concatenation of both dog’s text. The dog on the left side of the + 
    # operator is the object referenced by the "self" parameter. The
    # "otherDog" parameter is the dog on the right side of the + operator. 
    def __add__(self,otherDog):
        return Dog("Puppy of " + self.name + " and " + otherDog.name, \
            self.month, self.day, self.year + 1, \
            self.speakText + otherDog.speakText)

boyDog = Dogo("Mesa", 5, 15, 2004, "WOOOOF") 
girlDog = Dogo("Sequoia", 5, 6, 2004, "barkbark") 
print(boyDog.speak())
print(girlDog.speak()) 
print(boyDog.birthDate()) 
print(girlDog.birthDate()) 
boyDog.changeBark("woofywoofy") 
print(boyDog.speak())
puppy = boyDog + girlDog
print(puppy.speak())
print(puppy.getName())
print(puppy.birthDate())


#Testing operator overloading
#__add__(self, y)         x+y
#__contains__(self, y)    y in x
#__eq__(self, y)          x==y
#__ne__(self,y)           x!=y
#__ge__(self,y)           x>=y
#__le__(self,y)           x<=y
#__gt__(self,y)           x>y
#__lt__(self,y)           x<y
#__getitem__(self,y)     x[y] item at the yth position in x
#__hash__(self)          hash(x) Returns an integral value for x
#__int__(self)           int(x) Returns an integer representation of x
#__iter__(self)          for v in x
#__len__(self)           len(x)
#__mod__(self,y)         x%y
#__mul__(self,y)         x*y
#__neg__(self)           -x
#__str__(self)           str(x)  string representation of x suitable for user-level interaction
#__repr__(self)          repr(x)  string version of x suitable to be evaluated by the eval function.
#__setitem__(self,i,y)   x[i] = y   Sets the item at the ith position in x to y.
#__sub__(self,y)         x - y

class Testadd:
    def __init__(self, verbal, quant):
        self.verbal = verbal
        self.quant = quant
    def getVerbal(self):   #use different names from the dunda init method
        return self.verbal
    def getQuant(self):
        return self.quant
    def changeQuant(self,newQuant): #bring new in variable
        self.quant = newQuant
    def __add__(self, other):
        s1 = self.quant + other.quant
        s2 = self.verbal + other.verbal
        new = Testadd(s1, s2)
        return new
    
    def __gt__(self,other):   #who has the greater total score?
        r1 = self.quant + self.verbal
        r2 = other.quant + other.verbal
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.verbal, self.quant)


student1 = Testadd(157, 161)
student2 = Testadd(155, 165)

student1.getVerbal()
student2.getVerbal()
student1.getQuant()
student2.getQuant()
student1.changeQuant(167)
student1.getQuant()

addStudents = student1 + student2
addStudents.getVerbal()
addStudents.getQuant()
print(addStudents)

student1 > student2
if student1 > student2:
    print("Student 1 score is higher!")
else:
        print("Student 2 score is higher!")

#Modules
#Code that others wrote is usually provided in a module

import turtle
t = turtle.Turtle()  
#
# #safest way because namespace of module and turtle module are kept seperate
#All identifiers in the turtle module are in the turtle namespace, while the local identifiers are in the local namespace

#Indetation is very important in Python
#To adjust the indentation of a block of code in visual studio code
#⌘] / ⌘[


# Robot classes test
class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    
    def introduceSelf(self):  #this is what you call for the instance objects
        return "My name is " + self.name

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)
r1.introduceSelf()
r2.introduceSelf()

#set who the robot is looking at
r1.lookingAt = r2
r2.lookingAt = r1

class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def sitDown(self):  #this is command you call for the instance objects
        self.isSitting = True   #call in new variable or boolean
    def standUp(self):   #this is command you call for the instance objects
        self.isSitting = False

p1 = Person("Alice", "agressive", True) #case matters: True/False
p2 = Person("Becky", "talkative", False)
p1.name
p1.personality
p1.isSitting
p1.standUp()
p1.isSitting
p1.sitDown()
p1.isSitting

p1.robotOwned = r2
p2.robotOwned = r1

p1.robotOwned.name
p1.robotOwned.introduceSelf()
p2.robotOwned.introduceSelf()

