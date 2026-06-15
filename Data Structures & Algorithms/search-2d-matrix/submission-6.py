class Solution:
    def findRow(self, row: [List[int]], target: int):
        left = 0
        right = len(row) - 1

        while left <= right:
            mid = int((left + right) / 2)

            if row[mid] == target:
                return True

            if row[mid] < target:
                left = mid + 1

            if row[mid] > target:
                right = mid - 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] >= target:
                return self.findRow(row, target)
            if row[-1] < target:
                continue

        return False