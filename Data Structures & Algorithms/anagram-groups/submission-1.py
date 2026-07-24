class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) not in ana:
                ana["".join(sorted(strs[i]))] = [strs[i]]
            else:
                ana["".join(sorted(strs[i]))].append(strs[i])
        return list(ana.values())