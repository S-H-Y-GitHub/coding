class Solution:
  def sortList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
      return head
    mid = self.findmid(head)
    temp = mid.next
    mid.next = None
    p1 = self.sortList(head)
    p2 = self.sortList(temp)
    res = self.mergelist(p1, p2)
    return res
  
  def findmid(self, head):
    p1 = head
    p2 = head
    while True:
      if p2 is None or p2.next is None or p2.next.next is None:
        break
      p2 = p2.next.next
      p1 = p1.next
    return p1
  
  def mergelist(self, h1, h2):
    if h1 is None:
      return h2
    if h2 is None:
      return h1
    if h1.val < h2.val:
      res = h1
      p1 = h1.next
      p2 = h2
    else:
      res = h2
      p1 = h1
      p2 = h2.next
    res_head = res
    while True:
      if p1 is None:
        res.next = p2
        return res_head
      if p2 is None:
        res.next = p1
        return res_head
      if p1.val < p2.val:
        res.next = p1
        res = p1
        p1 = p1.next
      else:
        res.next = p2
        res = p2
        p2 = p2.next
