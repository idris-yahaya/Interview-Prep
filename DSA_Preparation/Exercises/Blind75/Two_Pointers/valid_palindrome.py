""" 125. Valid Palindrome """
# LeetCode: https://leetcode.com/problems/valid-palindrome/description/
# NeetCode: https://neetcode.io/solutions/valid-palindrome

""" Solution: [Approach] """
# Time Complexity: O(?)
# Space Complexity: O(?)
# Where [? is ?]

# Thought Process:
# [Insert explanation of approach and reasoning]

# Solution Code

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_c, right_c = 0, len(s) - 1
        alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = "".join(s.split())
        s = s.lower()

        while left_c < right_c:
            # Move left_c if it's not pointing to an alphanumeric character
            if s[left_c] not in alphanumeric:
                left_c += 1
                continue
            
            # Move right_c if it's not pointing to an alphanumeric character
            if s[right_c] not in alphanumeric:
                right_c -= 1
                continue
            
            # Compare characters after ensuring both are alphanumeric
            if s[left_c] != s[right_c]:
                return False
            
            # Move pointers inward
            left_c += 1
            right_c -= 1
        
        return True
