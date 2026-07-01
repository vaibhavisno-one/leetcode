class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        l=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]!=val:
                l+=1
            else:
                nums.remove(nums[i])

        return l