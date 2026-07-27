class Solution:
    def isValidSudoku(self, bd: List[List[str]]) -> bool:
        r=[set() for i in range(9)]
        c=[set() for i in range(9)]
        b=[set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                a=bd[i][j]
                if a=='.':
                    continue
                if a in r[i]:
                    return False
                if a in c[j]:
                    return False
                if a in b[(i//3)*3+(j//3)]:
                    return False
                r[i].add(a)
                c[j].add(a)
                b[(i//3)*3+j//3].add(a)
        return True