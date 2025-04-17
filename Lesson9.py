# Lesson 09: Exception Handling

# Exception Class Hierarchy

# In most programming languages, exception classes are organized in a hierarchy to allow for structured
#  error handling. Here's a general overview of an Exception Class Hierarchy, using Python as the main
#  example (though the concept applies similarly in Java, C#, etc.):

# 🌳 Python Exception Class Hierarchy

# BaseException
# ├── SystemExit
# ├── KeyboardInterrupt
# ├── GeneratorExit
# └── Exception
#     ├── ArithmeticError
#     │   ├── FloatingPointError
#     │   ├── OverflowError
#     │   └── ZeroDivisionError
#     ├── AssertionError
#     ├── AttributeError
#     ├── BufferError
#     ├── EOFError
#     ├── ImportError
#     │   └── ModuleNotFoundError
#     ├── LookupError
#     │   ├── IndexError
#     │   └── KeyError
#     ├── MemoryError
#     ├── NameError
#     │   └── UnboundLocalError
#     ├── OSError
#     │   ├── BlockingIOError
#     │   ├── ChildProcessError
#     │   ├── ConnectionError
#     │   │   ├── BrokenPipeError
#     │   │   ├── ConnectionAbortedError
#     │   │   ├── ConnectionRefusedError
#     │   │   └── ConnectionResetError
#     │   ├── FileExistsError
#     │   ├── FileNotFoundError
#     │   ├── InterruptedError
#     │   ├── IsADirectoryError
#     │   ├── NotADirectoryError
#     │   ├── PermissionError
#     │   └── TimeoutError
#     ├── ReferenceError
#     ├── RuntimeError
#     │   ├── NotImplementedError
#     │   └── RecursionError
#     ├── StopIteration
#     ├── StopAsyncIteration
#     ├── SyntaxError
#     │   └── IndentationError
#     │       └── TabError
#     ├── SystemError
#     ├── TypeError
#     ├── ValueError
#     │   └── UnicodeError
#     │       ├── UnicodeDecodeError
#     │       ├── UnicodeEncodeError
#     │       └── UnicodeTranslateError
#     └── Warning
#         ├── DeprecationWarning
#         ├── PendingDeprecationWarning
#         ├── RuntimeWarning
#         ├── SyntaxWarning
#         ├── UserWarning
#         ├── FutureWarning
#         ├── ImportWarning
#         ├── UnicodeWarning
#         └── ResourceWarning



# 1. The try Block 🌲
# The try block is used to test a block of code for errors. If an error occurs within the try block,
#  the program will immediately jump to the except block (if provided).

try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")


try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except:
    print("An error occurred!")

    # 2. The except Block 🧩 
    # The except block is used to handle exceptions that are raised in the try block. When Python
    # encounters an error in the try block, it stops execution there and jumps to the appropriate except block.
try:
    result = 5 / 0
except ZeroDivisionError:
    print("Oops! Division by zero.")

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

    # 3. The else Block 🧩 
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Caught an error!")
else:
    print("This won't run.")


try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Division successful. Result: {result}")

    # . The finally Block 🧩 
    # The finally block contains code that always runs, no matter what—whether an exception is raised or not.
    # It's typically used for clean-up actions like closing files, releasing resources, or disconnecting from 
    # a database.
def test():
    try:
        return "from try"
    finally:
        print("Cleaning up in finally")

print(test())



try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")

    # 5. Putting It All Together 🧩 
    # Let’s combine everything into a full example that shows how these blocks work together in harmony:

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")
    else:
        print("✅ Division successful. Result:", result)
    finally:
        print("🔚 Execution of division complete.\n")

# Test cases
divide(10, 2)
divide(5, 0)


def divide_numbers(a, b):
    try:
        result = a / b  # Test this block for errors
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid input type. Numbers required.")
    else:
        print(f"Division successful. Result: {result}")
    finally:
        print("Operation complete.\n")

# Test cases
divide_numbers(10, 2)  # Successful division
divide_numbers(10, 0)  # ZeroDivisionError
divide_numbers(10, "2")  # TypeError


# Play with Exception Handling in order to understand 🧩 
# Absolutely! Let’s play around with some interactive and fun Python examples to really get how exception
# handling works. Feel free to tweak them or run them in your local environment to see what happens. 
# I’ll guide you through the logic too.
class TooYoungError(Exception):
    pass

def check_age(age):
    try:
        if age < 18:
            raise TooYoungError("You're too young to register!")
        print("🎉 Welcome aboard!")
    except TooYoungError as e:
        print("⚠️", e)
    finally:
        print("📝 Age check complete.\n")

# Try different ages
check_age(16)
check_age(21)


def divide_numbers(a, b):
    try:
        result = a / b  # Test this block for errors
        # raise FloatingPointError("Testing FloatingPointError") 3. Uncomment to see execution flow

    # except Exception as e:    # 1. Uncomment to see execution flow
    #     print(f"Exception: An unexpected error occurred: {e}")
    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero!")
    except TypeError:
        print("TypeError: Invalid input type. Numbers required.")
    # except Exception as e:    # 2. Uncomment to see execution flow
    #     print(f"Exception: An unexpected error occurred: {e}")
    else:
        print(f"else: Division successful. Result: {result}")
    finally:
        print("finally: Operation complete.\n")

# Test cases
divide_numbers(10, 2)  # Successful division
divide_numbers(10, 0)  # ZeroDivisionError
divide_numbers(10, "2")  # TypeError


# Key Points Covered: 🔑
# 1-try Block: Used to test a block of code for errors.
# 2-except Block: Used to handle specific or generic errors.
# 3-else Block: Executes when no errors occur in the try block.
# 4-finally Block: Executes regardless of whether an error occurred.
# prompt: generate a learning code on error handling covering all the expects

import random
from typing import Tuple, Dict, List

def generate_random_data(num_samples: int) -> List[Tuple[int, int]]:
    """Generates a list of random number pairs."""
    try:
        if not isinstance(num_samples, int) or num_samples <= 0:
            raise ValueError("Number of samples must be a positive integer.")
        data = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(num_samples)]
        return data
    except ValueError as ve:
        print(f"Error: {ve}")
        return []  # Return empty list on error
    except Exception as e: # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []


def calculate_ratios(data: List[Tuple[int, int]]) -> List[float]:
    """Calculates the ratio of the first number to the second in each pair."""
    ratios = []
    try:
        for pair in data:
            num1, num2 = pair
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            if not isinstance(num1,int) or not isinstance(num2,int):
                raise TypeError("Input data must be integers.")
            ratio = num1 / num2
            ratios.append(ratio)
        return ratios
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
        return []  # Return empty list on error.
    except TypeError as te:
        print(f"Error: {te}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred during ratio calculation: {e}")
        return []


def process_data(num_samples: int) -> List[float]:
    """Combines data generation and ratio calculation with comprehensive error handling."""

    data = generate_random_data(num_samples)
    if not data: # check if generate_random_data returns an empty list which means it had an error
        return []

    ratios = calculate_ratios(data)

    return ratios

# Example usage with error handling
try:
  num_samples = 10
  results = process_data(num_samples)

  if results:
    print("Calculated ratios:", results)
  else: # if process_data returned an empty list it means there was some error
      print("Data processing failed due to an error.")

except Exception as e: # catching unexpected errors
    print(f"An unexpected error occurred: {e}")

# example of invalid input
results = process_data(-5)
if not results:
  print("Negative number of samples, data processing failed.")

results = process_data("abc")
if not results:
    print("Invalid input type, data processing failed.")

# Example
# prompt: generate a learning code on error handling covering all the expects

import random
from typing import Tuple, List

def generate_random_data(num_samples: int) -> List[Tuple[int, int]]:
    """
    Generates a list of tuples with random integers.
    Demonstrates ValueError handling and general Exception catching.
    """
    try:
        if not isinstance(num_samples, int) or num_samples <= 0:
            raise ValueError("❌ 'num_samples' must be a positive integer.")
        
        data = [(random.randint(1, 100), random.randint(0, 100)) for _ in range(num_samples)]
        return data

    except ValueError as ve:
        print(f"[ValueError] {ve}")
        return []

    except Exception as e:
        print(f"[Unexpected Error] {e}")
        return []


def calculate_ratios(data: List[Tuple[int, int]]) -> List[float]:
    """
    Calculates the ratio of the first to the second element in each tuple.
    Demonstrates handling of ZeroDivisionError, TypeError, and general Exception.
    """
    ratios = []

    try:
        for i, (num1, num2) in enumerate(data):
            if not isinstance(num1, int) or not isinstance(num2, int):
                raise TypeError(f"❌ Data at index {i} is not composed of integers.")

            if num2 == 0:
                raise ZeroDivisionError(f"❌ Cannot divide {num1} by zero at index {i}.")

            ratio = num1 / num2
            ratios.append(ratio)

        return ratios

    except ZeroDivisionError as zde:
        print(f"[ZeroDivisionError] {zde}")
        return []

    except TypeError as te:
        print(f"[TypeError] {te}")
        return []

    except Exception as e:
        print(f"[Unexpected Error] {e}")
        return []


def process_data(num_samples: int) -> List[float]:
    """
    Combines data generation and ratio calculation.
    Demonstrates chained function calls with error handling.
    """
    data = generate_random_data(num_samples)

    if not data:
        print("🚫 Data generation failed.")
        return []

    ratios = calculate_ratios(data)

    if not ratios:
        print("🚫 Ratio calculation failed.")
    
    return ratios


# 🧪 Test Run 1: Valid Input
print("🧪 Test 1: Valid input")
try:
    results = process_data(10)
    if results:
        print("✅ Ratios:", results)
except Exception as e:
    print(f"[Top-Level Error] {e}")

print("\n")

# 🧪 Test Run 2: Invalid Input (Negative Number)
print("🧪 Test 2: Negative number of samples")
results = process_data(-5)
if not results:
    print("⛔ Test passed: Handled negative input properly.")

print("\n")

# 🧪 Test Run 3: Invalid Input (Non-integer)
print("🧪 Test 3: Invalid type input (string)")
results = process_data("abc")  # type: ignore
if not results:
    print("⛔ Test passed: Handled string input properly.")


# Practice Problem: 🧩 
# Write a Python program that asks the user for two numbers and divides them. Use exception handling to
#     catch any errors that might occur (e.g., division by zero or invalid input).
def safe_divide():
    try:
        # Step 1: Input from user
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))

        # Step 2: Division logic
        result = num1 / num2

    except ValueError:
        print("🚫 Invalid input! Please enter numeric values only.")
    except ZeroDivisionError:
        print("❌ Cannot divide by zero.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
    else:
        print(f"✅ Result: {num1} / {num2} = {result}")
    finally:
        print("🔚 Division attempt completed.\n")


# Call the function to test
safe_divide()

# Example
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is: {result}")
finally:
    print("Thank you for using the program!")


    # How a Function Throws an Exception in Python?🧩 
def safe_divide():
    while True:
        try:
            # Step 1: Input from user
            num1 = float(input("Enter the numerator: "))
            num2 = float(input("Enter the denominator: "))
            
            # Step 2: Division logic
            result = num1 / num2
        except ValueError:
            print("🚫 Invalid input! Please enter numeric values only.")
        except ZeroDivisionError:
            print("❌ Cannot divide by zero.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")
        else:
            print(f"✅ Result: {num1} / {num2} = {result}")
            break  # Exit the loop once valid input is given
        finally:
            print("🔚 Division attempt completed.\n")


# Call the function to test
safe_divide()


# Example
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed!")  # Raising an exception
    return a / b

# Handling the exception using try-except
try:
    print(divide(10, 2))  # Output: 5.0
    print(divide(5, 0))   # This will raise an exception
except ValueError as e:
    print(f"Error: {e}")  # Catching the ValueError and printing the message


# Handling the Exception with try-except🧩 
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")
    except TypeError:
        print("❌ Both inputs must be numbers!")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Testing the function with different inputs
print(divide(10, 2))  # Output: 5.0
print(divide(5, 0))   # Output: ❌ Cannot divide by zero!
print(divide(10, "abc"))  # Output: ❌ Both inputs must be numbers!

# Example
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b

try:
    result = divide(5, 0)  # This will raise an exception
    print(result)  # This line won't run if exception occurs
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Division by zero is not allowed!

print("Program continues...")  # This line will always execute


# Throwing Custom Exceptions🧩 
# Python also allows you to define custom exceptions by creating a new class that inherits from Exception.
class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return f"{n} is positive"

try:
    print(check_positive(-5))  # Raises NegativeNumberError
except NegativeNumberError as e:
    print(f"Custom Exception Caught: {e}", " - Exception Class Type: ", type(e))  # Output: Custom Exception Caught: Negative numbers are not allowed!

    # Example
    # Step 1: Define the Custom Exception
class NegativeNumberError(Exception):
    def __init__(self, message="Division by a negative number is not allowed!"):
        self.message = message
        super().__init__(self.message)

# Step 2: Function to divide with custom exception handling
def divide(a, b):
    try:
        if b < 0:
            raise NegativeNumberError()  # Raising our custom exception
        if b == 0:
            raise ValueError("Division by zero is not allowed!")  # Built-in exception
        return a / b
    except NegativeNumberError as nne:
        print(f"❌ {nne}")  # Catching the custom exception
    except ValueError as ve:
        print(f"❌ {ve}")  # Catching the built-in exception
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
    else:
        print(f"✅ Result: {a} / {b} = {a / b}")
    finally:
        print("🔚 Division attempt completed.\n")

# Testing the function with custom exception
print(divide(10, -2))  # Output: Custom exception for negative denominator
print(divide(10, 2))   # Valid division
print(divide(10, 0))   # Division by zero


# What is NoReturn?🧩 
# In Python, NoReturn is a special type hint provided by the typing module that indicates a function does not return a value. It is part of the type hinting system, which allows you to specify the expected types of function parameters and return values.
from typing import NoReturn

def raise_error() -> NoReturn:
    raise ValueError("An error occurred!")

try:
    raise_error()
except ValueError as e:
    print(f"Caught an error: {e}")

# Example
from typing import NoReturn

def terminate_program() -> NoReturn:
    """Terminate the program by raising an exception."""
    raise SystemExit("Terminating the program.")

# When you call terminate_program, it never returns normally:
try:
    terminate_program()
except SystemExit as e:
    print(f"Program terminated: {e}")

    # Alternative to NoReturn in Python
def log_error(message: str) -> None:
    """Logs an error message but does not terminate the program."""
    print(f"Error: {message}")

log_error("Something went wrong!")