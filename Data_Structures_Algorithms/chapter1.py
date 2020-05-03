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
    # constructor for the class. It is called whenever a Dog
    # object/instance object is created. The reference called 
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
        self.speakText = bark


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

