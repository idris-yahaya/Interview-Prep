""" 242. Valid Anagram """
# LeetCode: https://leetcode.com/problems/valid-anagram/description/
# NeetCode: https://neetcode.io/solutions/valid-anagram

""" Solution: Sorted """
# Time Complexity: O(n log n + m log m)
# Space Complexity: O(1)

# Thought Process:
# Sort each string in alphanumeric order and check if they are the same

# Solution Code
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort and check if both strings are equal
        return sorted(s) == sorted(t)


""" Solution: Hashmap """
# Time Complexity: O(n)
# Space Complexity: O(1)

# Thought Process:
# Retrieve character counts for each string and check if they are the same

# Solution Code
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count, t_count  = {}, {}

        # Retrieve and compare character counts 
        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1
        return s_count == t_count