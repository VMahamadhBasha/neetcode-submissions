class Solution:
    def rotate(self, m:List[List[int]]) -> None:
        n,m1=len(m),len(m[0])
        """
        res=[[0 for i in range(m1)]for j in range(n)] 
        print(res)

        for i in range(n):
            for j in range(n):
                res[i][j]=m[j][i]
        for i in res:
            i.reverse()
        return 
        """
        for i in range(m1):
            for j in range(i+1,n):
                m[i][j],m[j][i]=m[j][i],m[i][j]
        for i in m:
            i.reverse()
        
