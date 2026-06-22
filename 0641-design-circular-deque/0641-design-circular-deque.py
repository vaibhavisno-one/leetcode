from collections import deque
class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """

        self.dq=deque()

        self.length=k
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """

        if len(self.dq) == self.length:
            return False
        
        self.dq.appendleft(value)
        return True


    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.dq) == self.length:
            return False
        
        self.dq.append(value)
        return True

        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if len(self.dq) == 0:
            return False
        
        self.dq.popleft()
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if len(self.dq) == 0:
            return False
        
        self.dq.pop()
        return True
        

    def getFront(self):
        """
        :rtype: int
        """
        if len(self.dq) == 0:
            return -1
        
        return self.dq[0]
        
        

    def getRear(self):
        """
        :rtype: int
        """
        if len(self.dq) == 0:
            return -1
        
        return self.dq[-1]
        
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.dq)==0

    def isFull(self):
        """
        :rtype: bool
        """

        return len(self.dq)==self.length
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()