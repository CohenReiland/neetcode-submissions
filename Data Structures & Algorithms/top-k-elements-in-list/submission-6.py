class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = 1 + seen.get(num, 0)
        
        s = []
        for num, freq in seen.items():
            s.append([freq, num])
        s.sort()

        r = []
        for i in range(k):
            r.append(s.pop()[1])
        return r