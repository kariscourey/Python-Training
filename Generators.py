#Generators

#create iterators
#simple functions which return an iterable set of items, one at a time, in a special way

#uses "yield"
#when generator's function code reaches a yield, generator yields
#its execution back to the for loop, returning a new value from the set
#generator function can generate as many values (possibly infinite)

import random

def lottery():
    #returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1,40)

    #returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
    print("And the next number is ... %d!" %(random_number))

#decides how to generate random numbers on its own
#executes yield statements one at a time, pauses in between to yield execution back to main for loop

#Exercise
#write generator function which returns Fibonacci series
a = 1
b = 2
b,a = a,b
print(b,a)


# fill in this function
def fib():
    a,b = 1,1
    while 1:
        yield a
        a,b = b, a+b

    pass #this is a null statement which does nothing when executed, useful as a placeholder.

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib(): #generator activated down here in for loop
        print(n) #n in fib is what is yielded
        counter += 1
        if counter == 10:
            break