class Solution:
    def oddEvenList(self, head):
      oot, i, last, first = head, 1, None, None
        if head and head.next: first = head.next
        while head:
            latter = head.next
            if i%2 != 0: last = head
            if head.next: head.next = head.next.next
            head, i = latter, i+1
        if last: last.next = first
        return root
