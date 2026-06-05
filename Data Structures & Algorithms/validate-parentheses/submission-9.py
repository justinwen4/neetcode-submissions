class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        
        stack = []

        for each in s:
            if each in "[{(":
                stack.append(each)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if d[each] == top:
                    continue
                else:
                    return False

        return len(stack) == 0
                