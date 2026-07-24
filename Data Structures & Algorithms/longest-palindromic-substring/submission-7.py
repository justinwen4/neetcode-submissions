class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s[0]
            
        longest = 0
        palindrome = ''
        for i in range(len(s)):
            # case 1: odd palindrome
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > longest:
                    longest = max(longest, right - left + 1)
                    palindrome = s[left:right + 1]

                right += 1
                left -= 1

            # case 2: even palindrome
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > longest:
                    longest = max(longest, right - left + 1)
                    palindrome = s[left:right + 1]

                right += 1
                left -= 1

        return palindrome