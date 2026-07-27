class Solution:
    def maxArea(self, h: List[int]) -> int:
        water=0
        l,r=0,len(h)-1
        while l<=r:
            if h[l]<=h[r]:
                water=max(water,h[l]*(r-l))
                l+=1
            else:
                water=max(water,h[r]*(r-l))
                r-=1
        return water