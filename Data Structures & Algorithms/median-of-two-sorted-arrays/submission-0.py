class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=nums1+nums2
        res.sort()
        n=len(res)
        if n%2==0:
            mid=n//2
            mid1=mid-1
            return (res[mid]+res[mid1]) /2.0
        else:
            return res[n//2]