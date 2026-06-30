class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        res = 0
        
        maxf = 0
        left = 0

        for right in range(len(s)):
            if s[right] not in counts:
                counts[s[right]] = 0
            counts[s[right]] += 1

            maxf = max(maxf, counts[s[right]])

            while (right - left + 1) - maxf > k:
                counts[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res

