class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        k = 0
        cur = haystack[:n]
        if cur == needle:
            return 0
        for i in range(n,len(haystack)):
            cur += haystack[i]
            cur = cur[1:]
            k+=1
            if cur == needle:
                return k
        return -1

