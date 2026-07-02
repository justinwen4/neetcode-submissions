class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetters = [0] * 26
        tLetters = [0] * 26

        for letter in s:
            sLetters[ord(letter) - ord('a')] += 1
        
        for letter in t:
            tLetters[ord(letter) - ord('a')] += 1

        return sLetters == tLetters