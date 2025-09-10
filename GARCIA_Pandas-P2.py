#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd
cars = pd.read_csv('cars.csv')

cars_a = cars.iloc[:5, ::2]
print(cars_a)

cars_b = cars[cars["Model"] == "Mazda RX4"]
print(cars_b)

cars_c = cars[cars["Model"] == "Camaro Z28"]["cyl"]
print(cars_c)

cars_d = cars[cars["Model"].isin(["Mazda RX4 Wag", "Ford Pantera L", "Honda Civic"])][["cyl", "gear"]]
print(cars_d)


# In[ ]:




