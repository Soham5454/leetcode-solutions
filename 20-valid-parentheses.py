class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in matches.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != matches[char]:
                    return False
        
        return len(stack) == 0
