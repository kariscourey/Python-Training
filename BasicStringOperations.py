#Basic String Operations

#string = anything between quotes

astring = "Hello world!"
astring2 = 'Hello world!'

#to assign the string in these bracket(single quotes are ' ') you need to use double quotes only like this
#prints out 12

astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

#prints out 4 because location of first occurrence of letter "o" is 4 characters away from the first character ... this method only recognizes the first "o"

astring = "Hello world!"
print(astring.index("o"))

#index starts with 0
#below counts number of "L"s in the string ... should print 3

astring = "Hellow world!"
print(astring.count("l"))

#prints out slice of string, starting at ind = 3 and ending at ind = 6
#ind 3 - ind 6 ... NOT ind 3 - ind 7
#first = inclusive, last = exclusive
#one number in brackets = single character at index
#leave out the first number and keep colon? slice = start to the number typed in
#leave out second number? slice from indicated index to end

astring = "Hello world!"
print(astring[3:7])

#can put negative numbers inside brackets - starts at end of string rather than beginning
#-3 means 3rd character from the end

astring = "Hello world!"
print(astring[-1])
print(astring[-8:-1])
print(astring[0:-1])

#prints characters from ind 3 to ind 6, skipping one char
#[start:stop:step]
astring = "0123456789"
print(astring[3:7:2])
print(astring[3:7:1])
print(astring[3:9:1])
print(astring[3:10:2])
print(astring[3:10:1])

#can reverse a string

print(astring[::-1])

#converts all letters to upper/lower

astring = "Hello world!"
print(astring.upper())
print(astring.lower())

#determines if (bool) string starts or ends with something

print(astring.startswith("Hello"))
print(astring.endswith("asdasdlas"))

#splits strings into strings grouped in a list, exclusive of delimiter
astring = "Hello world my old friend!"

afewwords = astring.split(" ")
print(afewwords)

nobang = astring.split("!")
print(nobang)

#Exercise
s = "Streets and welcome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))