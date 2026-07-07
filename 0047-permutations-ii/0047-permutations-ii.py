class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        count=Counter(nums)

        def bck(current):
            if len(current)==len(nums):
                result.append(current.copy())
                return

            for choice in count:
                # choice=nums[i]

                if count[choice]>0:
                    current.append(choice)
                    count[choice]-=1
                

                    bck(current)

                    count[choice]+=1
                    current.pop()

        bck([])

        return result
