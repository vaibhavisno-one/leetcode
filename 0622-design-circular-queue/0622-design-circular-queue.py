class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q=[]
        self.length=k
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """

        if len(self.q) != self.length:
            self.q.append(value)
            return True
        
        return False


        
        

    def deQueue(self):
        """
        :rtype: bool
        """

        if len(self.q) == 0:
            return False
        
        self.q.pop(0)
        return True


        
        

    def Front(self):
        """
        :rtype: int
        """

        if len(self.q) ==0:
            return -1
        
        return self.q[0]

        

    def Rear(self):
        """
        :rtype: int
        """
        if len(self.q) ==0:
            return -1
        
        return self.q[-1]
        

    def isEmpty(self):
        """
        :rtype: bool
        """

        return len(self.q) ==0
        

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.q) == self.length:
           
            return True
        
        return False



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()