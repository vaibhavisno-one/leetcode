class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)

        if not self.min_stack or value<=self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return 
        
        if not self.min_stack:
            return 

        value=self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """

        if not self.min_stack:
            return
        # return min(self.stack)
        return self.min_stack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()