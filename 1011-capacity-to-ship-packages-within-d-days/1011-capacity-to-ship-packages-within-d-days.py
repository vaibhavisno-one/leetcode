class Solution(object):
    def shipWithinDays(self, weights, days):
        low =max(weights)
        high=sum(weights)

        def canTake(m):
            load=0
            d=1
            for i in weights:
                if load+i>m:
                    d+=1
                    load=i
                else:
                    load=load+i
            return d<=days
                

        while (low<high):
            mid=(low+high)//2

            if canTake(mid):
                high=mid
            else:
                low = mid+1
        
        return low
                




        