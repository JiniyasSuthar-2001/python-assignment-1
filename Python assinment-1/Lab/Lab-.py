# Practical Example 5: Find Greater and Smaller Number

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is smaller than", num2)
else:
    print("Both numbers are equal")
