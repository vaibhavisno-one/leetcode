class Solution(object):
    def minEatingSpeed(self, piles, h):
        low=1
        high=max(piles)

        def isSmallest(m):
            val=0
            total=0
            for i in piles:
                val=(i+m-1)//m
                total+=val
            return h>=total

        while low<=high:
            mid=(low+high)//2
            if isSmallest(mid):
                high=mid-1
            else:
                low=mid+1
        return low