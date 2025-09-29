
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        left=0
        dum=cur=ListNode(-1)
        while l1 or l2 or left:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            total= val1+val2+left
            sm=total%10
            left=total//10
            cur.next=cur=ListNode(sm)
            l1=l1 and l1.next
            l2=l2 and l2.next
        return dum.next

        
        

        
