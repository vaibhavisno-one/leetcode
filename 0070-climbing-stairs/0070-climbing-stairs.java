class Solution {
    public int climbStairs(int n) {
        if (n<=2) return n;
        int first=1,second=2;
        int sum =0;
        for(int i=3;i<=n;i++){
            sum = first+second;
            first = second;
            second = sum;
        }
        return sum;
    }
}