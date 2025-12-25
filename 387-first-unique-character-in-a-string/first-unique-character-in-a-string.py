class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        index = -1
        for i in s:
            index += 1
            if d[i] == 1:
                return index
        return -1