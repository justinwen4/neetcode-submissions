class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = {}
        max_freq = 0
        ans = 0

        for right, char in enumerate(s):
            if char not in counts:
                counts[char] = 0
            counts[char] += 1

            max_freq = max(max_freq, counts[char])

            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans