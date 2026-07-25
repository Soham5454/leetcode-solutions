class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        distinct = list(set(nums))

        pair_xors = set()
        for x in distinct:
            for y in distinct:
                pair_xors.add(x ^ y)

        triple_xors = set()
        for s in pair_xors:
            for z in distinct:
                triple_xors.add(s ^ z)

        return len(triple_xors)
