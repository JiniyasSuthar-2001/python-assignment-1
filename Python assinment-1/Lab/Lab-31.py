# main string
text = "  Hello, Python World!  "

print("Original String:", text)

# 1. Remove leading and trailing spaces
print("Strip:", text.strip())

# 2. Convert to uppercase
print("Uppercase:", text.upper())

# 3. Convert to lowercase
print("Lowercase:", text.lower())

# 4. Replace a substring
print("Replace 'Python' with 'Java':", text.replace("Python", "Java"))

# 5. string starts with a substring
print("Starts with '  Hello':", text.startswith("  Hello"))

# 6. tring ends with a substring
print("Ends with 'World!  ':", text.endswith("World!  "))

# 7. Split string into a list of words
print("Split:", text.split())

# 8. Find the index
print("Index of 'Python':", text.find("Python"))

# 9. Count occurrences of a character
print("Count of 'o':", text.count("o"))

# 10. Capitalize the first character of the string
print("Capitalize:", text.capitalize())

# 11. capitalize first letter of each word
print("Title Case:", text.title())