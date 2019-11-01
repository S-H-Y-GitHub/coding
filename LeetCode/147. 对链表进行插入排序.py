class Solution:
  def insertionSortList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
      return head
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
      fast = fast.next.next
      slow = slow.next
    middle = slow.next
    slow.next = None
    head1 = self.insertionSortList(head)
    head2 = self.insertionSortList(middle)
    # merge sorted list
    if head1.val < head2.val:
      new_head = head1
      head1 = head1.next
    else:
      new_head = head2
      head2 = head2.next
    cur = new_head
    while True:
      
      if head1 is None:
        cur.next = head2
        break
      if head2 is None:
        cur.next = head1
        break
      if head1.val < head2.val:
        cur.next, head1 = head1, head1.next
      else:
        cur.next, head2 = head2, head2.next
      cur = cur.next
    return new_head
