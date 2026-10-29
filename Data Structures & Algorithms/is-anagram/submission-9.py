class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) != len(t):
            return False

        for l in range(len(s)):
            seen[s[l]] = 1 + seen.get(s[l], 0)

        for i in range(len(t)):
            seen[t[i]] = seen.get(t[i], 0) - 1


        for value in seen.values():
            if value != 0:
                return False
        return True
