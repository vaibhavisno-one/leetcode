class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=prices[0]
        maxP=0
        n= len(prices)
        for i in range(n):
            if prices[i]< low:
                low=prices[i]

            profit=prices[i]-low
            maxP=max(maxP,profit)

        return maxP