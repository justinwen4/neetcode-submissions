class Solution:
    def calPoints(self, operations: List[str]) -> int:
        my_list = []
        for op in operations:
            if op == '+':
                my_list.append(my_list[-1] + my_list[-2])
            elif op == 'D':
                my_list.append(my_list[-1] * 2)
            elif op == 'C':
                my_list.pop()
            else:
                my_list.append(int(op))

        return sum(my_list)