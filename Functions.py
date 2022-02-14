#Functions

#divide code into useful blocks, allowing us to order code, make it readable, reuse it, save time
#key to define interfaces so programmers can share code
#block = area of code


# block_head:
#     1st block line 
#     2nd block line 

#block head is of the following format: block_keyword block_name
#block keywords are if, for, while, etc.

#functions are defined using block keyword "def," followed with the function's name as the block's name

def my_function():
    print("Hello from My Function!")

my_function()

#functions can also receive arguments (variables passed from the caller to the function)

def my_function_with_args(username, greeting):
    print("Hello, %s, from My Function!, I wish you %s" %(username,greeting))

my_function_with_args("karis","a wonderful day!")

#functions may return a value to caller using keyword "return"

def sum_two_numbers(a,b):
    return a + b 

print(sum_two_numbers(1,2))

def return_42():
    return 42 #an explicit return statement

print(return_42())

num = return_42()
print(num)

#calling functions with python
#write functions name followed by ()

#define 3 functions
def my_function():
    print("Hello from My function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, from My function!, I wish you %s" %(username, greeting))

def sum_two_numbers(a,b):
    return a+b

#print (a simple greeting)
my_function()

#prints - Hello, Karis, from My funtion! I wish you a great year!
my_function_with_args("Karis","a great year!")

#x will hold value 3!
x = sum_two_numbers(1,2)
print(x)

#Exercise
# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code","More readable code","Easier code reuse","Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    #return benefit + " is a benefit of functions!"
    return "%s is a benefit of functions!" %benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

