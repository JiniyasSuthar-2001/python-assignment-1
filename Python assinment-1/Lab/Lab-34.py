#Write a Python program that filters out even numbers using the filter() function


numbers = [1, 2, 3, 4, 5, 6]

# Using filter() to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original numbers:", numbers)
print("Even numbers:", even_numbers)