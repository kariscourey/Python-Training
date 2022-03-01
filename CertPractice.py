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

