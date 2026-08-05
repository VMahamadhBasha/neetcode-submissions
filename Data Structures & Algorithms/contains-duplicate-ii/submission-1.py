class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
                if(len(d[nums[i]])>1):
                    if abs(d[nums[i]][-1]-d[nums[i]][-2])<=k:
                        return True
            else:
                d[nums[i]]=[i]
        return False
        