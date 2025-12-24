class Solution:
    def reverseWords(self, s: str) -> str:
        st = ""
        te = ""
        left=-1
        right=0
        for i in range(len(s)):
            right+=1
            if s[i] == " ":
                left += 1
                for j in range(left,right-1):
                    st = s[j] + st 
                    left += 1 
                st += " "
                te += st
                st = ""
                
            elif right == len(s):
                left += 1
                for k in range(left,right):
                    st = s[k] + st
                te += st
        return te