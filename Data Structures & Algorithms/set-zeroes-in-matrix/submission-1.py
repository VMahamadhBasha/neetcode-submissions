class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        r=set()
        c=set()
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j]==0:
                    r.add(i)
                    c.add(j)
        for i in range(len(m)):
            for j in range(len(m[0])):
                if i in r or j in c:
                    m[i][j]=0
            