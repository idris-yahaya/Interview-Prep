""" 217. Contains Duplicate """
# LeetCode: https://leetcode.com/problems/contains-duplicate/description/
# NeetCode: https://neetcode.io/solutions/contains-duplicate

""" Solution: Hash Set (Seen) """
# Time Complexity: O(n)
# Space Complexity: O(n)

# Thought Process:
# Use a set to keep track of seen elements. Return false if an element is already added

# Code Solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        # Store and check for duplicates 
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


""" Solution: Hash Set (Length) """
# Time Complexity: O(n)
# Space Complexity: O(n)

# Thought Process:
# Turn nums array into a set (eliminates duplicates) and check the size of both

# Code Solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Verify length of set/regular version of nums
        return len(set(nums)) != len(nums)


""" Solution: Sorting """
# Time Complexity: O(n log n)
# Space Complexity: O(1)

# Thought Process:
# Sort nums array and check if adjacent elements are duplicates

# Code Solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        # Check adjacent elements for duplicates
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False