class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        st = 0

        for l in range(len(s1)):
            count[s1[l]] = count.get(s1[l], 0) + 1

        for l2 in range(len(s2)):
            if s2[l2] in count :
                count[s2[l2]] -= 1

            while l2 - st + 1 - len(s1) > 0:
                if s2[st] in count:
                    count[s2[st]] += 1
                st += 1

            if max(count.values()) == 0 and min(count.values()) == 0:
                return True
        return False
