class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr=[0]*len(nums)
        for i in range(len(nums)):
            if i%2==0:
                arr[i]=nums[i//2]

            else:
                arr[i]=nums[n+i//2]

        return arr
            