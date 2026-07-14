class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # visualizing it, I think what we want to do is keep a stack of indices
        # while the values are larger than the top of the stack, we keep going
        # when we get a smaller element, we pop the last element of the stack
        # set a variable minimum equal to the smallest in the stack so far
        # and then calculate the length of the stack and multipoly by the height

        stack = []
        heights.append(0)
        largestRectangle = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                index, length = stack.pop()
                calculated_height = length * (i - index)
                largestRectangle = max(largestRectangle, calculated_height)
                start = index

            stack.append((start, height))

        return largestRectangle
            


            

            