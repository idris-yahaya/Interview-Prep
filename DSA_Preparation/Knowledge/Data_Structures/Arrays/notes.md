# DSA: Arrays

## Introduction and Overview
### Purpose and How it Works
- Collections of elements identified by a key index in a contiguous memory format.
- Access elements in O(1) time using an index.

### Advantages
- **Fast Access**: O(1) with an index.
- **Compact Storage**: Memory-efficient for fixed-size datasets.

### Limitations
- **Fixed Size**: Cannot resize after initialization (in static arrays).
- **Expensive Insert/Delete**: O(n) for shifting elements, except at the end (O(1)).

---

## Methods and Concepts
### Key Terms 
- **Indexing**: Position of an element in the array (starts at 0).
- **Contiguous**: Elements stored in a continuous block of memory.
- **Subarray**: A contiguous range of elements in an array.  
  Example: `[3, 6, 1]` is a subarray of `[2, 3, 6, 1, 5, 4]`.
- **Subsequence**: A sequence derived by deleting some elements without rearranging.  
  Example: `[3, 1, 5]` is a subsequence, but `[3, 5, 1]` is not.

### Operations
| Operation           | Time Complexity | Notes                                  |
|---------------------|-----------------|----------------------------------------|
| **Access**          | O(1)            | Direct access via index.               |
| **Insert/Delete**   | O(n)            | Requires shifting elements.            |
| **Search**          | O(n) / O(log n) | Linear for unsorted, binary for sorted.|

**Space Complexity**: O(n) where n is the number of elements.

### Techniques
- **Two Pointers**: Useful for comparisons or merging arrays.
- **Sliding Window**: Optimizes subarray problems by maintaining a dynamic window.
- **Pre-sorting**: Simplifies problems like finding pairs or intersections.
- **Right Traversal**: Solves problems requiring suffix-based logic.

---

## Tips and Resources
### Edge Cases
- **Empty Structure**
- **Single Element**
- **Out-of-Bounds**
- **Duplicates**

### Strategies
- **Clarify Constraints**: Sorted? Fixed-size? Unique elements?
- **Optimize**: Use binary search, prefix sums, or in-place modifications.

### Questions
- **Learning**: Two Sum, Best Time to Buy and Sell Stock, Product of Array Except Self, Maximum Subarray
- **Practice**: Contains Duplicate, Maximum Product Subarray, Search in Rotated Sorted Array, 3Sum, Container With Most Water, Sliding Window Maximum

### Additional Notes
- [W3Schools Arrays](https://www.w3schools.com/dsa/dsa_data_arrays.php)
- [Tech Handbook Arrays](https://www.techinterviewhandbook.org/algorithms/array/)

---