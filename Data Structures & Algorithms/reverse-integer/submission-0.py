class Solution:
    def reverse(self, n: int) -> int:
        s=1
        if n<0:
            s=-1
            n*=-1
        rev=0
        while n>0:
            r=n%10
            rev =(rev*10)+r
            n=n//10
        if rev<-2**31 or rev>2**31-1:
            return 0
        return rev*s
