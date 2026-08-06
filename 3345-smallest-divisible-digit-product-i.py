class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num):
            product = 1
            for ch in str(num):
                product *= int(ch)
            return product
        
        num = n
        while digit_product(num) % t != 0:
            num += 1
        return num
