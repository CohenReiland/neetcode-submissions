class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        r = []
        for num, freq in count.items():
            r.append([freq, num])
        r.sort()

        res = []
        for i in range(k):
            res.append(r.pop()[1])
        return res