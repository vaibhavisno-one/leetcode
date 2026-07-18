class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=best=nums[0]

        for num in nums[1:]:
            v1=best+num
            v2=num
            best=max(v1,v2)
            ans=max(best,ans)
        
        return ans