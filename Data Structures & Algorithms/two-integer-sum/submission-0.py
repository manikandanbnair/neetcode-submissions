class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        
        for i, value in enumerate(nums):
            if target - value in sol:
                return [sol[target - value], i]
            sol[value] = i

