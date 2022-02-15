#Dictionaries

#similar to arrays
#works with keys and values instead of indices
#each val stored in a dict can be accessed using a key (any type of object - string, number, list, etc.)

#database of phone numbers
phonebook = {}
phonebook["Karl"] = 938477566
phonebook["Karis"] = 981720301
phonebook["Pie"] = 912897301
print(phonebook)

#dictionary can be initialized with same values as follows
phonebook = {
    "Karl"  : 118477566,
    "Karis" : 136720301,
    "Pie"   : 114897301
}
print(phonebook)

#iterating over dictionaries

#dictionaries can be iterated over just like a list
#dictionary, unlike list, does not keep order of the values stored in it

#iterate over key-value pairs
phonebook = {"Karis" : 1209282, "Karl" : 1298231, "Pie" : 1029811}
for name, number in phonebook.items():
    print("Phone number of %s is %d" %(name, number))

#removing a value
phonebook = {
    "Karl"  : 888477566,
    "Karis" : 886720301,
    "Pie"   : 884897301
}
del phonebook["Karl"]
print(phonebook)

#or
phonebook = {
    "Karl"  : 888477566,
    "Karis" : 886720301,
    "Pie"   : 884897301
}
del phonebook["Karl"]
phonebook.pop("Karis") #pop deletes from dictionaries!
print(phonebook)

#Exercise

#Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
print("Exercise starts here.")

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here
del phonebook["Jill"]
phonebook["Jake"] = 938273443 #super neat and easy to add to phonebook!
#phonebook["John"] = 12809123 #overrides previous john
#phonebook["Jill"] = 947662781 #adds jill back in, any number

# testing code
print(phonebook)

if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.") 

if "Jill" not in phonebook and "Jake" in phonebook:
    print("yay!")