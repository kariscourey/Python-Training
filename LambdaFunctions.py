#Lambda Functions

#normally, define function using def keyword and call it whenever we need to use it
from doctest import OutputChecker


def sum(a,b):
    return a + b

a = 1
b = 2
c = sum(a,b)
print(c)

#instead of def function and calling it, can use lambda functions
#lambda functions = inline functions defined at same place we use it
#don't need to devlase function somewhere and revist code just for single time use
#don't need name; also called anonymous functions
#define lambda by using keyword lambda
#function_name = lambda inputs:output 

#above sume example
a = 1
b = 2
sum = lambda x,y: x + y
c = sum(a,b)
print(c)

#Exercise
#write using lambda to check if number in a given list is odd (bool)

l = [2,4,7,3,14,19]
odd = lambda x,y:x%y==0

for i in l:
    if odd(i,2):
        print(False)
    else:
        print(True)

#alternatively
print("alternate solution")
l = [2,4,7,3,14,19]
for i in l:
    odd_alt = lambda x:x%2 == 1
    print(odd_alt(i))

#alternatively
print("alternate solution2")
l = [2,4,7,3,14,19]
for i in l:
    odd_alt2 = lambda x:x%2 == 1
    print(odd_alt2(i))