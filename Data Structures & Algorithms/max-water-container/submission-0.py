class Solution:
    def maxArea(self, h: List[int]) -> int:
        res=0
        l,r=0,len(h)-1
        while l<r:
            if h[l]<=h[r]:
                res=max(res,h[l]*(r-l))
                l+=1
            else:
                res=max(res,h[r]*(r-l))
                r-=1
        return res