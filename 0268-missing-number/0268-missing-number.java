class Solution {
    public int missingNumber(int[] nums) {
        
        int n =nums.length;

        ArrayList <Integer> list = new ArrayList<>();

        for(int num :nums){
            list.add(num);
        }

        for(int i=0;i<=n;i++){
            if(!list.contains(i)){
                return i;
            }
        }

        return -1;
    }
}