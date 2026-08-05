class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        res=[]
        for i in range(n):
            res.append([i,abs(arr[i]-x),arr[i]])
        print(res)
        res.sort(key=lambda x:(x[1],x[0]))
        print(res)
        r=[]
        for i in range(k):
            r.append(arr[res[i][0]])
        return sorted(r)
        

        