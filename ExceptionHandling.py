#Exception Handling

#needed for bad input, network resource unavailable, program ran out of memory, programmer made mistake
#solutions to error = exception

# print(a)

#error
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
# NameError: name 'a' is not defined 
# </module></stdin>

#forgot to assign a value to a variable

#sometimes don't want exceptions to stop program... might want to do something else instead
#this is done with Try/Except block

#e.g. iterating over list
#need to iterate over 20 numbers but list is amde from user input and might not have 20 numbers in it
#after reach end of list, you just want rest of numbers to be interpreted as 0

def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1,2,3,4,5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: #Raised when accessing a non-existing index of a list
            do_stuff_with_number(0)

catch_this()

#Exercise
#handle all exceptions
print("Exercise starts here...")

# Setup
actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!
def get_last_name(): 
    try: 
        return actor["name"].split()[1]
    except KeyError:
        print("No last name!")

# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())