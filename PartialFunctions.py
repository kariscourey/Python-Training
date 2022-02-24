#Partial Functions
#can create partial functions by using partial function from functools library

#partial functions allow one to derive a function with x parameters to a function with
#fewer parameters and fixed values set for the more limited function

#import
from functools import partial

#returns 8
def multiply(x,y):
    return x*y

#create new function that multiples by 2
dbl = partial(multiply,2)
print(dbl(4))

#default values will start replacing variables from the left
#2 will replace x, y will be 4 when dbl(4) is called

#Exercise
#call partial() and replace first 3 variables in funct()
#print new partial fn using 1 input variable
#output = 60

#Following is the exercise, function provided:
from functools import partial
def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x

exercise = partial(func,6,6,6)
print(exercise(6))