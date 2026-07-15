class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        count = {}
        result = 0
        for index in range(len(s)):
            count[s[index]] = 1 + count.get(s[index], 0)
            while (index - start + 1) - max(count.values()) > k:
                count[s[start]] -= 1
                start += 1
            result = max(result, index - start + 1)
        return result

        