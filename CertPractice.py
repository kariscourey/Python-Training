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
from random import shuffle
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