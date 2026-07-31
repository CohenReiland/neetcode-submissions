class Solution:
    def isPalindrome(self, s: str) -> bool:
        sc = "".join(char for char in s if char.isalnum())
        sc = sc.lower()
        h = math.floor(len(sc) / 2)
        for i in range(h):
            if sc[i] != sc[len(sc) - 1 - i]:
                return False
        return True