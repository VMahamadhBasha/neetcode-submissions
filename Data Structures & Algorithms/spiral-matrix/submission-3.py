class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        l,r,t,b=0,len(m[0])-1,0,len(m)-1
        res=[]
        while l<=r and t<=b:
            for i in range(l,r+1):
                res.append(m[t][i])
            t+=1
            for i in range(t,b+1):
                res.append(m[i][r])
            print(res)
            r-=1
            if t<=b:    
                for i in range(r,l-1,-1):
                    res.append(m[b][i])
            b-=1
            print(res)
            if l<=r:
                for i in range(b,t-1,-1):
                    res.append(m[i][l])
            l+=1
            print(res)
        return res

            