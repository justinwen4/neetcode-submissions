class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0]) # find the length of the matrix
        left, right = 0, m * n - 1 # treat as global array

        while left <= right:
            mid = (left + right) // 2

            row = mid // n
            col = mid % n
            value = matrix[row][col]

            if value == target:
                return True

            if value < target:
                left = mid + 1

            if value > target:
                right = mid - 1

        return False
            