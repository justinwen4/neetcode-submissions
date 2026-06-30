class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if n > m:
            return False

        need = [0] * 26
        have = [0] * 26

        for c in s1:
            need[ord(c) - ord('a')] += 1

        for i in range(n):
            have[ord(s2[i]) - ord('a')] += 1

        if need == have:
            return True

        for r in range(n, m):
            have[ord(s2[r]) - ord('a')] += 1
            have[ord(s2[r - n]) - ord('a')] -= 1

            if need == have:
                return True

        return False