class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_freq = {}
        for n in nums:
            seen_freq[n] = seen_freq.get(n, 0) + 1
        
        freq_seen = []
        for n, freq in seen_freq.items():
            freq_seen.append([freq, n])
        
        freq_seen.sort()
        
        result = []
        for i in range(k):
            result.append(freq_seen.pop()[1])
        return result
