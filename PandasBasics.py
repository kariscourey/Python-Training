#Pandas Basics

#pandas = high-level data manipulation tool
#built on numpy package; key data structure = DataFrame

#DataFrames allow to store and manipulate tabular data in rows of observsations and columns of variables

#row = observation; column = variable

#create a DataFrame using a dictionary

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
"capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
"area": [8.516, 17.10, 3.286, 9.597, 1.221],
"population": [200.4, 143.5, 1252, 1357, 52.98]}

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

#     area    capital       country  population
# 0   8.516   Brasilia        Brazil      200.40
# 1  17.100     Moscow        Russia      143.50
# 2   3.286  New Dehli         India     1252.00
# 3   9.597    Beijing         China     1357.00
# 4   1.221   Pretoria  South Africa       52.98

#key is 0-4

#can change keys

#set index for brics
brics.index = ["BR", "RU","CH","SA"]
print(brics)

#can also create DataFrame by importing csv file using Pandas

#import pandas
import pandas as pd

#import cars.csv file data:cars
cars = pd.read_csv('cars.csv')
print(cars)

#Indexing Frames
#several ways to index a Pandas DataFrame
#easiest way = square bracket notation
#can use square brackets to select one column of the cars DataFrame
#can use single or double bracket
#single bracket will output Pandas series
#double bracket will output Pandas DataFrame

#import pandas and cars.csv
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

#print country column as Pandas Series
print(cars['cars_per_cap'])

#print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])

#print out DataFrame with country and drives_rigtht columns
print(cars[['cars_per_cap','country']])

#square brackets can also be used to access observations (rows) from DataFrame

#import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

#print out first 4 observations
print(cars[0:4])

#print out fifth and sixth observation
print(cars[4:6])

#can also use loc and iloc to perform most data selection operations
#loc = label-based (you have to specify rows and columns based on row and column labels)
#iloc = integer-based (specify based on integer index)

#import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

#print Japan observation
print(cars.iloc[2])

#print out observations for Aus and Egypt
print(cars.loc[['AUS','EG']])

