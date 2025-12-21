class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st = ""
        for i in strs:
            elt = i
            if elt == "":
                return elt
        if len(strs) == 0:
            return st
        elif len(strs)==1:
            return strs[0]
        elif len(strs)!=0:
            mi = min(len(s) for s in strs)
            for i in range(mi):
                res = strs[0][i]
                for j in range(1,len(strs)):
                    if res != strs[j][i]:
                        return st
                st += res
            return st
        else:
            return ""




