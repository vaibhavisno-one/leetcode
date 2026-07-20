class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        best=ans=worst=nums[0]

        if len(nums)==1:
            return abs(nums[0])

        for num in nums[1:]:
            v1=best+num
            v2=num
            v3=worst+num

            best=max(v1,v2,v3)
            worst=min(v1,v2,v3)
            

            ans=max(best,ans)
            ans=max(ans,abs(worst))
            

            
        return ans
