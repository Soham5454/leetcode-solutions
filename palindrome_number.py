# 9. Palindrome Number
# Difficulty: Easy
# Approach: String Reversal
# Runtime: 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
