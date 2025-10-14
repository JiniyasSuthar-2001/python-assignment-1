# ractical Example 1: Skip 'banana' using continue
# List of fruits
list1 = ['apple', 'banana', 'mango']

# Using for loop with continue
for fruit in list1:
    if fruit == 'banana':
        continue  # Skip banana
    print(fruit)