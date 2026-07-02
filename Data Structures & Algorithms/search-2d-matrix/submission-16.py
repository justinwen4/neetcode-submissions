class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0]) # 3, 4

        left, right = 0, r * c - 1

        while left <= right:
            mid = (left + right) // 2 #5
            row = mid // c 
            col = mid % c

            value = matrix[row][col]

            if value == target:
                return True

            if value < target:
                left = mid + 1

            else:
                right = mid - 1

        return False