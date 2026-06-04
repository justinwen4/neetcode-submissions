class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCounter = 0
        currentCounter = 0

        for num in nums:
            if num != 1:
                if maxCounter < currentCounter:
                    maxCounter = currentCounter
                currentCounter = 0
            else:
                currentCounter += 1
        
        if maxCounter < currentCounter:
            maxCounter = currentCounter
        
        return maxCounter