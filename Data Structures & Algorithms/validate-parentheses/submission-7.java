class Solution {
    public boolean isValid(String s) {
        Stack<Character> st=new Stack<>();
        Set<Character> d=new HashSet<>();
        
        for(char i:s.toCharArray()){
                if(i=='('||i=='['||i=='{'){
                    st.add(i);
                }
            else{
                if(st.isEmpty()){
                    return false;
                }
                char c=st.pop();
                if((i==')' && c!='(')||(i=='}' && c!='{')||(i==']' && c!='[')){
                    return false;
                }
                }
        }
        if(st.isEmpty()){
            return true;
        }
        return false;
        
    }
}
