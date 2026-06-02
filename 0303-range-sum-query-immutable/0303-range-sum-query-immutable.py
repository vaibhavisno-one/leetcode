class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.nums=nums
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        total =0

        for i in range(left,right+1):
            total+=self.nums[i]

        return total
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)