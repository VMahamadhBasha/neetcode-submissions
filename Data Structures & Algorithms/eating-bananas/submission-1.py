class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        m=max(p)
        i,j=1,m
        def cs(k):
            hr=0
            for i in p:
                hr+=(i+k-1)//k
            return hr<=h
        while i<j:
            mid=(i+j)//2
            if cs(mid):
                j=mid
            else:
                i=mid+1
        return i