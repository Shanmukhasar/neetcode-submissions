class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        minimum_cost = prices[0]

        max_profit = 0

        for i in range(1 , n):

            minimum_cost = min(minimum_cost , prices[i])

            max_profit = max(max_profit , prices[i] - minimum_cost)

        return max_profit




        