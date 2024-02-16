import random
import time

# Generate a list of 23 random numbers between 1 and 1212
numbers = [random.randint(1, 1212) for _ in range(23)]

# Determine the length of the maximum number in the list
max_length = len(str(max(numbers)))

print("Maximum number length:", max_length)
print("Original list:", numbers)

start_time = time.time()

# Initialize a list of lists to hold numbers based on their digits
buckets = [[] for _ in range(10)]

# Distribute numbers into buckets based on their digits
for digit_position in range(max_length):
    for num in numbers:
        digit = num // (10 ** digit_position) % 10
        buckets[digit].append(num)

# Reconstruct the list by concatenating numbers from all buckets
numbers.clear()
for bucket in buckets:
    numbers.extend(bucket)

end_time = time.time()

print("Time taken:", end_time - start_time)
print("Sorted list:", numbers)