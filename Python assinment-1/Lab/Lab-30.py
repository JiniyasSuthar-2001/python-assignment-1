# Write a Python program to demonstrate string slicing.
# main string
text = "PythonProgramming"

# substring from index 0 to 5 (excluding 5)
print("Slice [0:6]:", text[0:6])

#  substring from index 6 to end
print("Slice [6:]:", text[6:])

# every second character
print("Slice [::2]:", text[::2])

# string in reverse
print("Reverse string:", text[::-1])

# last 5 characters
print("Last 5 characters:", text[-5:])