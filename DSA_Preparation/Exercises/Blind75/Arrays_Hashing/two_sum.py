""" 1. Two Sum """
# LeetCode: https://leetcode.com/problems/two-sum/description/
# NeetCode: https://neetcode.io/solutions/two-sum

""" Solution: Hash Map """
# Time Complexity: O(n)
# Space Complexity: O(n)

# Thought Process
# Iterate through nums and find/track num complement (target - num)

# Solution Code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}

        # Find and add num complement
        for i, num, in enumerate(nums):
            if target - num in num_index:
                return [i, num_index[target - num]]
            num_index[num] = i

        return [-1, -1]


""" Solution: List Slice """
# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Thought Process
# Iterate through nums and check if num complement within previous array slice

# Solution Code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num, in enumerate(nums):
            complement = target - num

            # Check prev array slice for num complement
            if complement in nums[0:i]:
                return [i, nums[0:i].index(complement)]

        return [-1, -1]