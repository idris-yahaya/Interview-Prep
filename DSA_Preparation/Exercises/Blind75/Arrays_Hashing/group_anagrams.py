""" 49. Group Anagrams """
# LeetCode: https://leetcode.com/problems/group-anagrams/description/
# NeetCode: https://neetcode.io/solutions/group-anagrams

""" Solution: Sorted Hash Map """
# Time Complexity: O(n * m log m)
# Space Complexity: O(n * m)
# Where n is number of strings, and m is the length of the longest string

# Thought Process
# Hash map with sorted strings as keys and grouped anagrams as values

# Solution Code
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        # Add sorted strings to matching set
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_group[sorted_word].append(word)

        return list(anagram_group.values())


""" Solution: Char Count Hash Map """
# Time Complexity: O(n * m)
# Space Complexity: O(n)
# Where n is number of strings, and m is the length of the longest string

# Thought Process
# Hash map with character count as a tuple key and grouped anagrams as values

# Solution Code
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        # Track and determine character count for each string
        for word in strs:
            char_count = [0] * 26

            for char in word:
                char_count[ord(char) - ord('a')] += 1

            # Add char count as tuple key, and anagram string as value
            anagram_group[tuple(char_count)].append(word)
        
        return list(anagram_group.values())


""" Solution: Hash Map (Working logic, Errors Test Cases) """
# Time Complexity: O(n * m)
# Space Complexity: O(n)
# Where n is number of strings, and m is the length of the longest string

# Thought Process
# Sort strings by character count and use them as a tuple key to group anagrams as values

# Solution Code
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Sort anagram and return tuple of (char, count) pairs
        def sortAnagram(s: str) -> tuple:
            s_count = {}

            for char in s:
                s_count[char] = s_count.get(char, 0) + 1
            return tuple(set(s_count.items()))
            
        anagram_group = defaultdict(list)
        
        # Add sorted strings to matching set
        for word in strs:
            key = sortAnagram(word)
            anagram_group[key].append(word)

        return list(anagram_group.values())