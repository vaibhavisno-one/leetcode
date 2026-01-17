class Solution {
    public boolean isSubsequence(String s, String t) {

        char[] Sa = s.toCharArray();
        char[] Ta = t.toCharArray();
        int i= 0;

            for(int j=i; j<Ta.length & i<Sa.length; j++){
                if (Sa[i]==Ta[j]){
                    i++;
                }

                
            }
            return i==Sa.length;
        
        
    }
}