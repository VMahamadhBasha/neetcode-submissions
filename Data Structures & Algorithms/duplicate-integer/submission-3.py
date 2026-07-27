class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(nums)!=len(set(nums))
        s=set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False