# Custom Iterator Class



class IntegerIterator:
    def __init__(self, numbers):
        self.numbers = numbers  
        self.index = 0          # Initialize index

    def __iter__(self):
        return self  

    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index]  # Get current value
            self.index += 1                    # Move to next index
            return value
        else:
            raise StopIteration  # No more elements


# List of integers
numbers_list = [10, 20, 30, 40, 50]

# Creating the iterator
iterator = IntegerIterator(numbers_list)

# Using the custom iterator
for num in iterator:
    print(num)
