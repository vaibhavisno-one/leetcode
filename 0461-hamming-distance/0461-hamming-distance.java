class Solution {
    public int hammingDistance(int x, int y) {
        int h = x^y;
        int count =0;
        for (int i = 0;i<32;i++){
            if((h&(1<<i))!=0) count ++;
        }   
        return count;
        
    }
}