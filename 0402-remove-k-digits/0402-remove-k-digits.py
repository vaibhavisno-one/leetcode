class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        st=[]

        for i in num:
            while st and st[-1]>i and k>0:
                st.pop()
                k-=1
            st.append(i)

        while k>0:
            st.pop()
            k-=1
                


        
        
        
            
        ans= "".join(st).lstrip("0")

        if ans:
            return ans
        else:
            return "0"

