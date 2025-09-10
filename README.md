# Experiment-3

PROBLEM 1
Initial step was to import pandas as pd, then use the code for jupyter to read the cvs file
```python
import pandas as pd
cars = pd.read_csv('cars.csv')
```
After that was to identify the first and last 5 data on the given file
```
To show the output simply print the input
```python
print(cars.head())
print (cars.tail())
```

PROBLEM 2
Using the same initial step in Problem 1 since the data to be used is the same

```python
cars_a = cars.iloc[:5, ::2]
print(cars_a)
```

Then find the rows where the model column equals Mazda RX4
```python
cars_b = cars["Model"] == "Mazda RX4" 
```
This creates a boolean mask (True for rows that match).
```python
cars[ mask ]
```
 applies that mask to keep only matching rows

I print the full row(s) for "Mazda RX4"
```python
print(cars_b)
```

Find the Camaro Z28 row, then read its cylinder number, then print the output
```python
cars_c = cars[cars["Model"] == "Camaro Z28"]["cyl"]
print(cars_c)
```
Pick three car models, then only show the cylinders and gears
```python
cars_d = cars[cars["Model"].isin(["Mazda RX4 Wag", "Ford Pantera L", "Honda Civic"])][["cyl", "gear"]]
print(cars_d)
```
