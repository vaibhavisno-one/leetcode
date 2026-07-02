class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        q=[]

        time=0

        for i in range(len(tickets)):
            if k>=i:
              time+=min(tickets[i],tickets[k])
            else:
                time+=min(tickets[k]-1,tickets[i])
            
        return time