class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            middle_value = nums[middle]
            if middle_value == target:
                return middle
            elif middle_value > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1