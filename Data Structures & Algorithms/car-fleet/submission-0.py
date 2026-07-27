class Solution:
    def carFleet(self, target: int, p: List[int], s: List[int]) -> int:
        st=[]
        c=sorted(zip(p,s))[::-1]
        for i,j in c:
            t=(target-i)/j
            if not st or t>st[-1]:
                st.append(t)
        return len(st)