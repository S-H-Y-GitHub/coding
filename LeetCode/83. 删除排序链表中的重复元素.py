class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
      return head
    p1 = head
    p2 = head
    v = p2.val
    head = ListNode(None)
    head.next = p1
    p1 = head
    while p2 is not None:
      v = p1.val
      while v == p2.val:
        p2 = p2.next
        if p2 is None:
          p1.next = p2
          return head.next
      p1.next = p2
      p1 = p2
      p2 = p2.next
      
    return head.next
