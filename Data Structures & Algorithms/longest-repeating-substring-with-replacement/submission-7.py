class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        counts = {}

        l = 0
        maxf = 0

        for r in range(len(s)):
            if s[r] not in counts:
                counts[s[r]] = 0
            counts[s[r]] += 1

            maxf = max(maxf, counts[s[r]])
            
            while (r - l + 1) - maxf > k:
                counts[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

        
        
