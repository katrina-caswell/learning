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
