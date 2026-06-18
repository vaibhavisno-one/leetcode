class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        stack=[]
        sec=[]
        for char in s:
            if char != "#":
                stack.append(char)
            
            elif char == "#" and len(stack)==0:
                continue
            elif char == "#":
                stack.pop()

        for char in t:
            if char != "#":
                sec.append(char)
            elif char == "#" and  len(sec)==0:
                continue
            elif char == "#":
                sec.pop()
            
        return sec==stack