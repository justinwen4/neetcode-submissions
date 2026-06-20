class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        counts = {}
        max_freq = 0

        for right, let in enumerate(s):
            if let not in counts:
                counts[let] = 0
            counts[let] += 1

            max_freq = max(counts.values())

            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)


        return ans