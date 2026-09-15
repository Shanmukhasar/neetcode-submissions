class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for i in range(1 , amount + 1):

            for j in range(n):

                if i >= coins[j]:

                    current = 1 + dp[i - coins[j]]

                    dp[i] = min(dp[i] , current)

        return dp[amount] if dp[amount] != float('inf') else -1


        