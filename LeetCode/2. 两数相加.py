# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(0)
    cur = head
    c = False
    only = None
    while True:
      if only is None and l1 is None:
        if l2 is None:
          return head
        else:
          only = l2
      elif only is None and l2 is None:
        only = l1
      if only is None:
        if c:
          s = l1.val + l2.val + 1
          c = False
        else:
          s = l1.val + l2.val
        if s >= 10:
          c = True
          s -= 10
        cur.val = s
        l1 = l1.next
        l2 = l2.next
        if l1 is None and l2 is None:
          break
        cur.next = ListNode(0)
        cur = cur.next
      else:
        if c:
          s = only.val + 1
          c = False
        else:
          s = only.val
        if s >= 10:
          c = True
          s -= 10
        cur.val = s
        only = only.next
        if only is None:
          break
        cur.next = ListNode(0)
        cur = cur.next
    if c:
      cur.next = ListNode(1)
    return head
