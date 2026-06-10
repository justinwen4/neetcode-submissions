class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}

        for s in strs:
            new = [0] * 26

            for c in s:
                val = ord(c) - ord('a')
                new[val] += 1
            
            if tuple(new) not in grouped_anagrams:
                grouped_anagrams[tuple(new)] = []
            grouped_anagrams[tuple(new)].append(s)

        return list(grouped_anagrams.values())
