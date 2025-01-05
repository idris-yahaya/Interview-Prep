""" 347. Top K Frequent Elements """
# LeetCode: https://leetcode.com/problems/top-k-frequent-elements/description/
# NeetCode: https://neetcode.io/solutions/top-k-frequent-elements

""" Solution: Hash Map & Hash Set """
# Time Complexity: O(n * u)
# Space Complexity: O(n)
# Where n is the length of nums and u is the number of unique elements

# Thought Process:
# Get frequency count of each number and return the k elements attached to the leading counts 

# Solution Code
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(list)

        # Count frequency of each number
        for num in set(nums):
            num_count[nums.count(num)].append(num)

        # Get top k frequent counts
        top_k = sorted(list(num_count.keys()), reverse=True)[0:k]

        # Collect k most frequent elements 
        k_freq = []
        for count in top_k:
            k_freq.extend(num_count[count])

        return k_freq[0:k]