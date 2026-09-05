class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        vmax=[0]*n
        vmin=[0]*n
        vmax[0]=nums[0]
        vmin[n-1]=nums[n-1]
        for i in range(1,n):
            vmax[i]=max(vmax[i-1],nums[i])
        for i in range(n-2,-1,-1):
            vmin[i]=min(vmin[i+1],nums[i])

        for i in range(n):
            if vmax[i]-vmin[i]<=k:
                return i
        return -1