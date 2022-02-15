#Classes and Objects

#objects = encapsulation of variables and functions into a single entity
#objects get variables and functions from classes
#classes = template to create objects

#class contains variables and functions

class MyClass:
    variable = "blah"

    def function(self): #have to include self as a parameter
        print("This is a message inside the class.")

myobjectx = MyClass() #this assigns the above class(template) to an object

#variable myobjectx holds an object of the class "MyClass"
#that contains the variable and the function defined within the class called "MyClass"

#accessing object variables

#accesses variable inside of th newly created object "myobjectx"
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.variable

#outputs blah
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable)

#why doesn't print(myobjectx.function(self)) work? -- incorrect notation ... myobectx.function()

#can create multiple objects of the same class (have same variables and functions defined)
#each object contains independent copies of the variables defined in the class

#defines another object with MyClass class and changes string

print("Testing multiple different objects of the same class (have same variables and functions defined).")

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside a class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity" #if commented out, will report blah blah

#prints out both variables
print(myobjectx.variable)
print(myobjecty.variable)

#accessing object functions

#accesses a function inside of an object
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()
print(myobjectx.function()) #equivalent because function() calls print

#init()

#init is a special function called when class is being initialized
#init used for assigning values in class

class NumberHolder:
    def __init__(self,number):
        self.number = number

    def returnNumber(self):
        return self.number
    
var = NumberHolder(7)
print(var.returnNumber()) #prints 7

#Exercise

print("Exercise starting now.")

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000#.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000#.00

# test code
print(car1.description())
print(car2.description())

#look into self vs not self variables
#review use of init