# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        stack=[]

        current=head

        while current:
            stack.append(current)
            current=current.next
        if not stack:
            return None
        new_head=stack.pop()
        current=new_head
        while stack:
            current.next=stack.pop()
            current = current.next
            # stack.pop()
        current.next=None

        return new_head