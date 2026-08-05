class Solution:
    def calPoints(self, o: List[str]) -> int:
        st=[]
        for i in o:
            if i=='D':
                st.append(2*st[-1])
            elif i=="C":
                st.pop()
            elif i=='+':
                st.append(st[-1]+st[-2])
            else:
                st.append(int(i))
        return sum(st)
        