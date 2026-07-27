class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        d=Counter(nums)
        res=list(d.items())
        res.sort(key=lambda x:x[1],reverse=True)
        print(res)
        r=[]
        for i in range(k):
            r.append(res[i][0])
        return r