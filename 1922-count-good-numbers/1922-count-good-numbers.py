class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        even=(n+1)//2
        prime=n//2
        mod=pow(10,9)+7

        return (pow(5,even,mod)*pow(4,prime,mod))% mod