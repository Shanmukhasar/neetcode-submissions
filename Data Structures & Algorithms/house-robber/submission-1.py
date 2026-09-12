class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:

            return nums[0]

        a = nums[0]

        b = max(nums[0] , nums[1])

        for i in range(2 , n):

            pick = nums[i] + a

            not_pick = b

            a = b

            b = max(pick , not_pick)

        return b






        