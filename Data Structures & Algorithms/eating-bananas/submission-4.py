class Solution:
    def calculateBound(self, piles: List[int], rate: int):
        counter = 0
        for pile in piles:
            counter += (pile + rate - 1) // rate

        return counter

        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimum = 1
        maximum = max(piles)

        while minimum < maximum: 
            mid = (maximum + minimum) // 2
            hours = self.calculateBound(piles, mid)

            if hours > h:
                minimum = mid + 1
            else: 
                maximum = mid
            
        return minimum

