class Solution:
    def isPalindrome(self, s: str) -> bool:
        si = ""
        for i in s.lower():
            if i.isalpha() or i.isdigit():
                si+=i
        if si == si[::-1]:
            return True
        return False

        