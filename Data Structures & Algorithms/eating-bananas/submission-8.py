class Solution:
    def calculateHours(self, piles: List[int], rate: int):
        total = 0

        for pile in piles:
            total += (pile + rate - 1) // rate

        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2

            if self.calculateHours(piles, mid) > h:
                l = mid + 1

            else:
                r = mid

        return l