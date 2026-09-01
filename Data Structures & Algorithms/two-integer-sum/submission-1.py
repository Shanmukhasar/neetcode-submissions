class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {num : i for i , num in enumerate(nums)}

        for i , num in enumerate(nums):

            value = target - num

            if value in hash_map and i != hash_map[value]:

                return [i , hash_map[value]]

        return []


        