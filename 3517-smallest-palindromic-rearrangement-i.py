from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        
        left_half = []
        middle = ''
        for ch in sorted(count.keys()):
            c = count[ch]
            left_half.append(ch * (c // 2))
            if c % 2 == 1:
                middle = ch
        
        left = ''.join(left_half)
        return left + middle + left[::-1]
