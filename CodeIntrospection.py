#CodeIntrospection

#code introspection = ability to examine classes, functions, keywords
#to know what they are, what they do, and what they know

#python provides several functions and utilities for code intropsection

# help()
# dir()
# hasattr()
# id()
# type()
# repr()
# callable()
# issubclass()
# isinstance()
# __doc__
# __name__

#can use help to figure out what other functions do

#Exercise

# help(dir)
# help(hasattr)
# help(id)

# Define the Vehicle class.
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.
# Your code goes here

print(dir(Vehicle))