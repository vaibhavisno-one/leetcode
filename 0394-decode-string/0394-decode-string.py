class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        current=""
        num=0
        for char in s:

            if char.isdigit():
                num= num * 10+int(char)
            elif char=="[":
                stack.append((current,num))
                current=""
                num=0
            elif char=="]":
                prev,repeat=stack.pop()
                current=prev+current*repeat
            else:
                current+=char

        return current

        
