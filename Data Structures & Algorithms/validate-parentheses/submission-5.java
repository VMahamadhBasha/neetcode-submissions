class Solution {
    public boolean isValid(String s) {
        List<Integer> st=new Stack<>();
        Set<Character> d=new HashSet<>();
        
        for(Character i:s){
                if(i=='('||i=='['||i=='{'){
                    st.add(i);
                }
            else{
                if(st.isEmpty){
                    return false;
                }
                Character c=st.pop();
                if((i=='(' && c!=')')||(i=='[' && c!=']')||(i=='{' && c!='}')){
                    return false;
                }
                }
        }
        return true;
        
    }
}
