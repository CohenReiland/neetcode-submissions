class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_times = {}

        if len(s) != len(t):
            return False

        for letter in s:
            seen_times[letter] = seen_times.get(letter, 0) + 1
        
        for letter in t:
            if seen_times.get(letter, 0) > 0:
                seen_times[letter] = seen_times[letter] - 1
            else:
                return False
        return True