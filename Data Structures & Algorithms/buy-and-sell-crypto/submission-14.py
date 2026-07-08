class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimum = float("inf")

        for price in prices:
            if price < minimum:
                minimum = price
            
            max_profit = max(max_profit, price - minimum)

        return max_profit
