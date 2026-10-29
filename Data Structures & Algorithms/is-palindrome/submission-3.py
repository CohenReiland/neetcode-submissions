class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for l in s:
            if l.isalnum():
                new_string += l.lower()
        return new_string == new_string[::-1]