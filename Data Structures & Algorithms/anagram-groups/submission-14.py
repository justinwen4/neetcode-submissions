class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}

        for s in strs:
            anagram = [0] * 26

            for c in s:
                anagram[ord(c) - ord('a')] += 1
            
            if tuple(anagram) not in group_anagrams:
                group_anagrams[tuple(anagram)] = []
            group_anagrams[tuple(anagram)].append(s)

        return list(group_anagrams.values())