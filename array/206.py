class Solution:
    def reverseList(self, head: ListNode, prev=None) -> ListNode:
        if head:
            ne=head.next
            head.next=prev
            return self.reverseList(ne,head) if ne else head
