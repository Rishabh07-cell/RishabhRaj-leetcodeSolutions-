class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        arr = [dummy]
        while head:
            arr.append(head)
            head = head.next
