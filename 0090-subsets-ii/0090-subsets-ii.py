class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()

        def dfs(index,path):
            if index==len(nums):
                ans.append(path[:])
                return
            path.append(nums[index])
            dfs(index+1,path)
            path.pop()

            # skip duplicate branch

            while index+1 < len(nums) and nums[index]==nums[index+1]:
                index+=1

            dfs(index+1,path)

        dfs(0,[])

        return ans