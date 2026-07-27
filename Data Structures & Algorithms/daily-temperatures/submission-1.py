class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        st=[]
        n=len(temp)
        res=[0]*n
        for i in range(n):
            while st and temp[st[-1]]<temp[i]:
                a=st.pop()
                res[a]=i-a
            st.append(i)
        return res