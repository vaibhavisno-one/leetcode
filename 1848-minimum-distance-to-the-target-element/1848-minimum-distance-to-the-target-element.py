class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:

        one=0
        ans=inf
        for i in range(len(nums)):
            if nums[i]==target:
               ans=min(ans,abs(i-start))

        
        return ans