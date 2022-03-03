#CertPractice

#variables and types

#string
my_string = "Hello!"
print(my_string)

my_string2 = str("Hello!")
print(my_string2)

#float
my_float = 7.0
print(my_float)

#array
my_list = [1,2,3]
print(my_list)
print(type(my_list))

#set
my_set = {1,2,3}
print(my_set)
print(type(my_set))

variable = "blue"
print(type(variable))

#delete variable
# variable = None
# del variable  ##this one!!
# variable.delete()
# delete(variable) ##this one!!

#set variable to nothing
# variable = null 
# variable = None ##this one!!
# variable = none
# var:=0 
print(variable)

#print representation (string repr)
# __repr__(variable)
print(repr(variable))  ##this one!!
# print(variable)
# variable.repr()

#initialize dictionary
my_dict = {} ##this one!!
# my_dict:={} #invalid
# my_dict = dict[] #invalid
# my_dict = new Dictionary() #invalid
print(type(my_dict))

#initialize set
# my_set:={} #invalid
my_set2 = set() ##this one!!
# my_set = set[] #invalid
# my_set = new Set() #invalid
print(type(my_set2))

#initialize bytes string
# bytes = new Bytes()
# bytes:= b""
# bytes = bytes[]
bytes  = bytes() ##this one!!
print(type(bytes))

#set bool to false
# my_bool.set_false()
# my_bool = false 
my_bool = False ##this one!!
# my_bool = bool("False") #returns true
print(my_bool)

#initialize a tuple with 2 numbers
# tuple = [1,2] #list
# tuple = Tuple([1,2])
# tuple = tuple(1,2)
tuple = (1,2) ##this one!!
print(type(tuple))

#assign two variables from a tuple
# a:b = (1,2)
# a,b:=(1,2)
# assign((a,b),(1,2))
a,b=(1,2) ##this one!!
print(a)
print(b)

#Lists
#add new element to list
list = []
list.append(1)
print(type(list))
print(list)

#access first element of list
list = [1,2,3,4,5]
print(list[0])

#access last element of list
print(list[-1])

#remove last element from list
# list[-1] = None #nope!
# pop(list) #nope!
# list = list.pop() #just prints last item in list
del list[-1] ##this one!!
print(list)

#remove first element from list
del list[0]
print(list)

#check if item is not part of a list
list = [2,3,4,5]

if 1 not in list: #no "is"
    print("1 is not in list")

#sort list
list = [5,9,2,4]
# list = sort(list) #nope!
# sort(list) #nope!
list.sort()
# list = list.sort() #nope!
print(list)

#remove value from list
# list.pop(5) #nope!
if 5 in list: #ok..
    list.remove(5)
# i = list.index(5)
# del list(i) #nope!
# list = list.filter(lambda x: x != 5) #nope!
print(list)

list.append(1)

#wrong way to reverse a list
# list = list[::-1] #works! 
# list.reverse() #works! doesn't create a new list!!
# list = list(reversed(list)) #doesn't work
# reverse(list) #doesn't work
print(list)

#count how many times a value appears in a list
list.append(1)
print(list)
# print(list.count(lambda x: x==1))
# print(len(filter(list,lambda x:x==1)))
# print(list.count(1)) ##this one!!
# print(count([x for x in list if x == 1]))

#length of list
# print(list.length())
print(len(list))
# print(count(list))
# print(list.count())

#randomize order of items in list
# from random import random
# # list.sort(key=random)
from ast import Pass
from multiprocessing.dummy import Namespace
import py_compile
from random import shuffle
from tkinter import Y
shuffle(list) ##this one!!
# list = list.shuffle() #list has no attribute shuffle!
# list.shuffle()
print(list)

#Basic Operators

#add
a = 3
b = 4
c = a + b
print(c)

#subtract
c = b-a
print(c)

#multiply
c = a*b
print(c)

#divide
c = (a+4)/b
print(c)

#power
c = a ** b
print(c)

#concetanate
a = "blue"
b = "dog"
c = a+b
print(c)

#substring
# c = a.substring(2,3) #nope! string doesn't have attribute substring
c = a[1:3]
print(c)

#fetch all numbers at even indices of list
c = [1,2,3,4,5,6,7,8,9,10,11,12]
c = c[::2]
print(c)
c = c[1::2]
print(c)

#concetenate lists
a = [1,2,3,4,5]
b = [11,10,9,8]
c = a + b
print(c)

#integer division operator
a = 22
b = 7
# c = a div b nope!
c = a//b #returns closest integer less than or equal to result
print(c)

#modulus
c = a%b 
print(c)

#check if one number greater than other
if a > b: #>> and << are bit shift operators
    print("a is greater than b")

#check if variable between two numbers
if b < 10 < a:
    print("10 is between a and b")

#check if two variables are true
a = True
b = True
# if (a,b) is True:
#     # print("a and b are true") #nope!
if a and b:
    print("a and b are true")

# if a == True and b == True: #single = DOES NOT WORK!!
#     print("a and b are true!")

#execute bitwise AND operation between numbers
#https://wiki.python.org/moin/BitwiseOperators
c = a & b
print(c)

#bitwise XOR (exclusive OR)
#https://www.geeksforgeeks.org/python-bitwise-operators/
c = a ^ b
print(c)

#bitwise shift right
c = a >> b
print(c)

a = []

#wrong way to check variable is not True
if a != True:
    print("a not true")

# if a !== True:
#     print("a not true!") #invalid syntax

if not a:
    print("a not true!!") #wrong way!!

if a is not True:
    print("a is not True")

#check is member is not part of iterable
list = [6,7,8,9]
# if 5 is not in list: #syntax invalid
# if not list.contains(5): #no attribute contains
if 5 not in list: ##this one!
# if 5 ~ list:
    print("5 not in list")

#Strings

#initialize multi-line string
# string = "this is a\n" . "multiline"
string = '''Multiline string'''
print(string)

#concetanate
string = "hello" + " everyone!"
print(string)

#length
print(len(string))

#check if string appears in another string
if "fun" in "this is fun":
    print('contains fun')
    
#check index of substring in another string
print("this is fun".index("fun"))

#check if string only has digits
string = "11111"
# if isnumber(string): #isnumber not defined
# if isdigit(string): #isdigit not defined
if string.isdigit():
    print(string)
# if string.isnumber(): #string has no attribute isnumber
#     print(string)

#check if string starts with another string
if "substring".startswith("sub"):
    print("yes!")

#joing string with comma delimiter
# print(["foo","bar"].join(",")) #no attribute join
# print(",".join["foo","bar"]) 
# print(",".join("foo","bar")) 
# print("," + ["foo","bar"])
list = ["foo","bar"]
joined = ",".join(list)
print(joined)
print(",".join(["foo","bar"]))

#split string to list with delimiter
string = "foo, bar"
print("foo,bar".split(","))

#capitalize all words in string
print(string.capitalize())
# print(capitalize(string)) #nope!
# print([x.capitalize() for x in "yo yo yo".split()].join(" "))
print(" ".join([x.capitalize() for x in "yo yo yo".split()]))

#Print number using a format string
number = 2
print("%d" %number)

#print number using f string
#https://realpython.com/python-f-strings/
number = 412
print(f"{number}")

#print number using string format function
print("{number}".format(number=number))

#find index of substring within a string
print("this is fun".find("fun"))


#Conditions
a = 1
b = 2

if a == b: # := is assignment operator
    print("a = b")
else:
    print("no")

if a != b: print("aaaaaaaa") #else: print("bbbbbb") #else doesn't work on single line

#complex condition
name = "Kayla"
age = 24
if name == "Karis" and age == 24:
    print("yeah!")

#print output
# if not True == True:
#     print("hello!") #nope!
if True or False and False:
    print("hey!")

#check multiple conditions
if name == "Karis":
    print(name)
elif age == 24: #no else if! elif!
    print(age)
else:
    print("boo!")

#if statement with no context
if name == "Karis":
    pass

#ternary operator = conditional expression; allows testing a condition in a single line replacing the multiline if-else making the code compact
result = "John" if name == "John" else "Jane" #works!
# result = name == "Karis" and "Karis" or "Jane" #works!
print(result)

#nested if
if name == "Karis":
    if age == 24:
        print("Karis and 24")
    else:
        print("Not 24")
else:
    print("Not Karis")

#For Loop
primes = [2,3,5,7]
for i in primes:
    print(i)

#While Loop
count = 0
while count <5:
    print(count)
    count+=1

#exit loop
# count = 0
# while True:
#     print(count)
#     count+=1
#     if count >= 5:
#         pass #will loop forever!
count = 0
while True:
    print(count)
    count+=1
    if count >= 8:
        break

#skip current block and proceed to next loop
for x in range(10):
    if x%2 == 0:
        continue
    print(x)

#use else clause for a loop
count = 3
while count <12:
    print(count)
    count+=1
else:
    print("count value reached %d" %count)

#nested loop
names = ["Karis","Karl","Kayla","Kurt","Kale"]
foods = ["chips","popcorn","pretzels"]
for i in names:
    for j in foods:
        print(i + "likes" + j)

#infinite loop
# while names:
#     print(names.pop()) #pop removes item at given index from list and returns the removed item
# while True:
#     if not names:
#         break
#     print(names.pop()) #nope!
# do: #no do
# if not names:
#     break
# print(names.pop())
# while True #nope!
# for True:
#     if not names:
#         break
#     print(names.pop()) #nope! can't assign to true

# a = ['foo', 'bar', 'baz', 'qux', 'corge']
# while a:
#     if len(a) < 3:
#         continue
#     print(a.pop())
# print('Done.')

#correct way to iterate over range of numbers
for x in range(30):
    print(x)

#wrong way to implement a loop
x = 0
while True:
    print(x)
    x+=1
    if (x>4):
        break 

x = 10
while x < 20:
    print(x)
    x +=1

#print only even numbers
for x in range(10):
    if x%2 == 0:
        print(x)
    continue 

print("Alternatively...")

# for x in range(10):
#     if x%2 == 1:
#         break
#     print(x) #nope!

for x in range(10):
    if x%2 != 0:
        continue
    print(x)

#run exactly 10 iterations
# for n in range(1,10):
#     print(n) #nope!

for n in range(10,20,1):
    print(n)

#b = 23
a = 1
b = 2
while a<5:
    b += a
    a += 1

a = 1
b = 2
while a <10:
    b += a
    a += 2

a = 2
b = 3
while a <10:
    b+=a
    a+=2

print(b)
print(a)

#Functions

#define function
def myfunc(name,age):
    print(name + "is" + str(age) + "years old")

print(myfunc("Karis",24))
print(myfunc(name="Karis",age=23))

#does not return None
def func():
    print("Hello!")

print(func())

#recursive factorial calculator
def fact(x):
    if x ==1:
        return 1
    else:
        return(x*fact(x-1))
print(fact(4))

#https://book.pythontips.com/en/latest/args_and_kwargs.html

#use args #*args is used to send a non-keyworded variable length argument list to the function.
def func(name,age,*args): #*args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-key worded, variable-length argument list. The syntax is to use the symbol * to take in a variable number of arguments
    for v in args:
        print(v)

#use kwargs #**kwargs allows you to pass keyworded variable length of arguments to a function #**kwargs if you want to handle named arguments in a function
def func(name,age,**kwargs): #
    for v in kwargs:
        print(v)

#wrong way to use function
def sum(a,b):
    return a + b
def multiply(a,b):
    return a*b
print(multiply(sum(3,4),5))

# def sum(a,b):
#     def multiply(a,b):
#         return a*b
#     return a+b 
# print(multiply(sum(3.4),5)) #sum() missing 1 required positional argument: 'b'

def sum(a,b): return a + b
print(sum(3,4))

def func(name,age):
    def nest(a):
        return a + 1
    print("Next year" + name + "will be" + str(nest(age)))
func("Karis",24)

#lambda
# values = [1,2,3]
# multiples = map(lambda x: x*2,values)
# print(list(multiples))

#lamba with 2 args
add = lambda x,y:x+y 
print(add(3,2))

#define func which returns lambda fun that multiples number by given arg of original function
# def mult(x):
#     return lambda n:n*x 
# print(mult(2))

# def mult(x):
#     return lambda x:n*x
# print(mult(2))

# def func(x):
#     return lambda n,x: n*x
# print(func(2))

#wrong way of defining partial function with first arg prefilled as value 1
add = lambda x,y:x+y 
add2 = lambda x: add(x,5)
print(add2(3))

import functools
add = lambda x,y:x+y 
add2 = functools.partial(add,5)
print(add2(3))

add = lambda x,y:x+y 
def add2(x):
    return add(x,5)
print(add2(3))

# add = lambda x,y:x+y 
# add2 = add(5)
# print(add2(3))

#Classes and Objects

#create a class
class Person:
    name = "John"
    age = 23

print(type(Person))

#create instance object of class
class MyClass:
    pass
instance = MyClass()
print(instance)

#check if an object is an instance of the class
cat = "meow" 
print(isinstance(cat, MyClass)) #isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument)
print(isinstance(instance, MyClass))

#assign initial values to object properties when object is created
class Number:
    def __init__(self,value):
        self.value = value 
    
#example
class fruit:            
    def __init__(self,color,shape):      
               self.color=color                 
               self.shape=shape             
    def sayhi(self):         
               print(f"Hi.\nI am {self.color}and{self.shape}")       
orange=fruit('Orange','Round')
orange.sayhi()

#corect way to define object method    ##object = collection of data (variables) and methods (functions) that act on those data
# class Dog:
#     bark = def(self):
#         print("bark!") #nope!

# class Dog:
#     @method 
#     def bark():
#         print("bark!") #nope!

class Dog:
    def bark(self):
        print("bark!") #this one!!

# class Dog:
#     bark(self):
#     print("bark!") #nope!

#correct way to access current instance of class from its method

value = 2

# class MyClass:
#     def get_value(self):
#         return self::value  #nope!

# class MyClass:
#     def get_value():
#         return value 

class MyClass:
    def get_value(self):
        return self.value  #this one!

# class MyClass:
#     def get_value():
#         return this.value 

instance = MyClass()

#set property of object #https://www.geeksforgeeks.org/python-property-function/
class gfg:
    def __init__(self,value):
        self._value=value
    
    def getter(self):
        print("getting value")
        return self._value 

    def setter(self,value):
        print("setting value to" + value)

    def deleter(self):
        print("deleting value")
        del self._value

    value = property(getter,setter,deleter, )


# x = gfg("coding!").property(getter,setter,deleter)

x = gfg("Happy coding!")
print(x.value)

x.value = "Hey coder!" #here! set property of object
del x.value #deletes property of object
print(type(x))

#deleting an object
del x

#define subclass
#https://pybit.es/articles/python-subclasses/
#class SubClass(SuperClass)

class Boss(object):
    def __init__(self,name,attitude,behavior,face):
        self.name = name
        self.attitude = attitude
        self.behavior = behavior 
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behavior(self):
        return self.behavior

    def get_face(self):
        return self.face

class GoodBoss(Boss): #GoodBoss will inherit everything from Boss
    def __init__(self, name, attitude, behavior, face,laugh): #have to specify all attributes from Boss, but can add whatever GoodBoss attributes we want
        super().__init__(name,attitude,behavior,face) 
        self.laugh = laugh 

    def print_laugh(self):
        print(self.laugh)

    def nurture_talent(self):
        print("Employees feel great!")

    def encourage(self):
        print("Team cheers!")

karis = GoodBoss("Karis","Positive","Friendly","Smiling","Loud")

karis.print_laugh()

#shortest and correct way to create a class
class Empty: pass

print(type(Empty))

#call super class constructor when initializing subclass instance
#https://www.kite.com/python/answers/how-to-invoke-the-super-constructor-of-a-class-in-python#:~:text=Use%20super()%20to%20invoke,the%20constructor%20of%20the%20superclass.
class BadBoss(Boss):
    def __init__(self):
        super().__init__()
        print("Super constructor")

#correct way to create static method within class
#static methods, much like class methods, are methods that are bound to a class rather than its object
#method = function available for a given object because of object's type
#provide a way to divide the utility methods into separate sub-modules
#https://www.askpython.com/python/python-static-method
#class method can access class variables but static method can’t access class variables

# class Person:
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
    
#     @staticmethod
#     def full_name(cls,full):
#         first,last = map(str,full.split(' '))
#         return cls(first,last)

# person = Person.full_name("Karis Courey")

#wrong way to list class attributes
class MyClass:
    a = 1
    b = 2
instance = MyClass()
print(repr(instance)) #doesn't print class attributes!
# print(dir(instance))
# print(type(instance).__dict__)
# print(instance.__dir__())

#wrong way to overload operators in a class
#extending meaning of operators beyond their predefined operational meaning
#from https://www.programiz.com/python-programming/operator-overloading
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return "({0},{1})".format(self.x, self.y)

#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)
# p1 = Point(1,2)
# p2 = Point(2,3)

# print(p1+p2)

# class Number:
#     def __init__(self,value):
#         self.value = value
#     def __eq__(self,other):
#         return self.value == other.value #works!

# class Number:
#     def __init__(self,value):
#         self.value = value
#     def __mul__(self,other):
#         return Number(self.value * other.value) #works!

class Number:
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        return Number(self.value + other.value) #works!

# class Number:
#     def __init__(self,value):
#         self.value = value
#     def __str__(self,other):
#         return "The value is " + str(other.value) #doesn't work!

print(Number(2))

#use multiple inheritance
#from https://www.geeksforgeeks.org/multiple-inheritance-in-python/#:~:text=Inheritance%20is%20the%20mechanism%20to,would%20also%20inherit%20from%20P.
class Base1:
    pass

class Base2:
    pass

class Derived(Base1, Base2):
    pass


#define abstract class
#https://www.pythontutorial.net/python-oop/python-abstract-class/#:~:text=Python%20doesn't%20directly%20support,for%20defining%20abstract%20base%20classes.
#abstract class is a class that cannot be instantiated
#instantiated = creating a copy of the class which inherits all class variables and methods
#can create classes that inherit from an abstract class
from abc import ABC, abstractmethod
class Abstract(ABC):
    @abstractmethod
    def foo(self):
        pass 

#define private method
#from https://favtutor.com/blogs/python-private-methods
class Class:
  def __init__(self):
    self.__var = 2

  def __get_var(self):
    return self.__var


# #Dictionaries

# #wrong way to merge dictionaries
# dict_a = {"Me" : "Cat", "You" : "Dog"}
# dict_b = {"Her": "Bird", "Him": "Fish"}

# # new_dict = {}
# # new_dict.update(dict_a)
# # new_dict.update(dict_b) #works!

# # new_dict = {**dict_a,**dict_b} #works!

# # new_dict = dict_a + dict_b #this one doesn't work!

# new_dict = dict_a | dict_b  #works!

# print(new_dict)

# #check if member in dict
# if "Me" in new_dict:
#     print("it's in!") #works only for keys!

# # if new_dict.contains("Her"):
# #     print("yup!") #no attribute "contains"

# # if "Her" | new_dict:
# #     print("ok!") #nope!

# #remove item from dict
# # new_dict.remove("Me") #nope!
# del new_dict["Her"]
# # new_dict["Him"].delete() #nope!
# # new_dict["You"] = None #replaces value with None 
# print(new_dict)

# #wrong way to fetch keys in dict
# wow = {"Me" : "Cat", "You" : "Dog", "Her": "Bird", "Him": "Fish"}
# print(wow)
# keys = wow.keys() #works!
# # keys = [x for x in wow] #works!
# # keys = []
# # for x in wow:
# #     keys.append(x) #works!
# # keys = [x[1] for x in wow()] #doesn't work!
# print(keys)

# #fetch all values in dict
# values = wow.values()
# print(values)

# #empty dict
# wow.clear() 
# print(wow)

# #get value from dict that doesn't raise exception for missing keys
# d = {"a": 2, "c": 3}
# v = d.get("b") #https://stackoverflow.com/questions/6755655/handle-undeclared-dict-key-in-python#:~:text=If%20you%20want%20to%20get,if%20the%20key%20is%20missing.&text=To%20just%20check%20if%20a,in%20or%20not%20in%20keywords.
# print(v) 

# #set value in a way that doesn't override existing values
# # d.set("a",4,update=False) #no attribute set
# # d["a"] = 4 if "a" not in d else None #sets a to None
# # d.setdefault("a",4)
# d.setdefault("b",4) #works!
# # d["a"] = 4 #updates existing key value 
# print(d)

# #wrong way of deleting value of key "key" from dict
# d = {"Key": 2, "Key2": 3}
# # d.remove("Key") #no attribute remove!
# # del d["Key"] #works!
# # d.pop("Key",None) #works!
# # d = {key:val for key, val in d.items() if key != "Key"} #works!
# print(d)

# #wrong way of creating dict from 2 lists of keys and values
# keys, values = ["a","b","c"], [1,2,3]
# # d = dict(zip(keys,values)) #works!
# # d.fromkeys(keys,values) #doesn't work!
# # d = {}
# # for x in range(len(keys)):
# #     d[keys[x]] = values [x] #works!
# # d = {keys[x]:values[x] for x in range(len(keys))} #works!
# print(d)

# #Modules and Packages

# #import module
# # import Fibo

# #import object from module into current namespace
# # from Fibo import fib, fib2 
# # fib(50)

# #import all objects from module into current namespace
# # from Fibo import * 
# # fib(50)

# #import module under custom name
# # import Fibo as WOAH
# # WOAH.fib(20)

# #tell python interpreter where to search during import
# # PYTHONPATH=/Fibo.py #PYTHONPATH is environmental variable; specify additional directories to look for modules in
# # sys.path.append("/GitHub") #adds GitHub directory to list of paths to look for modules in; execute BEFORE running import

# #wrong way to explore imported module
# # import Fibo
# # help(Fibo)
# # print(Fibo.__dict__.keys())
# # print(repr(Fibo))
# # print(dir(Fibo))

# #conditionally import module
# # v = "cat"
# # if v == "cat":
# #     import Fibo as pet
# # else:
# #     import Sets as pet
# # pet.play()

# #prints hello when first imported #__init__ makes Python treat directories containing the file as packages
# import ImportPrintHello

# #import module from package  ##packages are just containers for modules or sub-packages
# #great resource: https://docs.python.org/3/tutorial/modules.html
# #dir1.dir2.my_module

# #access a module imported from a package
# #import dir1.dir2.my_module
# #print(dir(my_module))
# print(dir(ImportPrintHello))

# #specify imported module must be located within same package
# #https://realpython.com/absolute-vs-relative-python-imports/#:~:text=Relative%20imports%20make%20use%20of,that%20is%2C%20the%20directory%20above.
# #use dot notation to specify location
# #ssingle dot = module or package is referenced in same directory as current location
# #double dot = it is in parent directory of current location (e.g. directory above)
# #three dot = in grandparent directory, etc.
# #from .some_module import some_class
# #from ..some_package import some_function
# #from . import some_class

# #prevent names from being imported with "from... import*" statement
# # __hidden_name__ = "value"
# # __hidden_name = "value"
# # _hidden_name = "value"
# # private hidden_name = "value"
# #https://stackoverflow.com/questions/12117087/python-hide-methods-with
# #https://stackoverflow.com/questions/1547145/defining-private-module-functions-in-python


# #dynamically import module using function
# # name = "Fibo"
# # fibo = eval("import %s" %name)
# # print(fibo) #nope!
# # name = "Fibo"
# # fibo = import name
# # print(fibo) #nope!
# name = "Fibo"
# fibo = __import__(name) #yup!


# #List Comprehensions

# # #previous example ... output = [result for member in iterable if condition]
# # sentence = "the quick brown fox jumps over the lazy dog"
# # words = sentence.split()
# # word_lengths = [len(word) for word in words if word != "the"]
# # print(words)
# # print(word_lengths)

# # #create new list from list of numbers with only even numbers
# # numbers = [1,2,3,4,5,6,7,8]
# # even_numbers = [x for x in numbers if x%2==0]
# # print(even_numbers)

# # #capitalize a list of words
# # words = ["blue","cat","mouse"]
# # capped = [x.capitalize() for x in words]
# # print(capped)

# # #creat dict with cap keys out of another dict
# # d = {"me":"no","you":"yes","them":"ok"}
# # capped_d = {x[0].capitalize(): x[1] for x in d.items()}
# # print(capped_d)

# # #sum abs val of list
# # numbers = [-1,2,-3,4]
# # # sumabs = [abs(x) for x in numbers] 
# # # sumabs = [abs(x) for x in sum(numbers)]
# # # sumabs = sum([abs(x) for x in numbers])
# # # sumabs = [sum(abs(x)) for x in numbers]
# # # print(sumabs)

# # #omit filter in list comprehension
# # words = ["blue","cat","mouse"]
# # capped = [x.capitalize() for x in words]
# # print(capped) #don't include if

# # #create set of all letters used in string
# # # lets = [letter for letter in "hello"] #prints list, "h", "e", "l","l","o"
# # # lets = [letter for letter in "hello".split()] #prints list, "hello"
# # lets = {letter for letter in "hello"}
# # # lets = {letter for letter in set(["hello"])} #prints set, "hello"
# # print(lets)
# # print(type(lets))

# # #switch between keys and values of dict
# # dict = {"Yo":"Yes","No":"Nes","Wo":"Wes"}
# # revdict = {x[1]:x[0] for x in dict.items()}
# # print(revdict)

# # #all squares of numbers 0-9
# # sq = [x**2 for x in range(10)]
# # print(sq)

# # #get list of all numbers from 0-99 which are divisible by 3 and 5
# # div = [x for x in range(100) if x%3 == 0 if x%5 == 0]
# # print(div)

# # #flatten nested list (a list of lists of numbers)
# # list1 = [1,2,3,4,5]
# # list2 = [6,7,8,9,10]
# # list3 = [11,12,13,14,15]
# # listall = [list1,list2,list3]
# # flat = [x for y in listall for x in y]
# # print(flat)

# # #create list of tuples in range (0,0)-(2,2)
# # tups = [(x,y) for x in range(3) for y in range (3)]
# # print(tups)

