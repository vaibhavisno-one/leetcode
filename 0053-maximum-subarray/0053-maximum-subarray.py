class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local=nums[0]

        global_max=nums[0]

        for i in range(1,len(nums)):

            local=max(nums[i], local+nums[i])

            if local> global_max:
                global_max=local

        
        return global_max