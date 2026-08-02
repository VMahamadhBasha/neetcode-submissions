class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        res=""
        n1=len(w1)
        n2=len(w2)
        k=0
        for i in range(0,min(n1,n2)):
            res += w1[i]
            res +=w2[i]
            k+=1
        if k<n1:
            res+=w1[k:]
        elif k<n2:
            res += w2[k:]
        return res
        