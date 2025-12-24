class Solution:
    def reverseWords(self, s: str) -> str:
        st = ""
        te = ""
        left=-1
        for i in range(len(s)):
            if s[i] == " ":
                left += 1
                for j in range(left,i):
                    st = s[j] + st 
                    left += 1 
                st += " "
                te += st
                st = "" 
            elif i == len(s)-1:
                left += 1
                for k in range(left,i+1):
                    st = s[k] + st
                te += st
        return te