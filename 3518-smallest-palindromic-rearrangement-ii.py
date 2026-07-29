from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        count = Counter(s)
        odd_chars = [ch for ch, c in count.items() if c % 2 == 1]
        middle = odd_chars[0] if odd_chars else ''
        
        half_counts = {ch: c // 2 for ch, c in count.items() if c // 2 > 0}
        half_len = sum(half_counts.values())
        
        CAP = k  # once count exceeds k, we don't care about the exact value
        
        def count_perms_capped(counts, length):
            result = 1
            remaining = length
            for c in counts.values():
                if c == 0:
                    continue
                for i in range(1, c + 1):
                    result = result * (remaining - c + i) // i
                    if result > CAP:
                        return CAP + 1  # sentinel: "more than enough"
                remaining -= c
            return result
        
        total = count_perms_capped(half_counts, half_len)
        if total < k:
            return ""
        
        chars_sorted = sorted(half_counts.keys())
        remaining_counts = dict(half_counts)
        remaining_len = half_len
        half = []
        
        for _ in range(half_len):
            for ch in chars_sorted:
                if remaining_counts.get(ch, 0) == 0:
                    continue
                remaining_counts[ch] -= 1
                remaining_len -= 1
                cnt = count_perms_capped(remaining_counts, remaining_len)
                if k <= cnt:
                    half.append(ch)
                    break
                else:
                    k -= cnt
                    remaining_counts[ch] += 1
                    remaining_len += 1
        
        half_str = ''.join(half)
        return half_str + middle + half_str[::-1]
