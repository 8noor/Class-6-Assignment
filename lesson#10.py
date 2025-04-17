# Lesson 10: I/O File Handling 📁

# File Handling in Python: A Comprehensive Tutorial with Examples

# 2. Reading Files 🗃️
# There are several ways to read the contents of a file:

# Read Entire File

file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

# Read Line by Line 🗃️

file = open('example.txt', 'r')
line = file.readline()  # Read one line at a time
while line:
    print(line, end='')
    line = file.readline()
file.close()


# Read All Lines into a List 🗃️

file = open('example.txt', 'r')
lines = file.readlines()  # Read all lines into a list
for line in lines:
    print(line, end='')
file.close()


# 3. Writing to Files 🗃️
# To write data to a file, you use the write() or writelines() methods.

# Write Data to a File 🗃️

file = open('example.txt', 'w')  # Open for writing
file.write('Hello, world!\nThis is a new line.\n')
file.close()


# Write Multiple Lines 🗃️

lines = ['Hello, world!\n', 'This is the second line.\n', 'And here is the third line.\n']
file = open('example.txt', 'w')
file.writelines(lines)
file.close()
# 4. Appending to Files 🗃️
# Appending data to an existing file can be done by opening the file in append mode 'a'.

file = open('example.txt', 'a')  # Open for appending
file.write('Appending this line.\n')
file.close()
# 5. File Operations 🗃️
# seek(): Moves the file pointer to a specific location.

file = open('example.txt', 'r')
file.seek(5)  # Move the pointer to the 5th byte/character
content = file.read()
print(content)
file.close()

# tell(): Returns the current position of the file pointer.


file = open('example.txt', 'r')
print(file.tell())  # Returns current position of the pointer (byte/character)
file.close()

# flush(): Forces the internal buffer to be written to the file.


file = open('example.txt', 'w')
file.write('Writing this data...')
file.flush()  # Force write the data to disk immediately
file.close()
# 6. Closing Files 🗃️
# It is important to always close the file after performing operations on it. The close() method is used to close the file.


file = open('example.txt', 'r')
content = file.read()
file.close()  # Close the file to free up system resources

# 7. Context Manager (with statement) 🗃️
# The with statement provides a convenient way to handle file opening and closing automatically. The file is automatically closed once the block of code under with is executed.

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# No need to explicitly call file.close(), it's done automatically

# 8. Handling File Exceptions🗃️
# File operations can sometimes raise exceptions, for instance, if the file doesn’t exist or there’s a permission issue. You can use exception handling to deal with such errors.
# Handling FileNotFoundError

try:
    file = open('non_existing_file.txt', 'r')
except FileNotFoundError:
    print("The file was not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Handling IOError (General Input/Output Errors)

try:
    file = open('example.txt', 'r')
    content = file.read()
except IOError:
    print("An I/O error occurred!")
finally:
    if 'file' in locals():
        file.close()

# Example: Complete File Handling Program
# Let’s put everything together with a complete example:


def file_operations():
    # Open and write to a file
    with open('example.txt', 'w') as file:
        file.write("Hello, Python!\n")
        file.writelines(['This is a file handling example.\n', 'File operations are useful.\n'])
    
    # Open and read the file
    try:
        with open('example.txt', 'r') as file:
            content = file.read()
            print("File Content:\n", content)
    except FileNotFoundError:
        print("File not found!")
    
    # Append data to the file
    with open('example.txt', 'a') as file:
        file.write("Appending some more text.\n")
    
    # Read again after appending
    with open('example.txt', 'r') as file:
        content = file.read()
        print("\nFile Content After Appending:\n", content)

file_operations()

# Reading in chunks

with open("new_file.txt", "r") as file:
  print(file.tell())     # 0


  while True:
    content = file.read(10)
    if not content:
      print("End of file")
      break
    print(content)
    i+=1


           # reads 5 characters
  print(file.tell())     # now at position 5
  file.seek(0)           # back to start

#   Conclusion
# Python’s file handling is straightforward with open(), read(), write(), and close(). Always use the with statement for safety and leverage exception handling for robustness. Experiment with modes and methods to manage files effectively!
# prompt: generate a comprehensive example of file handling using all the functions

# Create a file and write to it
with open('example.txt', 'w') as f:
  f.write("This is line 1.\n")
  f.write("This is line 2.\n")
  f.writelines(["This is line 3.\n", "This is line 4.\n"])

# Read the file and print its content
with open('example.txt', 'r') as f:
  content = f.read()
  print("--- Full Content ---")
  print(content)

# Read the file line by line and print each line
with open('example.txt', 'r') as f:
  print("--- Line by Line ---")
  for line in f:
    print(line, end='')

# Read a single line
with open('example.txt', 'r') as f:
  print("\n--- Readline ---")
  print(f.readline(), end='')

# Read all lines into a list
with open('example.txt', 'r') as f:
  lines = f.readlines()
  print("\n--- Readlines ---")
  for line in lines:
    print(line, end='')

# Append to the file
with open('example.txt', 'a') as f:
  f.write("This is appended line 1.\n")
  f.write("This is appended line 2.\n")

# Reading with seek and tell
with open('example.txt', 'r') as f:
  print("\n--- Seek and Tell ---")
  print("Current position:", f.tell())
  print("First line:", f.readline(), end="")
  print("Current position:", f.tell())
  f.seek(0)
  print("After seek(0):", f.tell())
  print("First line again:", f.readline(), end="")

# Demonstrating 'x' mode (exclusive creation)
try:
    with open('new_file.txt', 'x') as f:
        f.write("This is a new file created in 'x' mode.")
        print("new_file.txt created successfully!")
except FileExistsError:
    print("File 'new_file.txt' already exists!")

# Copy file example
def copy_file(source, destination):
  try:
    with open(source, 'r') as src, open(destination, 'w') as dest:
      for line in src:
        dest.write(line)
      print(f"'{source}' successfully copied to '{destination}'")
  except FileNotFoundError:
    print(f"Error: File not found '{source}'")
  except Exception as e:
    print(f"Error during copying: {e}")

copy_file("example.txt", "example_copy.txt")

