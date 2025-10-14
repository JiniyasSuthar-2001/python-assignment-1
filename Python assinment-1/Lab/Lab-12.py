# Practical Example 8: Check Blood Donation Eligibility



age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

# Nested if to check eligibility
if age >= 18:
    if age <= 80:
        if weight >= 60 :
            print("You are eligible to donate blood.")
        else:
            print("You are not eligible to donate blood due to low weight.")
    else:
        print("You are not eligible to donate blood due to age limit.")
else:
    print("You are not eligible to donate blood due to age limit.")
