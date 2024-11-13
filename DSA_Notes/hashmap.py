""" Dictionaries """
# Time Complexity
# Insertion O(1), Lookup O(1), Deletion O(1)

# Creating and updating a dictionary
my_dict = {}
my_dict = {"apple": 1, "banana": 2}
my_dict["orange"] = 3         # Add new key-value pair
my_dict["apple"] = 5          # Update existing key-value

# Accessing values
value = my_dict.get("apple")   # Returns 5
orange_count = my_dict.get("orange", 0)  # Returns 3 if exists, else 0

# Deleting a key
del my_dict["banana"]


""" Sets """
# Time Complexity
# Insertion O(1), Lookup O(1), Deletion O(1)

# Creating and updating a set
my_set = set()
my_set = {1, 2, 3}
my_set.add(4)                  # Adds 4

# Removing elements
my_set.remove(2)               # Raises KeyError if 2 is missing
my_set.discard(5)              # Removes 5 if exists, else no error

# Set operations
another_set = {3, 4, 5}
union_set = my_set | another_set           # Union: combines elements from both sets {1, 3, 4, 5}
intersection_set = my_set & another_set    # Intersection: elements common to both sets {3, 4}
difference_set = my_set - another_set      # # Difference: elements in my_set but not in another_set {1}