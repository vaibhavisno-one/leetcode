class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        result=[]

        used=set()

        def bck(current):

            if len(current)==len(nums):
                result.append(current.copy())
                return

            for i in range(len(nums)):
                choice=nums[i]

                if choice in used:
                    continue

                current.append(choice)

                used.add(choice)

                bck(current)
                current.pop()
                used.remove(choice)

        bck([])
        return result