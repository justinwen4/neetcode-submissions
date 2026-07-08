class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            letters = [0] * 26

            for char in word:
                letters[ord(char) - ord('a')] += 1

            if tuple(letters) not in anagrams:
                anagrams[tuple(letters)] = []
            anagrams[tuple(letters)].append(word)
        
        return list(anagrams.values())
                
