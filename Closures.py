#Closures

#closure = functoin object that remembers values in enclosing scopes even if they are not present in memory

#nested function = function defined inside another function
#can access variables of the enclosing scope
#in python, variables of the enclosing scope are read only
#can use "nonlocal" keyword explicitly with variables to modify them

def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()

print(transmit_to_space("Test message"))

#data transmitter fn can access the "message" 

#nonlocal keyword
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number = 3
        print(number)
    printer()
    print(number)

print_msg(9)

#without nonlocal keyword, output would be 3 9
#with its usage, we get 3 3
#the value of the "number" variable gets modified

def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        number = 3
        print(number)
    printer()
    print(number)

print_msg(9)

#RETURN rather than CALL .. return function object rather than calling the nested function within (functions are objects in python)
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    return data_transmitter

ahhh = transmit_to_space("Burn the sun!")
ahhh()

#even though execution of "transmit_to_space()" was completed, message was rather preserved
#closures = data is attached to some code even after end of those other original functions
#closures can avoid use of global variables and provides some form of data hiding (e.g. when there are few methods in a class, use closures instead)

#Exercise
#make nested loop and python closure to make functions to get multiple multiplication functions using closures


def multiplier_of(choice):
    "This is the enclosing function"
    def multiply(choice2):
        "The nested function"
        return choice*choice2
    return multiply

multiplywith5= multiplier_of(5)
print(multiplywith5(9))