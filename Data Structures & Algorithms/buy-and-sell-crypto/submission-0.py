class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        for i1 in range(len(prices)):
            for i2 in range(i1+1, len(prices)):
                if prices[i2] - prices[i1] > maxProf:
                    maxProf = prices[i2] - prices[i1] 

        return maxProf