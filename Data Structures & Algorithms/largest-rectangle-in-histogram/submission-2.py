class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        st=[]
        h.append(0)
        res=0
        for i in range(len(h)):
            while st and h[st[-1]]>=h[i]:
                h1=h[st.pop()]
                w=i if not st else i-st[-1]-1
                res = max(res,h1*w)
            st.append(i)
        return res