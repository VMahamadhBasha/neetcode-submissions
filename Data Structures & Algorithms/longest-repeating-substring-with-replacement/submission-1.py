class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        res=0
        for i in range(n):
            for j in range(i,n):
                sb=s[i:j+1]
                c=len(sb)
                d=Counter(sb)
                if c-max(d.values())<=k:
                    res=max(res,c)
        return res