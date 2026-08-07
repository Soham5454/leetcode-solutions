class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        factors = {2: 0, 3: 0, 5: 0, 7: 0}
        tt = t
        for p in (2, 3, 5, 7):
            while tt % p == 0:
                factors[p] += 1
                tt //= p
        if tt != 1:
            return "-1"

        need0 = (factors[2], factors[3], factors[5], factors[7])

        digit_factors = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        def sub(need, df):
            return (
                need[0] - df[0] if need[0] > df[0] else 0,
                need[1] - df[1] if need[1] > df[1] else 0,
                need[2] - df[2] if need[2] > df[2] else 0,
                need[3] - df[3] if need[3] > df[3] else 0
            )

        def min_digits_needed(need):
            a, b, c, d = need
            base = c + d
            best = float('inf')

            limit = a if a < b else b
            for x in range(limit + 1):
                rem_a = a - x if a > x else 0
                rem_b = b - x if b > x else 0
                cost = x + (rem_a + 2) // 3 + (rem_b + 1) // 2
                if cost < best:
                    best = cost
            return base + best

        def construct(length, need):
            result = []
            for pos in range(length):
                remaining = length - pos - 1
                for d in range(1, 10):
                    nd = sub(need, digit_factors[d])
                    if min_digits_needed(nd) <= remaining:
                        result.append(str(d))
                        need = nd
                        break
            return ''.join(result)

        n = len(num)
        digits = [int(c) for c in num]

        first_zero = n
        for i in range(n):
            if digits[i] == 0:
                first_zero = i
                break

        prefix_needs = [need0]
        for i in range(first_zero):
            prefix_needs.append(sub(prefix_needs[-1], digit_factors[digits[i]]))

        if first_zero == n and prefix_needs[-1] == (0, 0, 0, 0):
            return num

        start_i = min(n - 1, first_zero)

        for i in range(start_i, -1, -1):
            nd_prefix = prefix_needs[i]
            for d in range(digits[i] + 1, 10):
                nd2 = sub(nd_prefix, digit_factors[d])
                remaining = n - i - 1

                if min_digits_needed(nd2) <= remaining:
                    suffix = construct(remaining, nd2)
                    return num[:i] + str(d) + suffix

        length = max(n + 1, min_digits_needed(need0))
        return construct(length, need0)
