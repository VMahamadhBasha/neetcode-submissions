class Solution:
    def maxProfit(self, p: List[int]) -> int:
        dp=[0]*(len(p)+1)
        pr=0
        m=p[0]
        for i in p:
            if i<=m:
                m=i
            else :
                pr=max(pr,i-m)
        return pr
        
        