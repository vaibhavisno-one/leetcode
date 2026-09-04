class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)-1
        i=0
        num_max=-1
        count=0
        
        
        while i <= n:
            num_max=max(num_max,nums[i])
            num_min=inf
            for j in range(i,n+1):
                num_min=min(num_min,nums[j])
            
            if num_max-num_min<=k:
                return i
            
            i+=1
    
        return -1
