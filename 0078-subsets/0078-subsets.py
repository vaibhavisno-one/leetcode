class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]

        def bck(start, current):
            result.append(current.copy())

            for i in range(start, len(nums)):

                current.append(nums[i])

                bck(i+1,current)
                current.pop()

        bck(0,[])

        return result
