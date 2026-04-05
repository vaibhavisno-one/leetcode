class Solution {


    private long calculateTotalHours(int[] piles, int speed) {
        long totalH = 0;
        for (int bananas : piles) {
            totalH += (int)Math.ceil((double)bananas / speed);
        }
        return totalH;
    }


    public int minEatingSpeed(int[] piles, int h) {

        int low =1;
        int high = Arrays.stream(piles).max().getAsInt();
        int ans =high;

        while(low<=high){
            int mid = low + (high - low) / 2;
            long totalHrs =calculateTotalHours(piles,mid);
            if(totalHrs<=h){
                ans=mid;
                high=mid-1;
            }
            else{
                low=mid+1;
            }
            
        }

    return ans;
        
    }
}