# 9. Palindrome Number
# Difficulty: Easy
# Approach: String Reversal
# Runtime: 7ms - Beats 63.19%

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
