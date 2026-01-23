class Solution {
    public int pivotIndex(int[] nums) {
        int n = nums.length;
        int rs,ls=0 ,total= 0;

        for (int num:nums){
            total+=num;
        }
        
        for(int i=0;i<n;i++){
            rs=total-ls-nums[i];
        
        if(ls==rs) return i;


        ls+=nums[i];
        }
        return -1;
    }
}