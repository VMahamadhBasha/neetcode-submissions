class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        st=[]
        for i in range(len(a)):
            if not st:
                st.append(a[i])
            else:
                while st and ((st[-1]>0 and a[i]<0) or (st[-1]<0 and a[i])>0):
                    k=st.pop()
                    if abs(k)==abs(a[i]):
                     break
                    if k<0:
                     if abs(k)>a[i]:
                         st.append(k)
                     else:
                         st.append(a[i])
                    elif k>0:
                     if abs(a[i])>k:
                         st.append(a[i])
                     else:
                         st.append(k)
        return st
            
