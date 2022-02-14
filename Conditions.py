#Conditions

#bool eval conditions (T/F)
#var assignment with = operator
#comparison with == operator
#not equals operator: !=

x = 2
print(x == 2) #prints true
print(x == 3) #prints false
print (x < 3) #prints true
print (x == 1+1) #prints true
print (x != 2) #prints false

#Boolean operators
name = "Karis"
name2 = "Karl"
age = 24
if name == "Karis" and age == 24:
    print("Your name is %s, and you are also %d." %(name,age))

if name == "Karis" or name == name2:
    print("Your name is %s or %s." %(name, name2))

#The "in" Operator

#can be used to check is specified object exists within an iterable object container

name = "Karis"
name2 = "Karl"
if name in ["Karl", "Karis"]:
    print("Your name is either %s or %s." %(name, name2))

#code blocks don't require termination nor brackets
#pass ends if statements
statement = False
statement2 = False
if statement is True:
    #do something
    pass
elif statement2 is True: #else if
    #do something else
    pass
else:
    #do another thing
    pass

x == 2
if x == 2:
    print("x equals 2!")
else:
    print("x doesn't equal 2.")

#statement is true if (1) true bool variable given or calculated (2) object which isn't considered empty is passed
#objects are empty e.g. empty string (""), empty list ([]), number 0, False

#The 'is' Operator
#is does not match the values of the variables but the instances themselves

x = [1,2,3]
y = [1,2,3]
print(x==y) #prints ture
print(x is y) #prints false

#The 'not' Operator
#using not before a bool expression inverts it

print(not False) #prints true
print ((not False) == (False)) #prints false
print (False is False) #prints true

#Exercise

number = 15.01
second_number = 0
first_array = [1,0,0]
second_array = [2,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

print(type(0))