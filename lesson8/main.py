# What is a Module in Python?
# In Python, a module is simply a file containing Python code — typically with a .py extension — 
# that can define functions, classes, and variables, and can also include runnable code.

# Types of Modules in Python

# Why use modules?
# Modules help you:

# Organize your code into manageable pieces

# Reuse code across multiple programs

# Avoid repetition

# Namespace separation, which helps prevent name conflicts

# math_utils.py
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b


# import math_utils # type: ignore

# print(math_utils.add(5, 3))        # Output: 8
# print(math_utils.subtract(5, 3))   # Output: 2


# import math
# print(math.sqrt(25))  # Output: 5.0


### **2.  User-Defined Modules (Custom Modules)**

# mymodule.py

# def greet(name):
#     return f"Hello, {name}!"

# def square(n):
#     return n * n



# lesson8.py

import mymodule  # Yeh line mymodule.py ka code yahan laati hai

print(mymodule.add(5, 3))  # Output: 8


# What is a Third-Party Module?

# 🔸 Example Usage of Popular Modules
# 📦 1. NumPy – for numerical computing
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr * 2)  # Output: [2 4 6 8]


# 📦 2. pandas – for working with data (like Excel)
import pandas as pd

data = {'name': ['Ali', 'Sara'], 'age': [25, 30]}
df = pd.DataFrame(data)

print(df)


# 📦 3. requests – for making HTTP requests (APIs)
import requests

response = requests.get("https://api.github.com")
print(response.status_code)       # 200
print(response.json())            # API response in JSON

# Example
import requests
response = requests.get("https://www.example.com")
print(response.status_code)

# How to Import a Module in Python?
# 1. Basic Import
import math
print(math.pi)

# 1. Import the whole module
import math

print(math.sqrt(25))  # Output: 5.0

# 2. Import with an alias (shortcut)
import math as m

print(m.sqrt(36))  # Output: 6.0

# 3. Import specific functions or classes
from math import sqrt, pi

print(sqrt(49))  # Output: 7.0
print(pi)        # Output: 3.141592653589793


# 4. Import everything (not recommended)
from math import *
print(sin(0))  # Output: 0.0



## **What’s Happening in This Namespace Overlap?**

from math import *
from numpy import *
print(pi) 

# Example
import math
print(math.sqrt(9))  # Here, sqrt belongs to math's namespace
