class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for w in strs:
            sw = "".join(sorted(w.lower()))
            if sw in seen:
                seen[sw].append(w)
            else:
                seen[sw] = [w]
        return list(seen.values())