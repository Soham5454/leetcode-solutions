class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = str(n)
        non_zero = [d for d in digits if d != '0']
        
        if not non_zero:
            x = 0
        else:
            x = int(''.join(non_zero))
        
        total_sum = sum(int(d) for d in str(x))
        
        return x * total_sum
