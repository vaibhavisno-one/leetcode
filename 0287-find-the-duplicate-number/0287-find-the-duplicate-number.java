class Solution {
    public int findDuplicate(int[] nums) {
        int[] arr = new int[nums.length];
        for(int n: nums)
        {
            if(arr[n]==1)
                return n;
            arr[n]=1;
        }
        return -1;
    }
}