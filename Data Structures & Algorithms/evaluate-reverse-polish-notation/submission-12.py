class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                v1 = int(stack.pop())
                v2 = int(stack.pop())

                stack.append(v2 + v1)

            elif token == '/':
                v1 = int(stack.pop())
                v2 = int(stack.pop())

                stack.append(int(v2 / v1))

            elif token == '-':
                v1 = int(stack.pop())
                v2 = int(stack.pop())

                stack.append(v2 - v1)
            elif token == '*':
                v1 = int(stack.pop())
                v2 = int(stack.pop())

                stack.append(v2 * v1)

            else:
                stack.append(int(token))

        return stack[-1]
