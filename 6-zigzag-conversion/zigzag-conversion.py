class Solution:
    def convert(self, s: str, numRows: int) -> str:
        cr = -1
        i = 0
        end = False
        lis =[]
        if numRows == 1 or len(s) < 3:
            return s 
        for j in range(numRows):
            lis.append([])
        while i < len(s):
            if cr <= numRows-1 and not end:
                if cr == numRows-1:
                    end = True
                    continue
                cr += 1
            elif cr >=0 and end:
                if cr == 0:
                    end = False
                    continue
                cr -= 1
            lis[cr].append(s[i])
            i += 1
        st = ""
        for k in range(numRows):
            for a in lis[k]:
                st += a
        return st