class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []
        
        for length in range(2,10):
            for start in range(0, len(digits) - length + 1):
                num = int(digits[start:start+length])
                if low <= num <= high:
                    result.append(num)
        
        return result
