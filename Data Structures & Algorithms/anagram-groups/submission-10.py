class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = {}

        for s in strs:
            alpha = [0] * 26

            for letter in s:
                index = ord(letter) - ord('a')
                alpha[index] += 1
            
            key = tuple(alpha)

            if key not in groupedAnagrams:
                groupedAnagrams[key] = []
            groupedAnagrams[key].append(s)
        
        return list(groupedAnagrams.values())