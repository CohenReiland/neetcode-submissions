class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [0] * len(nums)
        for i in range(len(nums)):
            p = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                p *= nums[j]
            prod[i] = p
        return prod