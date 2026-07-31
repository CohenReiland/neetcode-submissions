class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            u = i + 1
            while numbers[i] + numbers[u] != target and u < len(numbers) - 1:
                u += 1
                print(u)
            if numbers[i] + numbers[u] == target:
                return [i + 1, u + 1]
        return []