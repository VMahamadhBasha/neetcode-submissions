class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        st=[]
        for i in range(len(nums)-1,k-1,-1):
            st.append(nums.pop())
        for i in range(k):
            nums.insert(0,st.pop(0))
        
        