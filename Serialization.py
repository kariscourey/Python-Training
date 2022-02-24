#Serialization

#py provides built in JSON libraries to encode and decode json

import json

#datastructure = lists and dictionaries inside each other

#JSON data either in string or datastructure
#datastructure = lists and dictionarites inside each other
#datastructure allows one to use python methods (for lists and dictionaries)
#to add, list, search, and remove elements
#string used to pass data into anotjer program or load into a DS

#to load JSON back to DS, use "loads" method; LOADS to JSON
#loads takes string and turns it into JSON obj DS

#to encode DS to JSON, use "dumps"
#dumps takes object and returns string; DUMPS to STRING

import json
json_string = json.dumps([1,2,3,"a","b","c"])
print(json_string)

print(json.loads(json_string))

#Pickle = python serialization method, used same way

import pickle
pickled_string = pickle.dumps([1,2,3,"a","b","c"])
print(pickle.loads(pickled_string))

#Exercise
#print out JSON string w key value pair ME:800 added to it

print("Exercise starts here...")

import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    substring = salaries_json[:-2]
    salaries_json = substring + ', "' + name + '" : ' + str(salary) + "}"
    return salaries_json

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
print(new_salaries)
print("new_salaries type: " + str(type(new_salaries)))

decoded_salaries = json.loads(new_salaries)
print(decoded_salaries)
print("decoded_salaries type: " + str(type(decoded_salaries)))

print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])

#alternatively
print("Alternative solution...")

import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
