#Multiple Function Arguments

#every fn receives predefined number of arguments, if declared normally

def myfunction(first,second,third):
    #do something with 3 variables
    ...

#possible to declare functions which receive a variable number of arguments, using following syntax
def foo(first, second, third, *therest):
    print("First: %s" %first)
    print("Second: %s" %second)
    print("Third: %s" %third)
    print("And all the rest... %s" %list(therest))

#therest variable = list of variables, which receives all arguments which were 
#given to the "foo" function after first 3 arguments

#call foo (1,2,3,4,5)
foo(1,2,3,4,5)

#possible to send functions arguments by keyboard (order of args doesn't matter)

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first #return exits a function and returns a value

result = bar(1,2,3,action="sum",number="first")
print("Result: %d" %result)

#bar function receives 3 arguments
#if additional action argument is received, it instructs on summing numbers and printing sum
#function also must return first argument if value of number = "first"

#Exercise
#fill in foo and bar so they can receive variable # args
#foo must return amount of extra arguments received
#bar must return true if arg with magicnumber is worth 7

# edit the functions prototype and implementation
def foo(a, b, c, *args): #if no keywords
    return len(args)
def bar(a, b, c, **wargs): #** if keywords
    if wargs.get("magicnumber") == 7:
        print(True)
    else:
        print(False)

# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")


#alternatively
print("alt solution")
def foo(a, b, c, *args): #if no keywords
    return len(args)
def bar(a, b, c, **wargs): #** if keywords
    return wargs["magicnumber"] == 7

# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")