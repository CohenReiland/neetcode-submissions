class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for w in strs:
            s += w + "@ "
        return s


    def decode(self, s: str) -> List[str]:
        r = s.split("@ ")
        r.pop(len(r) - 1)
        return r