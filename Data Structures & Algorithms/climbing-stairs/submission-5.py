class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        arr = [1, 1]

        # 5
        for i in range(n - 1):
            temp = arr[0]
            arr[0] = arr[0] + arr[1]
            arr[1] = temp

        return arr[0]

