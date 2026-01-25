class Solution {
    public int rangeBitwiseAnd(int left, int right) {
    //     int and = left;
    //     if(left==0 && right==0) return 0;
    //     if(left==right) return left&right;
    //     for (int i = left+1;i<right;i++){
    //         and &=i;

    //     }
    //     return and;

    int shift = 0;

        while (left < right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }

        return left << shift;
    }
}