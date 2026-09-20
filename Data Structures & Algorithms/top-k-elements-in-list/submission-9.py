class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = {}
        for num in nums:
            f_map[num] = f_map.get(num,0) + 1

        a = dict(sorted(f_map.items(), key = lambda x: x[1], reverse = True))
        a = list(a.keys())
        return a[:k]