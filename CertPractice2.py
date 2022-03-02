#CertPractice2

#Regular Expressions

#import reg ex object
import re
pattern = r"\d+"
re_obj = re.compile(pattern)
# re_obj=re.match(pattern) #missing 1 required positional argument
# re_obj = r"\d+" #string
# re_obj = /\d+/ #invalid
print(type(re_obj))
print(re_obj)

#search for regex pattern at beginning of string
#https://www.guru99.com/python-regular-expressions-complete-tutorial.html#:~:text=match()%20function%20of%20re,it%20returns%20the%20match%20object.
#re.match() only searches first line (beginning of string)
#re.search() searchs ALL lines
string = "123"
if re.match(pattern,string):
    print("Found")

#search anywhere in string
string = "Some text. 123"
if re.search(pattern,string):
    print("Found!")

#split string by occurrences of regex pattern
string = "Some text. 123. Some text"
# occurrences = re.findall(pattern,string)
# print(string.split(occurrences)) #nope!
# re_obj = re.compile(pattern)
# print(string.split(re_obj)) #nope!
# print(string.split(pattern,type="regex")) #nope!
print(re.split(pattern,string))

#replace all occurrences of regex pattern in a string
string = "Some text. 123. Some text. 321"
replacement = "Some text"
# print(replacement.join(string.split(pattern)))
print(re.sub(pattern,replacement,string))

#wrong way to fetch all occurrences of regex pattern in string
string = "Some text. 123. Some text. 321"
re_obj = re.compile(pattern)
print(re_obj.findall(string))  #works!
# print(re_obj.search(string))  #doesn't work!
# print(re.findall(pattern,string)) #works!
# occurrences = re.finditer(pattern,string)
# print([o.group() for o in occurrences])  #works!

#find how many occurrences of regex pattern were replaced in a string
string = "Some text. 123. Some text. 321. 421"
replacement = "Some text"
# repcount = re.subn(pattern,replacement,string) #returns tuple
# result, repcount = re.sub(pattern,replacement,string) #nope!
result, repcount = re.subn(pattern,replacement,string)
print(repcount)
print(type(repcount))

#wrong way to get part of string where there was a match
pattern = r"\d+"
string = "Some text. 123"
matcho = re.match(pattern,string)
# print(matcho.group()) #no attribute group
# print(matcho[0]) #not subscriptable / nope!
# print(matcho.groups()[0]) #no attribute group
# print(matcho.group(0)) #no attribute group

#find substring that matched last capturing group of regex
pattern = r"(\d+)(\d+)?"
string = "123 text"
matcho = re.match(pattern,string)
# print(matcho.groups()[-1]) #returns none!
print(matcho.group(matcho.lastindex)) #works!
# print(matcho.groups()[matcho.lastindex]) #returns none!
# print (matcho.lastgroup) #returns none!

#contains two characters
#https://stackoverflow.com/questions/12871066/what-exactly-is-a-raw-string-regex-and-how-can-you-use-it
# '\n' #one character, containes newline
# r"\n" #\n = two characters
# r"\\n" #\\n = three characters
# r"{\n}" #

#wrong way to perform case-insensitive matching
pattern = r"hello"
string = "hEllo, how are you?"

re_obj = re.compile(pattern,re.IGNORECASE)
if re_obj.match(string):
    print("found")

re_obj = re.compile(pattern,re.I)
if re_obj.search(string):
    print("found!")

if re.findall(pattern, string, re.IGNORECASE):
    print("found!!")

# pattern = r"/hello/i"
# re_obj = re.compile(pattern)
# if re_obj.search(string):
#     print("found!!!") #doesn't work!

#split string by multiple delimiters
string = "Some text; 123, Some text, 123"
pattern = r"[,;]"
print(re.split(pattern,string))

#capture any two characters except newline between py and on
#https://www.w3resource.com/python/python-regular-expression.php
string = "python"
pattern = r"py..on"
if re.search(pattern,string):
    print("Found!")
else:
    print("ahh")

#specify pattern that captures shortest possible match
word = "Some text 'a', Some text 'b'"
# pattern = r"'(.?*)'" #doesn't work
# pattern = r"'(.*)'"
# pattern = r"'(.*??)'" #doesn't work
pattern = r"'(.*?)'"
reo = re.compile(pattern)
result = reo.findall(word)
print(result)

#returns match
string = '''multiline
string
'''
pattern = r"mul.+ing"
# pattern = r"mul(.\n)+ing"
# reo = re.compile(string) #works ... ['multiline\nstring\n']
# reo = re.compile(pattern,re.MULTILINE) #doesn't work
reo = re.compile(pattern,re.DOTALL) #works ... ['multiline\nstring']
# reo = re.compile(pattern) #doesn't work
print(reo.findall(string))

#pattern captures one or more whitespace characters

#(\S+) is a capture group that will match any string of non-whitespace characters
#\s+ - “any white space character, one or more times”

#wrong way to check if whole string matches pattern
string = "pythonn"
pattern = r"python"
if re.match(pattern,string):
    print("The whole string matches the pattern") #incorrect!!

# string = "pythonn"
# pattern = r"^python$"
# reo = re.compile(pattern)
# if reo.search(string):
#     print("The whole string matches the pattern")
    
# string = "pythonn"
# pattern = r"^python$"
# if re.match(pattern,string):
#     print("The whole string matches the pattern")

# string = "pythonn"
# pattern = r"python"
# if re.fullmatch(pattern,string):
#     print("The whole string matches the pattern")

#Exceptions
# mlist = [1,2,3]
# try:
#     mlist[5] = 0
# except IndexError():
#     print("mlist[5] not found") #nope!

# mlist = [1,2,3]
# try:
#     mlist[5] = 0
# catch (IndexError):
#     print("mlist[5] not found") #nope!

mlist = [1,2,3]
try:
    mlist[5]=0
except IndexError:
    print("mlist[5] not found")
    
# mlist = [1,2,3]
# try:
#     mlist[5]=0
# catch IndexError:
#     print("mlist[5] not found")

#trigger exception
# raise ValueError, "Error description" #nope!
# raise ValueError("Error description") #work!
# raise (ValueError,"Error description") #nope!

#wrong way to trigger exception
# raise ValueError() #works!
# raise "Error description" #doesn't work!
# raise ValueError #works!

#define custom exception type
#https://www.programiz.com/python-programming/user-defined-exception#:~:text=In%20Python%2C%20users%20can%20define,also%20derived%20from%20this%20class.
class MyException(Exception):
    pass

#catch instance of specific exception type
#https://www.programiz.com/python-programming/exception-handling#:~:text=Catching%20Specific%20Exceptions%20in%20Python&text=We%20can%20specify%20which%20exceptions,in%20case%20an%20exception%20occurs.
def fun():
    pass
try:
    fun()
except ValueError as e:
    print(e)

#specify same handler for multiple exception types
try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass

#wrong way to specify a handler for all exception types
try:
    num = int("string")
# except e:
#     print(e) #doesn't work
# except:
#     print("Exception caught") #works
# except Exception:
#     print("Exception caught") #works
except Exception as e:
    print(e) #works, access attributes of exception object

#define actions that should be executed, whether exception or not
try:
    num = int(2.2)
except ValueError:
    print("ValueError")
finally: #if else, does not execute except; if finally, executed if exception or not
    print("Finished")

#define actions that should be executed when there was no exception in try block
try:
    num = int(2)
except ValueError:
    print("ValueError!")
else: 
    print("No exception!")

#not built in exception type
#https://www.google.com/search?q=python+built+in+exception+types&rlz=1C1CHBD_enUS906US906&sxsrf=APq-WBt9nRspd5kWEbJ4vUd5rDrpaLojrg%3A1646263031346&ei=9_ofYvTiFKzB0PEPxM6t4Ao&ved=0ahUKEwi0usLZx6j2AhWsIDQIHURnC6wQ4dUDCA4&uact=5&oq=python+built+in+exception+types&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEOgcIABBHELADOgcIABCwAxBDOgQIIxAnOgQIABBDOgcIABCxAxBDOggIABCABBCxAzoICAAQsQMQkQI6BQgAEJECOgsIABCABBCxAxCDAToGCAAQFhAeSgQIQRgASgQIRhgAUOIOWNIlYMkmaAJwAXgAgAGNA4gBtCOSAQcwLjcuNi41mAEAoAEByAEJwAEB&sclient=gws-wiz

#reraise current exception
#https://www.geeksforgeeks.org/python-reraise-the-last-exception-and-issue-warning/
try:
    num = int(2)
except ValueError:
    raise

#conditionally raise and handle exception during debugging
x = False
try:
    assert x is True,"x must be true"
except AssertionError as e:
    print(e)

#customize how user-defined exception is displayed with "print"
class MyException(Exception):
    def __str__(self):
        return "Custom exception"

try:
    raise MyException()
except MyException as e:
    print(e)

#print traceback of exception being handled

# import traceback
# try:
#     raise MyException()
# except MyException:
#     traceback.print_exc() #prints!

# import traceback
# try:
#     raise MyException()
# except MyException as e:
#     traceback.print_tb(e.__traceback__) #doesn't print traceback

# import traceback
# try:
#     raise MyException()
# except MyException:
#     traceback.print_exception(*sys.exc_info()) #prints!

# import traceback
# try:
#     raise MyException()
# except MyException:
#     traceback.print_tb(sys.exc_info) #prints!

