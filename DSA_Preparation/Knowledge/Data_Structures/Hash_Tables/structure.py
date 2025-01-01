""" Hash Table (Set | Map) Implementation and Operations """

# Custom Hash Set
class SimpleHashSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, value):
        return sum(ord(char) for char in value) % self.size

    def add(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    def contains(self, value):
        index = self.hash_function(value)
        return value in self.buckets[index]

    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def print_set(self):
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")

hash_set = SimpleHashSet()
hash_set.add("Alice")
hash_set.add("Bob")
hash_set.print_set()

### Built-in Set ###

# Initialization
hash_set = set()                # Empty set
hash_set = {1, 2, 3}            # Set with initial values

# Access
value = 'apple'
exists = value in hash_set      # Check if value exists

# Insertion
hash_set.add('apple')           # Add value to the set

# Deletion
if 'apple' in hash_set:
    hash_set.remove('apple')    # Remove value; raises KeyError if value not found
hash_set.discard(5)             # Removes 5 if exists, no error if 5 is not in the set

# Search
exists = 'apple' in hash_set    # Returns True if value exists

# Traversal
for value in hash_set:
    print(f"Value: {value}")    # Print each element

# Enumerate during Traversal
for index, value in enumerate(hash_set):
    print(f"Index: {index}, Value: {value}")    # Print index and value during traversal

# Other Methods and Techniques
size = len(hash_set)                            # Get the number of elements in the set
hash_set.clear()                                # Remove all elements from the set
hash_set.update(['banana', 'cherry'])           # Bulk insert elements from an iterable

# Set operations
another_set = {3, 4, 5}
union_set = hash_set | another_set              # Union: combines elements from both sets {1, 2, 3, 4, 5}
intersection_set = hash_set & another_set       # Intersection: elements common to both sets {3}
difference_set = hash_set - another_set         # Difference: elements in hash_set but not in another_set {1, 2}


# Custom Hash Map
class SimpleHashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  # Remove the key-value pair
                return

    def print_map(self):
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")

hash_map = SimpleHashMap()
hash_map.put("123", "Alice")
hash_map.put("456", "Bob")
hash_map.print_map()

### Built-in Dictionary ###

# Initialization
hash_map = {}

# Access
key = 'apple'
value = hash_map[key]
value = hash_map.get(key, 'Not Found')  # Returns 'Not Found' if key does not exist

# Insertion
hash_map['apple'] = 5                   # Add key-value pair

# Deletion
if 'apple' in hash_map:
    del hash_map['apple']               # Remove key-value pair

# Search
exists = 'apple' in hash_map            # Returns True if key exists

# Traversal
for key, value in hash_map.items():
    print(f"Key: {key}, Value: {value}")

# Enumerate during Traversal
for index, (key, value) in enumerate(hash_map.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")

# Other Methods and Techniques
size = len(hash_map)                                # Get number of key-value pairs
hash_map.clear()                                    # Remove all entries
hash_map.update({'banana': 2, 'cherry': 3})         # Bulk insert/update

# Retrieval and Update
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruit_count = {}
for fruit in fruits:
    fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
print(fruit_count) 