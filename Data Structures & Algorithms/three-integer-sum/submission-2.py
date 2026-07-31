class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            seen = {}
            p = i + 1
            while p < len(nums) - 1:
                seen[nums[p]] = p
                p += 1
                if ((nums[i] + nums[p]) * -1) in seen and sorted([nums[i], nums[p], ((nums[i] + nums[p]) * -1)]) not in res:
                    res.append(sorted([nums[i], nums[p], ((nums[i] + nums[p]) * -1)]))
        return res
