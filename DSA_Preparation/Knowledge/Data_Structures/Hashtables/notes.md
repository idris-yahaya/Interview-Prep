# DSA: Hash Tables (Sets | Maps)

## Introduction and Overview
### Purpose and How it Works
- A **Hash Table** is a data structure that provides efficient storage, retrieval, and deletion of data using key-value pairs.
- **Key Idea**: Uses a **hash function** to map keys to specific buckets in an array, enabling quick access to values

### Advantages
- **Fast Operations**: Average time complexity of \(O(1)\) for insert, search, and delete.
- **Efficient Use of Keys**: Great for scenarios involving unique key lookups or associations.

### Limitations
- **Space Overhead**: Requires extra memory for buckets to maintain efficiency.
- **Collision Handling**: Requires strategies like chaining or open addressing, which may affect performance.

---

## Methods and Concepts
### Key Terms 
- **Hash Set**: Every element is a unique key.
- **Hash Map**: Every entry is a key-value-pair, with a key that is unique, and a value connected it.
- **Bucket**: Storage container for one or more elements.
- **Hash Code**: Result of a hash function that determines the bucket.
- **Hash Function**: Maps a key to an integer, determining its hash code. Ex: `sum(ord(c) for c in key) % num_buckets`.
- **Collision**: Occurs when two keys map to the same bucket.
- **Load Factor**: Ratio of stored elements divided by the total buckets

### Operations
| Operation           | Time Complexity | Notes                                  |
|---------------------|-----------------|----------------------------------------|
| **Insert**          | O(1)            | Add key-value pairs or elements.       |
| **Delete**          | O(1)            | Remove key-value pairs or elements.    |
| **Search**          | O(1)            | Locate an element or value by its key. |
| **Update**          | O(1)            | Modify the value of a given key.       |

**Space Complexity**: O(n), where n is the number of elements.

### Techniques
- **Chaining**: Resolves collisions by storing multiple elements in a bucket using linked lists or arrays.
- **Open Addressing**: Resolves collisions by finding the next available bucket (e.g., linear probing, quadratic probing).
- **Dynamic Resizing**: Resizes and redistributes buckets when the load factor exceeds a threshold (commonly 0.75).

---

## Tips and Resources
### Edge Cases
- **Empty Structure**
- **Single Element**
- **Invalid Inputs**
- **Duplicates**

### Strategies
- Use hash tables when frequent insertions and lookups are needed.

### Questions
- **Learning**: Two Sum, Ransom Note
- **Practice**: Group Anagrams, Insert Delete GetRandom O(1), First Missing Positive, LRU Cache, All O one Data Structure

### Additional Notes
- [Tech Handbook](https://www.techinterviewhandbook.org/algorithms/hash-table/)
- [W3Schools](https://www.w3schools.com/dsa/dsa_theory_hashtables.php)
- [VisuAlgo](https://visualgo.net/en/hashtable).

---