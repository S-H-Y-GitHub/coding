class Solution:
  def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    if k <= 1:
      return head
    node = head
    prev_node = None
    time = 0
    while True:
      cur = node
      if cur is None:
        return head
      n1 = node.next
      if n1 is None:
        if prev_node is not None:
          prev_node.next = cur
        return head
      n2 = node.next.next
      for i in range(k-1):
        n1.next = cur
        if n2 is not None:
          cur = n1
          n1 = n2
          n2 = n2.next
        else:
          if i == k-2:
            node.next = None
            if prev_node is not None:
              prev_node.next = n1
            else:
              head = n1
            return head
          else:
            for j in range(i):
              n1.next = n2
              n2 = n1
              n1 = cur
              cur = cur.next
            n1.next = n2
            if prev_node is not None:
              prev_node.next = cur
            return head
      time += 1
      if time == 1:
        head = cur
      else:
        prev_node.next = cur
      # node.next = n1
      prev_node = node
      node = n1
