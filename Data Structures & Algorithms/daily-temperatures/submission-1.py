class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []


        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                output[prev_i] = i - prev_i

            stack.append(i)

        return output