class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for string in strs:
            anagram = ''.join(sorted(string))
            if anagram not in d:
                d[anagram] = []
            d[anagram].append(string)
        
        return list(d.values())

        