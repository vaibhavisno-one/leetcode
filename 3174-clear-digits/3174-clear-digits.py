class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        st=[]

        for ch in s:
            
                
            if ch.isalpha():
                st.append(ch)
            else:
                if st:
                    st.pop()

        return "".join(st)