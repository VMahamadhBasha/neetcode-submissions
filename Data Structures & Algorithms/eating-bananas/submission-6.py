class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        l,m=1,max(p)
        def can(k):
            s=0
            for i in p:
                s+=(i+k-1)//k
            return s<=h
        while l<m:
            r=(l+m)//2
            if can(r):
                m=r
            else:
                l=r+1
        return l