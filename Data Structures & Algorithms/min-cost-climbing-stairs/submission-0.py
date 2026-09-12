class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        dp = [0] * (n + 1)

        dp[0] = cost[0]

        dp[1] = cost[1] 

        for i in range(2 , n):

            first = cost[i] + dp[i - 1]

            second = cost[i] + dp[i - 2]

            dp[i] = min(first , second)

        dp[-1] = min(dp[n - 1] , dp[n - 2])

        return dp[-1]




        