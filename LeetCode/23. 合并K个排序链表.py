class Helper:
  def __init__(self, val, node):
    self.val = val
    self.node = node

  def __gt__(self, other):
    return self.val > other.val

  def __lt__(self, other):
    return self.val < other.val


class Solution:
  def mergeKLists(self, lists: 'List[ListNode]') -> ListNode:
    candidates = [Helper(lists[i].val, lists[i]) for i in range(len(lists)) if lists[i] is not None]
    import heapq
    heapq.heapify(candidates)
    if len(candidates) > 0:
      head = heapq.heappop(candidates).node
      cur = head
      if head.next is not None:
        heapq.heappush(candidates, Helper(head.next.val, head.next))
    else:
      return None
    while len(candidates) > 0:
      temp = heapq.heappop(candidates).node
      cur.next = temp
      cur = temp
      if cur.next is not None:
        heapq.heappush(candidates, Helper(cur.next.val, cur.next))
    return head
