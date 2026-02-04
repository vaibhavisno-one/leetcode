class Solution {
    public int removeDuplicates(int[] nums) {
        ArrayList<Integer> lists = new ArrayList<>();
        int n = nums.length;
        for (int i =0;i<n;i++) {
            if(!lists.contains(nums[i])){
                lists.add(nums[i]);
            }
        }
        
        for (int i = 0; i < lists.size(); i++) {
            nums[i] = lists.get(i);
        }

        return lists.size();

        

        
    }
}