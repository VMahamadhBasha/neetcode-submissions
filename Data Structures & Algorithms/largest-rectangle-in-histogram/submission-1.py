class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        a=0
        h.append(0)
        st=[]
        n=len(h)
        for i in range(n):
            while st and h[st[-1]]>=h[i]:
                height=h[st.pop()]
                w=i if not st else i-st[-1]-1
                a=max(a,height*w)
            st.append(i)
        return a