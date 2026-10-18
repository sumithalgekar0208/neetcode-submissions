class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                if profit > 0 and max_profit < profit:
                    max_profit = profit
        
        return max_profit

        