class Solution:
    def trap(self, h: List[int]) -> int:
        lmax,rmax=0,0
        l,r=0,len(h)-1
        water=0
        while l<=r:
            if h[l]<=h[r]:
                if h[l]>=lmax:
                    lmax=h[l]
                else:
                    water+=lmax-h[l]
                l+=1
            else:
                if h[r]>=rmax:
                    rmax=h[r]
                else:
                    water+=rmax-h[r]
                r-=1
        return water