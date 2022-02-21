#Numpy Arrays

#alternatives to Python lists
# Numpy arrays are fast, easy to work with, give users opportnity to perform calcs across entire arrays

#two lists > import numpy package > create numpy arrays

#create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# import numpy package as np
import numpy as np

# numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

#print out type of np_height
print(type(np_height))

#Element-wise calculations

#now we can perform element-wise calcs on height and weight
#can take all 6 of height and weight and calculate BMI for each observation with single eq
#helpful with 1000s of observations in data due to computational efficiency

#calculate bmi
bmi = np_weight / np_height ** 2
print(bmi)

#Subsetting

#ability to subset -- if want to konw which observations in BMI are above 23, can quickly find out

#for boolean response
bmi > 23

#print only observations above 23
bmi[bmi > 23]

#Exercise
#convert list of weight from a list to a numpy array; convert all weights from kg to lbs; print result

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# create a numpy np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# print np_weight_lbs
print(np_weight_lbs)