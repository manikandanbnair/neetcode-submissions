class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for x in nums:
            if x in result:
                return True
            result[x] = ""
        return False
