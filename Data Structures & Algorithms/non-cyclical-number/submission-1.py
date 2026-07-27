class Solution:
    def isHappy(self, n: int) -> bool:
        seen=[]
        while n!=1 and n not in seen :
            seen.append(n)
            temp=n
            s=0
            while temp>0:
                s+= (temp%10)**2
                temp //=10
            n=s
            if n in seen:
                return False
        return True
