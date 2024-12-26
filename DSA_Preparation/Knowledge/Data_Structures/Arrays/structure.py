""" Array Implementation and Operations """

# Initialization
arr = [1, 2, 3, 4, 5]

# Access
print(arr[2])               # Access element at index 2 (3)

# Insertion
arr.append(6)               # Add an element to the end
arr.extend([7, 8])          # Extend the array
arr.insert(2, 99)           # Insert at index 2

# Deletion
arr.remove(99)              # Remove the first occurrence of 99
popped = arr.pop()          # Remove and return the last element
popped_index = arr.pop(1)   # Remove and return element at index 1
arr.clear()                 # Clear all elements: []

# Search
index = arr.index(3)        # Find index of the first occurrence of 3
count = arr.count(1)        # Count occurrences of 1

# Binary Search (Requires Sorted Array)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Traversal 
arr = [10, 20, 30]

for i in range(len(arr)):                   # Index, Reversal: range(len(arr) - 1, -1, -1)
    print(f"Index {i}: Value {arr[i]}")

for num in arr:                             # For-each, Reversal: reversed(arr)
    print(f"Value: {num}")

for index, value in enumerate(arr):         # Enumerate, Reversal: enumerate(reversed(arr))
    print(f"Index {index}: Value {value}")

# Sorting
arr.sort()                  # Sort in place - ascending order
arr.sort(reverse=True)      # Sort in place - descending order
sorted_arr = sorted(arr)    # Return a new sorted list (keep original)

# Reversing
arr.reverse()               # Reverse in place
reversed_arr = arr[::-1]    # Create a reversed copy

# Copying
copy_arr = arr.copy()       # Create a shallow copy

# Slicing
arr = [1, 2, 3, 4, 5]
subarray = arr[1:4]         # Slice from index 1 to 3: [2, 3, 4]
step_array = arr[::2]       # Slice with step of 2: [1, 3, 5]

# List Comprehension
squares = [x ** 2 for x in arr]         # Square each element: [1, 4, 9, 16, 25]
evens = [x for x in arr if x % 2 == 0]  # Filter even numbers: [2, 4]

# Unique Elements
arr = [1, 2, 3, 1, 2, 4]
unique_elements = list(set(arr))        # [1, 2, 3, 4]

# Two Pointers
arr = [1, 2, 3, 4, 5, 6]
i, j = 0, len(arr) - 1
while i < j:
    print(arr[i], arr[j])  # Process elements from both ends
    i += 1
    j -= 1

# Sliding Window (Sum of Subarray of Size K)
k = 3
max_sum, window_sum = 0, sum(arr[:k])
for i in range(len(arr) - k):
    window_sum = window_sum - arr[i] + arr[i + k]
    max_sum = max(max_sum, window_sum)