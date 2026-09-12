class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        a = cost[0]

        b = cost[1] 

        for i in range(2 , n):

            first = cost[i] + a

            second = cost[i] + b

            a = b

            b = min(first , second)

        ans = min(a , b)

        return ans




        