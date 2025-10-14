# Generator function to yield first 10 even numbers
def generate_even_numbers():
    for i in range(1, 11):  #
        yield i * 2  # Multiply by 2 to get even numbers


# generator
even_numbers = generate_even_numbers()


for number in even_numbers:
    print(number)
