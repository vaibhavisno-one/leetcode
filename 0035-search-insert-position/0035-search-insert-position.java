class Solution {
    public int searchInsert(int[] nums, int target) {
        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            // If the target is less than or equal to the current element, return the index
            if (nums[i] >= target) {
                return i;
            }
        }
        return nums.length;
    }
}
