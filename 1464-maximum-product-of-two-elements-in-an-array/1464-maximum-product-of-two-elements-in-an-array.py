class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sorted_arr=sorted(nums)
        
        return (sorted_arr[-1]-1)*(sorted_arr[-2]-1)