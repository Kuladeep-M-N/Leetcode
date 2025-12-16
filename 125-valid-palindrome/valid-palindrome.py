class Solution:
    def isPalindrome(self, s: str) -> bool:
        si = ""
        for i in s.lower():
            if i.isalnum():
                si+=i
        left = 0
        right = len(si) - 1
        while left < right:
            if si[left] != si[right]:
                return False
            left+=1
            right-=1
        return True
            

        