class Solution:
    def calculateHours(self, piles: List[int], rate: int):
        total = 0
        for pile in piles:
            total += (pile + rate - 1) // rate

        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxEating = max(piles)
        minEating = 1

        while minEating < maxEating:
            mid = (minEating + maxEating) // 2
            hours = self.calculateHours(piles, mid)
            
            if hours > h:
                minEating = mid + 1

            else:
                maxEating = mid
        
        return minEating