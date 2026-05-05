class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        st=s+s

        if len(s)!=len(goal):
            return False

        if goal in st:
            return True
        else:
            return False
        