class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def numHours(piles, rate):

            if rate == 0:
                return float("inf")
            total = 0

            for pile in piles:
                total += (pile + rate - 1) // rate

            return total

        left = 0
        right = max(piles)

        eatingRate = 0

        while left <= right:
            mid = (left + right) // 2

            val = numHours(piles, mid)

            if val > h:
                left = mid + 1

            else:
                eatingRate = mid
                right = mid - 1

        return eatingRate

