class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)

        max_length , count = 0 , 0

        hash_set = set(nums)

        for i in range(n):

            value = nums[i]

            if (value - 1) not in hash_set:

                while value in hash_set:

                    count = count + 1

                    max_length = max(max_length , count)

                    value = value + 1

                else:

                    count = 0

        return max_length

                


        