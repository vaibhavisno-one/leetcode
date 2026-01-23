class Solution {
    public int[] searchRange(int[] nums, int target) {
        int n =nums.length;
        ArrayList <Integer> list= new ArrayList<>();


        for (int num:nums){
            list.add(num);
        }

        if(!list.contains(target)){
            return new int[] {-1,-1};
        }
        int first = list.indexOf(target);
        int last = list.lastIndexOf(target);

        return new int[]{first,last};
    }
}