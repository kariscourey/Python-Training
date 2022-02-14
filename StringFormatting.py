#String Formatting

#tuple = fixed size list
#% formats set of variables enclosed in a tuple, together with a format string, which contains normal text together with argument specifiiers (i.e. %s, $d)

#This prints out "Hello, ___!"

name = "Karl"
print("Hello, %s!" %name)

#to use 2+ argument specifiers, use a tuple (parantheses)
name = "Karis"
age = 24
print("%s is %d years old." %(name, age))
#print("%s is %d years old." %(age, name))
print("%s is %s years old." %(name, age))

#This prints out: A list: [1,2,3]; other variable types can be written as str
mylist = [1,2,3]
print("A list: %s" %mylist)

# %s - string
# %d - integers
# %f - floating point numbers
# %.<number of digits>f - floating point number with fixed number of digits to right of dot
# %x/%X - integers in hex representation (lowercase/uppercase)

#Exercise
data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string + " %s %s. Your current balance is $%.2f." %data)
