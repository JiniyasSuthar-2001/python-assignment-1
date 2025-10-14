# Practical Example 3: Find a specific string in a list

# List of strings
list1 = ['apple', 'banana', 'mango']


search_fruit = input("Enter the fruit to search: ")


found = False  # to check if fruit is found

for fruit in list1:
    if fruit == search_fruit:
        found = True
        break  # Exit the loop once found


if found:
    print(search_fruit, "is present in the list.")
else:
    print(search_fruit, "is not present in the list.")
