# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList( head) :
            current=head
            p=None
            n=None
            while current:
                p=current
                temp=current.next
                p.next=n
                n=current
                current=temp
            return p
        head=reverseList(head)
        dummy=ListNode(0)
        dummy.next=head
        current=head
        maxi=current.val
        while current and current.next:
            if current.next.val<maxi:
                current.next=current.next.next
            else:
                current=current.next
                maxi=current.val
        head=reverseList(head)
        return head


        