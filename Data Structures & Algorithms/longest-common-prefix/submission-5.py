class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        temp=strs[0]
        i=0
        while i<len(temp):
            for j in range(len(strs)):
                if i >= len(strs[j])  or temp[i] != strs[j][i]:
                    return res
            res+=temp[i]
            i+=1
        return res