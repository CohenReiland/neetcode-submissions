class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        largest = 0
        start = 0
        letters = {}
        for i, l in enumerate(s):
            if l in letters and letters[l] >= start:
                start = letters[l] + 1
            letters[l] = i
            largest = max(largest, i - start + 1)
        return largest