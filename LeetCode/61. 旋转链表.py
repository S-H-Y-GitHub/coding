# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if head is None or head.next is None:
      return head
    phead = head
    pend = head
    pk = head
    pk1 = None
    for i in range(k):
      if pend.next is None:
        pend = head
        k = k % (i+1)
        break
      else:
        pend = pend.next
    else:
      while pend.next is not None:
        pk1=pk
        pk=pk.next
        pend=pend.next
      pend.next=phead
      pk1=pk.next if pk.next is not None else head
      pk.next=None

      return pk1
  
    for i in range(k):
      pend = pend.next
    while pend.next is not None:
      pk1=pk
      pk=pk.next
      pend=pend.next
    pend.next=phead
    pk1=pk.next if pk.next is not None else head
    pk.next=None
    
    return pk1
