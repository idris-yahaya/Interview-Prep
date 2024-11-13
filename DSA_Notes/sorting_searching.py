""" Sorting: sorted() and .sort() """
# Time Complexity: O(n log n)
# Space Complexity: O(n)

# sorted() - returns a new sorted list
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers)           # [1, 1, 3, 4, 5]
sorted_numbers_desc = sorted(numbers, reverse=True)  # [5, 4, 3, 1, 1]

# .sort() - sorts in place
numbers = [3, 1, 4, 1, 5]
numbers.sort()                             # Modifies list to [1, 1, 3, 4, 5]
numbers.sort(reverse=True)                 # Modifies list to [5, 4, 3, 1, 1]

""" Binary Search """
# Time Complexity: O(log n)
# Space Complexity: O(1)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if arr[mid] == target:  # If the target is found, return the index
            return mid
        elif arr[mid] < target:  # If target is larger, search the right half
            left = mid + 1
        else:  # If target is smaller, search the left half
            right = mid - 1
    
    return -1  # Return -1 if the target is not found