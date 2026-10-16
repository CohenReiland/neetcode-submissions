class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        highest = 0
        length = len(arr)
        for i in range(length):
            index = length - i - 1
            current = arr[index]
            arr[index] = highest
            if current > highest:
                highest = current
        arr[-1] = -1
        return arr