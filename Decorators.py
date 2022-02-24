#Decorators

#http://wiki.python.org/moin/PythonDecoratorLibrary

#allow to make simple modifications to callable objects like functions, methods, classes
#functions used in this tutorial

# @decorator
# def functions(arg):
#     return "value"

# equivalent to

# def function(arg):
#     return "value"
# function = decorator(function) #this passes the function to the decorator and reassigns it to the functions

#decorator is another function which takes functions and returns one

#make new_function = old_function repeated (2x)
def repeater(old_function):
    def new_function(*args,**kwds):
        old_function(*args,**kwds) #run old function
        old_function(*args,**kwds) #do it twice
    return new_function #we have to return new_function or it wouldn't reassign it to the value

@repeater
def multiply(num1, num2):
    print(num1*num2)

multiply(2,3)

#can make it change output
def double_out(old_function):
    def new_function(*args,**kwds):
        return 2*old_function(*args,**kwds) #modify return value
    return new_function

#change input
def double_Ii(old_function):
    def new_function(arg): #only works if the old function has one argument
        return old_function(arg*2) #modify the argument passed
    return new_function

#do checking
def check(old_function):
    def new_function(arg):
        if arg < 0: raise (ValueError, "Negative Argument") #this causes an error, which is better than it doing the wrong thing
        old_function(arg)
    return new_function

#multiply output by a variable amount
def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args,**kwds):
            return multiplier*old_function(*args,**kwds)
        return new_function
    return multiply_generator #returns the new generator

#usage
@multiply(3) #multiply is not a generator, but multiply (3) is
def return_num(num):
    return num 

#now return_num is decorated and reassigned to itself
print(return_num(5)) #should print 15

#Exercise
#not done!!