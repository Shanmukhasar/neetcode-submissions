class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={num:i for i,num in enumerate(nums)}
        for j,num in enumerate(nums):
            if target-num in d and d[target-num]!=j:
                return [j,d[target-num]]
        