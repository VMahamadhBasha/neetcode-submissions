class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=set()
        j,res=0,0
        for i in range(len(s)):
            while s[i] in l:
                l.remove(s[j])
                j+=1
            l.add(s[i])
            res=max(res,len(l))
        return res
                