class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(v1 + v2)

            elif token == '*':
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(v1 * v2)

            elif token == '-':
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(v1 - v2)

            elif token == '/':
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(int(v1 / v2))

            else:
                stack.append(int(token))

        return stack[0]
