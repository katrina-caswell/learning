Python as a calculator

```
print(5 + 5)
  10
print(5 - 5)
  0
print(3 * 5)
  15
print(10 / 7)
  1.4285714285714286
# Modulo: returns the remainder of the division of the number to the left by the number on the right
print(18 % 7)
  4
# Exponentiation: raises the number to its left to the power of the number to its right
print(4 ** 2)
  16
```

```
# You have £100, which you can invest with a 10% return each year. How much is £100 worth after 7 years?
print(100 * 1.1 ** 7)
  194.87171000000012
```

Calculations with variables

```
savings = 100
growth_multiplier = 1.1
year = 7
result = savings * growth_multiplier ** year
print (result)
  194.87171000000012
```

Determine data type of variable

```
print(type(growth_multiplier))
  <class 'float'>
```

Converting data types to concatenate a string

```
savings = 100
result = 100 * 1.10 ** 7
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")
```

Slicing Lists

```
# Remember how 0 indexing works, and that slicing this way [a:b] is inclusive of a and exclusive of b
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
downstairs = areas[0:6]
upstairs = areas[6:10]
bwords = areas[-4:]
print(downstairs)
print(upstairs)
  ['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0]
  ['bedroom', 10.75, 'bathroom', 9.5]
  ['bedroom', 10.75, 'bathroom', 9.5]
```

Deleting list items

```
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
del(areas[-4,-2])
# This code will remove poolhouse and 24.5 from the above list
```

Explicit list copying

```
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = list(areas)
# If the above copy said areas_copy = areas, then any changes made to areas_copy would also change areas
areas_copy[0] = 5.0
print(areas)
```

Builtin functions:
* print
* str, int, bool, float
* type
* max
* round
* help
* len (length)
* pow (x to power of y)
* sorted (defaults ascending)
* index
* append
* remove
* reverse


```
list = [4, 56, 67, 9]
list_sorted = (sorted((list),reverse=True))
```

Example of count method
```
# string to experiment with: place
place = "poolhouse"
# Use upper() on place: place_up
place_up = str.upper(place)
# Print out place and place_up
print(place, place_up)
# Print out the number of o's in place
print(place.count('o'))
```

Testing math package to use pi
```
# Import the math package
import math as m
# Calculate C
C = (2*m.pi*r)
# Calculate A
A = (m.pi*(pow(r,2)))
# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))
```

Using numpy to check which parts of a list fall under certain conditions
```
# height_in and weight_lb are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
```

Generating data

```
#To generate data you can use np.random.normal(), its arguments are distribution mean, distribution standard deviation, and number of samples
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height, weight))
```

Text files
```
file = open('moby_dick.txt', mode='r')
print(file.read())
file.close()
print(file.closed)

with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
```

Plotting data
```
import numpy as np
file = 'digits.csv'
digits = np.loadtxt(file, delimiter=',')
print(type(digits))
# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))
# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

file = 'seaslug.txt'
data = np.loadtxt(file, delimiter='\t', dtype=str)
print(data[0])
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)
print(data_float[9])
# Scatter plot
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()
```

Pandas dataframes, missing data
```
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = 'titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
```

Pickle
```
import pickle
with open('data.pkl', 'rb') as file:
  d = pickle.load(file)
print(d)
print(type(d))
```

Excel
```
import pandas as pd
file = 'battledeath.xlsx'
xls = pd.ExcelFile(file)
print(xls.sheet_names)
```

Loading sheets by name or index
```
df1 = xls.parse('2004')
print(df1.head())
df2 = xls.parse(0)
print(df2.head())
```

Assigning columns names
```
# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=[0], names=['Country','AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())
```
