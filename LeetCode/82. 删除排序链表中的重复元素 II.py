class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
      return head
    p2 = head
    head = ListNode(None)
    head.next = p2
    p1 = head
    p2 = head
    while p2.next is not None:
      flag = False
      p2 = p2.next
      v = p2.val
      while p2.next is not None and v == p2.next.val:
        flag = True
        p2 = p2.next
      if flag:
        p1.next = p2.next
      else:
        p1 = p2
    return head.next
