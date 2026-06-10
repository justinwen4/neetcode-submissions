class Solution:
    def isValid(self, s: str) -> bool:
        d = {
        ')':'(',
        '}':'{',
        ']':'['
        }

        stack = []

        for p in s:
            if p in '([{':
                stack.append(p)
            else:
                if stack:
                    top = stack.pop()
                else:
                    return False

                if d[p] != top:
                    return False
                
        return len(stack) == 0

