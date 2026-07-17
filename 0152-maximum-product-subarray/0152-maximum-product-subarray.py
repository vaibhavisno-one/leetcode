class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        worst=best=ans=nums[0]

        for num in nums[1:]:
            v1=best*num

            v2=num
            v3=worst*num

            best=max(v1,v2,v3)
            worst=min(v1,v2,v3)
            ans=max(best,ans)
        return ans