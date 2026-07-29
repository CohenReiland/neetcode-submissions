class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        zeros = []
        p = 1

        for i in range(l):
            if nums[i] == 0:
                zeros.append(i)
            else: 
                p *= nums[i]
        
        r = [0] * l
        if len(zeros) > 1:
            return r
        elif len(zeros) == 1:
            r[zeros.pop()] = p
            return r

        
        for i in range(l):
            r[i] = p // nums[i]
        return r