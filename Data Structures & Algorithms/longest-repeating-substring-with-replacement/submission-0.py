class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        res=0
        for i in range(n):
            for j in  range(i,n):
                sb=s[i:j+1]
                d=Counter(sb)
                m=max(d.values())
                if (len(sb)-m)<=k:
                    res=max(res,len(sb))      
        return res         
