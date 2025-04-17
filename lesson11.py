# Lesson 11: The Math & Date Time Calendar ⏱🕖📆

# In this lesson, we'll explore how to work with math operations and how to handle date and time with Python’s built-in libraries.

# 1. Math Operations in Python
# Python provides a math module that provides mathematical functions. We also have some built-in operations that are useful for calculations.

# 1.1 Basic Arithmetic Operations
# You can perform basic arithmetic directly in Python:

# Addition
a = 10 + 5  # 15

# Subtraction
b = 10 - 5  # 5

# Multiplication
c = 10 * 5  # 50

# Division
d = 10 / 5  # 2.0 (float division)

# Floor Division (divides and returns the integer part)
e = 10 // 3  # 3

# Modulo (remainder of division)
f = 10 % 3  # 1

# Exponentiation (power)
g = 2 ** 3  # 8

# Example
import math

# Square root
print(math.sqrt(25))  # 5.0

# Factorial
print(math.factorial(5))  # 120

# Pi constant
print(math.pi)  # 3.141592653589793

# Exponential
print(math.e)  # 2.718281828459045

# Trigonometry
angle = math.radians(45)  # Convert 45 degrees to radians
print(math.sin(angle))  # sin(45°)


# 1.3 Rounding Numbers
# You can round numbers in Python using:


x = 3.14159

# Round to the nearest integer
rounded_value = round(x)  # 3

# Round to a specific number of decimal places
rounded_value_2 = round(x, 2)  # 3.14
# 1.4 random Module for Random Numbers
# If you need to generate random numbers, Python’s random module can be helpful:


import random

# Generate a random integer
print(random.randint(1, 100))  # Random integer between 1 and 100

# Generate a random floating-point number
print(random.random())  # Random float between 0.0 and 1.0
# 2. Date and Time with Python
# Python’s datetime module allows you to work with dates and times in a variety of ways.

# 2.1 Getting the Current Date and Time
# The datetime module is essential for working with dates and times. You can get the current date and time as follows:


from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()
print(current_datetime)  # Example: 2025-04-17 14:30:00.123456
# 2.2 Date Formatting
# You can format the date and time in various ways using strftime(). The strftime() method allows you to specify the format.


current_datetime = datetime.now()

# Format: Year-Month-Day Hour:Minute:Second
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)  # Example: 2025-04-17 14:30:00

# Format: Day-Month-Year
formatted_date2 = current_datetime.strftime("%d-%m-%Y")
print(formatted_date2)  # Example: 17-04-2025
# 2.3 Creating Dates
# You can create a date object by specifying the year, month, and day:

from datetime import date

# Create a specific date
specific_date = date(2025, 4, 17)
print(specific_date)  # Output: 2025-04-17
# 2.4 Date Arithmetic
# You can perform operations like addition or subtraction with dates and times. The timedelta class is used for this purpose.


from datetime import timedelta

# Subtracting a specific number of days from today
today = datetime.now()
ten_days_ago = today - timedelta(days=10)
print(ten_days_ago)  # Output: 2025-04-07 14:30:00 (example)

# Adding 1 month to the current date (assuming 30 days in a month)
next_month = today + timedelta(days=30)
print(next_month)
# 2.5 Working with Timezones
# The datetime module allows you to work with time zones using the timezone class. Here’s how you can use it:


from datetime import timezone

# Get current time with UTC timezone
utc_time = datetime.now(timezone.utc)
print(utc_time)  # Example: 2025-04-17 14:30:00+00:00
# 2.6 Parsing Strings into Date Objects
# If you have a string that represents a date, you can use strptime() to convert it into a datetime object:


date_string = "17-04-2025 14:30:00"
parsed_date = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
print(parsed_date)  # Output: 2025-04-17 14:30:00
# 3. Calendar Module
# The calendar module provides functions related to the calendar, such as getting the days of the week, leap years, and printing entire calendars.

# 3.1 Printing a Calendar
# To print a month or an entire year’s calendar:


import calendar

# Print the calendar for a specific month
print(calendar.month(2025, 4))  # April 2025

# Print the entire year’s calendar
print(calendar.calendar(2025))
# 3.2 Checking for Leap Year
# You can check if a year is a leap year using the isleap() function:


# Check if a year is a leap year
print(calendar.isleap(2025))  # False
print(calendar.isleap(2024))  # True
# 3.3 Getting the Day of the Week
# You can use the weekday() function to find out which day of the week a specific date falls on:


# Get the day of the week for a specific date
day_of_week = calendar.weekday(2025, 4, 17)
print(day_of_week)  # Output: 3 (Thursday)


# Why is there an epoch?
# The epoch is a fixed point in time that computers use as a reference to calculate and represent dates and times.
from datetime import datetime

# Get the epoch
epoch = datetime.utcfromtimestamp(0)
print("Epoch starts at:", epoch)  # Output: Epoch starts at: 1970-01-01 00:00:00


# Example
import time # This is required to include time module.
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

# Getting the Current Time
import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

# Python Math Module
import math

# abs() returns the absolute value of a number
# In Python, abs() is a built-in function, which means it's a global function
# available in the standard library without needing to import any specific modules.
# You can use it directly in your code.
print("abs(-5) = ", abs(-5))  # outputs: 5

# pow() raises a number to a power
print("pow(2, 3) = ", pow(2, 3))  # outputs: 8

# round() rounds a number to a specified number of decimal places
print("round(3.14159, 2) = ", round(3.14159, 2))  # outputs: 3.14

# max() returns the largest of a set of numbers
print("max(1, 2, 3, 4, 5) = ", max(1, 2, 3, 4, 5))  # outputs: 5

# min() returns the smallest of a set of numbers
print("min(1, 2, 3, 4, 5) = ", min(1, 2, 3, 4, 5))  # outputs: 1

# math.sin() returns the sine of an angle in radians
print("math.sin(math.pi/2) = ", math.sin(math.pi/2))  # outputs: 1.0

# math.cos() returns the cosine of an angle in radians
print("math.cos(0) = ", math.cos(0))  # outputs: 1.0

# math.tan() returns the tangent of an angle in radians
print("math.tan(math.pi/4) = ", math.tan(math.pi/4))  # outputs: 1.0

# math.sqrt() returns the square root of a number
print("math.sqrt(9) = ", math.sqrt(9))  # outputs: 3.0

# math.factorial() returns the factorial of a number
print("math.factorial(5) = ", math.factorial(5))  # outputs: 120

# math.log() returns the natural logarithm of a number
print("math.log(10) = ", math.log(10))  # outputs: 2.302585092994046

# math.log10() returns the base-10 logarithm of a number
print("math.log10(100) = ", math.log10(100))  # outputs: 2.0

# math.exp() returns the value of e raised to a power
print("math.exp(2) = ", math.exp(2))  # outputs: 7.38905609893065

# math.ceil() returns the smallest integer greater than or equal to a number
print("math.ceil(4.7) = ", math.ceil(4.7))  # outputs: 5

# math.floor() returns the largest integer less than or equal to a number
print("math.floor(4.7) = ", math.floor(4.7))  # outputs: 4

# math.pi is a constant representing the ratio of a circle's circumference to its diameter
print("math.pi = ", math.pi)  # outputs: 3.14159265359

# math.e is a constant representing the base of the natural logarithm
print("math.e = ", math.e)  # outputs: 2.718281828459045

# math.tau is a constant representing the ratio of a circle's circumference to its radius
print("math.tau = ", math.tau)  # outputs: 6.283185307179586

# math.inf is a constant representing infinity
print("math.inf = ", math.inf)  # outputs: inf

# math.nan is a constant representing "not a number"
print("math.nan = ", math.nan)  # outputs: nan