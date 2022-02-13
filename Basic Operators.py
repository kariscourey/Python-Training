#Basic Operators

#Arithmetic Operators

#follows order of operations
number = 1 + 2*3 / 4.0
print(number)

#modulo
remainder = 11%3
print(remainder)

#power
squared = 7**2
cubed = 2**3
print(squared)
print(cubed)

#Using Operators with Strings

#concetante
helloworld = "hello" + " " + "world"
print(helloworld)

#multiply string to form a string with a repeating sequence
lotsofhellos = "hello" * 10
print(lotsofhellos)

#Using Operators with Lists
	
#lists can be joined with addition ops
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#form new lists with repeating sequence using multiplication op
print([1,2,3]*3)

#Exercise

x = object()
y = object()

myval = 10

x_list = [x]*myval
y_list = [y]*myval
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == myval and y_list.count(y) == myval:
	print("Almost there...")
if big_list.count(x) == myval and big_list.count(y) == myval:
	print("Great!")