# question link : https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        x=1
        y=head
        while y.next:
            x+=1
            if not y.next.next:
                prev=y
            y=y.next
        if n==x:
            y=head.next
            head.next=None
            head=y
            return head
        if n==1:
            prev.next=None
            return head
        x=x-n-1
        y=head
        while x:
            x-=1
            y=y.next
        y.next=y.next.next
        return head
