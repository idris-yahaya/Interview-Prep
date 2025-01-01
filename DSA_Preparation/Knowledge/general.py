""" General Functions """

# Maximum
max_val = max([1, 3, 5])  # Output: 5

# Minimum
min_val = min(1, 3, 5)    # Output: 1

# Summation
total = sum([1, 2, 3, 4])  # Output: 10

# Absolute value
abs_val = abs(-10)  # Output: 10


""" Float Infinity """

# Initialize minimum value with positive infinity
min_value = float('inf')
for num in [3, 5, 2, 7]:
    min_value = min(min_value, num)  # 2 after loop

# Initialize maximum value with negative infinity
max_value = float('-inf')
for num in [3, 5, 2, 7]:
    max_value = max(max_value, num)  # 7 after loop


""" Math Module Functions """

import math

# Square root
sqrt_val = math.sqrt(16)  # Output: 4.0

# Greatest Common Divisor (GCD)
gcd_val = math.gcd(20, 8)  # Output: 4


ord()
''.join()