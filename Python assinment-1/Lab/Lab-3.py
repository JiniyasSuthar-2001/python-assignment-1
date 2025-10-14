#Write a Python program that demonstrates the correct use of indentation, comments, and
#variables following PEP 8 guidelines.



# Function to calculate area
def calculate_area(length, width):
    """Return the area of a rectangle."""
    area = length * width
    return area


# Main part of the program
length_of_rectangle = 10   # Variable names use lowercase_with_underscores
width_of_rectangle = 5

# Calculate area using the function
area_result = calculate_area(length_of_rectangle, width_of_rectangle)

# Display the result
print("Length:", length_of_rectangle)
print("Width:", width_of_rectangle)
print("Area of Rectangle:", area_result)

