# Practical Example 6: Check if a Number is Prime



num = int(input("Enter a number: "))

# Prime number check
if num > 1:
    # if the number is prime
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
else:
    print(num, "is not a prime number")
