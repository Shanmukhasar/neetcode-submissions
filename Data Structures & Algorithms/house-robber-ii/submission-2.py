class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:

            return nums[0]

        if n == 2:

            return max(nums[0] , nums[1])

        def max_profit(nums):

            n = len(nums)

            a = nums[0]

            b = max(nums[0] , nums[1])

            for i in range(2 , n):

                pick = nums[i] + a

                not_pick = b

                a = b

                b = max(pick , not_pick)

            return b

        first = max_profit(nums[ : n - 1])

        second = max_profit(nums[1 :]) 

        return max(first , second)


        