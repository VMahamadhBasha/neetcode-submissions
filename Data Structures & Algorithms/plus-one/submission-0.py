class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        res=0
        for i in d:
            res=res*10+int(i)
        res+=1
        print(res)
        res=str(res)
        r=[]
        for i in range(len(res)):
            r.append(int(res[i]))
        return r