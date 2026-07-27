class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        n=len(m)
        for i in range(n):
            for j in range(i+1,n):
                m[i][j],m[j][i]=m[j][i],m[i][j]
        for i in m:
            i.reverse()
            
