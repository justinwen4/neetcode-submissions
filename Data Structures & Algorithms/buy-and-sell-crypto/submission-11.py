class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 99999
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price

            net = price - minPrice
            
            maxProfit = max(net, maxProfit)


        return maxProfit 
            