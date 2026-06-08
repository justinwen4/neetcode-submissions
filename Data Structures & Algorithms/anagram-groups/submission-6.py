class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = {}
        ret = []

        for s in strs:
            anagram = ''.join(sorted(s))
            if anagram not in groupedAnagrams:
                groupedAnagrams[anagram] = []
            groupedAnagrams[anagram].append(s)

        for value in groupedAnagrams.values():
            ret.append(value)
        
        return ret