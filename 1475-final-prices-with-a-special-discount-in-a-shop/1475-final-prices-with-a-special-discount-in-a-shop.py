class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        
        
        ans=list(prices)
        st=[]

        for i in range(len(prices)-1,-1,-1):
            while st and st[-1]>prices[i]:
                st.pop()
                

            if st:
                ans[i]=prices[i]-st[-1]
            
            st.append(prices[i])

        return ans
