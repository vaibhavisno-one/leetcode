# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap=[]
        for row in lists:
            curr=row
            while curr:
                heapq.heappush(heap,curr.val)
                curr=curr.next
        
        dummy=ListNode(0)
        curr=dummy

        while heap:
            curr.next=ListNode(heapq.heappop(heap))
            curr=curr.next
        
        return dummy.next
