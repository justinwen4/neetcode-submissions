class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        start = -1

        for i in reversed(range(len(arr))):
            save = arr[i]
            arr[i] = start
            start = max(save, start)
        
        return arr