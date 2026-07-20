class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        length_longest = 0
        freqs = {}

        for right, char in enumerate(s):
            if char not in freqs:
                freqs[char] = 0
            freqs[char] += 1

            while (right - left + 1) - max(freqs.values()) > k:
                freqs[s[left]] -= 1
                left += 1

            length_longest = max(
                    length_longest,
                    right - left + 1
                )

        return length_longest



