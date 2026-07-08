class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []

        for p in s:
            if p in d.values():
                stack.append(p)
            
            else:
                if not stack:
                    return False
                    
                top = stack.pop()

                if not d[p] == top:
                    return False

        if stack: return False

        return True
