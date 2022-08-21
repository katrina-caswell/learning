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
