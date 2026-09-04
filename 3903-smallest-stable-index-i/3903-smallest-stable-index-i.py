class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)

        vmax=[0]*n
        vmin=[inf]*n
        vmax[0]=nums[0]

        for i in range(1,n):
            vmax[i]=max(nums[i],vmax[i-1])
        
        vmin[n-1]=nums[n-1]

        for i in range(n-2,-1,-1):
            vmin[i]=min(nums[i],vmin[i+1])

        for i in range(n):
            if vmax[i]-vmin[i]<=k:
                return i

        return -1        
