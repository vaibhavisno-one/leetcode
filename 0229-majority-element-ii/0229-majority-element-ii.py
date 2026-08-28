class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n=len(nums)/3
        Counthash={}
        arr=[]
        for num in nums:
            Counthash[num]=Counthash.get(num,0)+1

        for num in Counthash:
            if Counthash[num]>n:
                arr.append(num)
        return arr