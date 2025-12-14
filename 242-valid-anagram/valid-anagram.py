class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in t:
            if i in s and t.count(i) == s.count(i):
                continue
            else:
                return False
        return True