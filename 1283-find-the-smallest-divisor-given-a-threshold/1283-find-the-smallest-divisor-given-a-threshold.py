class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low=1
        high=max(nums)

        def isSmallest(m):
            val=0
            total=0
            for i in nums:
                val=(i+m-1)//m
                total+=val
            return threshold>=total

        while low<=high:
            mid=(low+high)//2
            if isSmallest(mid):
                high=mid-1
            else:
                low=mid+1
        return low
        