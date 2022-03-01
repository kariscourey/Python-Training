#Map, Filter, Reduce

#allow programmer to write simpler, shorter code without loops and branching
#map and filter come built in with python (in __builtins__ module)
#reduce has to be imported with functools

#Map

#map() has following syntax:
#map(func,*iterables)
#func = function on which each element in "iterables" would be applied
# * on iterables - there can be as many iterables as possible 
#as long as function has that exact number as required input arguments
#returns map object (generator object)
#to get result as list, use list(map(func,*iterables))
#number of arguments to func must be the # of iterables listed
#passes each iterable element through a function and returns result of all elements having passed through function

#e.g. list (iterable) of my favorite pet names in lowercase, need uppercase
#traditionally
my_pets = ['alfred','joyce','arla']
uppered_pets = []

for item in my_pets:
    Pet = item.upper() #item.upper() = call function
    uppered_pets.append(Pet)

print(uppered_pets)

#with map
my_pets = ['alfred','joyce','arla']
uppered_pets = map(str.upper,my_pets) #do not need to call func as above, as map function does that on each element in my_pets
print(list(uppered_pets)) #str.upper = func; my_pets = ONE iterable

#circle rounding based on index
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round,circle_areas,range(1,7)))
print(result)

#no exception raised, stops when runs out of args
print("second argument short")
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round,circle_areas,range(1,3)))
print(result)

#no exception raised, stops when runs out of args
print("second argument long")
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round,circle_areas,range(1,9999)))
print(result)

#zip function takes number of iterables and created a tuple containing each of the elemnets in the iterables
#zip returns generator object

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]
results = list(zip(my_strings,my_numbers))
print(results)

#no exception raised, stops when runs out of args
my_strings = ['a', 'b', 'c']
my_numbers = [1, 2, 3, 4, 5]
results = list(zip(my_strings,my_numbers))
print(results)

#same as above
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)

#lambda example
add_one = lambda x:x+1
print(add_one(2))

#Filter
#filter(fund,iterable)
#filter() requires function to return bool values
#passes each iterable element through function and filters away the false

#key items
#only ONE iterable (not *)
#if func doesn't output boolean, filter simply returns iterable passed to it
#returns ONLY TRUE

#exam example
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def top_scores(grade):
    return grade > 75

top_scores_list = list(filter(top_scores,scores))
print(top_scores_list)

#palindrome detector example
potential_palindromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1],potential_palindromes))
print(palindromes)

#Reduce
#reduce(func,iterable[,initial])
#applies function of TWO arguments to iterable elements
#optionally starts with an initial argument
#initial = placed before element of iterable in calculation
#initial = serves as default when iterable is empty

#key notes
#func requires TWO arguments
#    first element in iterable (if initial isn't supplied; if it is, initial = 1st element)
#    second element in iterable (if initial is supplied, initial = first element and first element = second element)
#reduces iterable into a single value

from functools import reduce
numbers = [3,4,6,8,34,12]

def custom_sum(first,second):
    return first + second

result = reduce(custom_sum,numbers)
print(result)

#reduce takes first and second elements in numbers and passes them to custom_sum
#custom_sum computes their sum and returns it to reduce
#reduce then takes that result and applies it as the first element to custom_sum
#takes next element (third) in numbers as the second element to custom_sum
#does this continuously and cumulatively until numbers is exhausted

from functools import reduce
numbers = [3,4,6,8,34,12]

def custom_sum(first,second):
    return first+second

result = reduce(custom_sum,numbers,10)
print(result)

#Exercise
print("Exercise starts here...")

from functools import reduce

#use map to print square of each numbers rounded to 3 decimal places
my_floats =[4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
squared_floats = list(map(lambda x: round(x**2,3),my_floats))
print(squared_floats)

#use filter to print only names <= 7 letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

def short_names(name):
    return len(name) <= 7

short_names_list = list(filter(short_names,my_names))
print(short_names_list)

#use reduce to print product
my_numbers = [4,6,9,23,5]

def custom_product(first,second):
    return first*second

result = reduce(custom_product,my_numbers)
print(result)

#fix
print("Alternative solution...")
map_result = list(map(lambda x: round(x**2,3), my_floats))
filter_result = list(filter(lambda name: len(name)<=7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)