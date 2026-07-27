class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        l,m=1,max(p)
        def can(k):
            hr=0
            for i in p:
                hr+=(i+k-1)//k
            return hr<=h
        while l<m:
            mid=(l+m)//2
            if can(mid):
                m=mid
            else:
                l=mid+1
        return l
    