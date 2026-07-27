class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        res=[]
        l,r,t,b=0,len(m[0])-1,0,len(m)-1
        while l<=r and t<=b:
            for i in range(l,r+1):
                res.append(m[t][i])
            t+=1
            for j in range(t,b+1):
                res.append(m[j][r])
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    res.append(m[b][i])
            b-=1
            if l<=r:
                for j in range(b,t-1,-1):
                    res.append(m[j][l])
            l+=1
        return res