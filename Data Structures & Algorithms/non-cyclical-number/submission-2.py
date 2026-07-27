class Solution:
    def isHappy(self, n: int) -> bool:
        l=[]
        while n!=1 and n not in l:
            l.append(n)
            t=n
            s=0
            while t>0:
                r=t%10
                s+=r**2
                t=t//10
            n=s
            if s in l:
                return False
        return True