class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        n=len(nums)
        if (n==1) and (nums[0] ==k):
            return k*(n+1)
        for i in range(1,n):
            if( k*i) not in nums:
                return k*i

        if (k*n) in nums:
            return k*(n+1)

        return k*n