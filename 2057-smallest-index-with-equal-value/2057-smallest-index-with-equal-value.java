class Solution {
    public int smallestEqual(int[] nums) {
        for (int i = 0; i<=nums.length-1; i++){
            if ((i % 10)==nums[i]){
                return i;
                
            }
            
        }
        return -1;
    }
}