class Solution(object):
    def removeOuterParentheses(self, s):

        if s == "":
            return ""
        
        res=""
        count=0
        for i in s:
            if i=="(":
                if count>0:
                    res+=i
                
                count+=1

            if i==")":
                count-=1

                if count>0:
                    res+=i
            
        return res



                
        