# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# https://www.youtube.com/watch?v=nIVW4P8b1VA

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if (left == right):
                return nums[middle]

            if nums[left] <= nums[right]:
                right = middle - 1
            
            if nums[right] < nums[left]:
                left = middle + 1

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            # If the array is sorted, the minimum is at 'left'
            if nums[left] <= nums[right]:
                return nums[left]

            # If middle element is greater than right, minimum must be in the right half
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                # Otherwise, the minimum is in the left half (including middle)
                right = middle

        return nums[left]