class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in '({[':
                st.append(i)
            else:
                if not st:
                    return False
                k=st.pop()
                if (i==')' and k=='[') or (i==')' and k=='{'):
                    return False
                elif (i=='}' and k=='[') or (i=='}' and k=='('):
                    return False
                elif (i==']' and k=='{') or (i==']' and k=='('):
                    return False
        return True if not st else False