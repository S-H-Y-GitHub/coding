class Solution:
  def isPalindrome(self, head: ListNode) -> bool:
    if head is None:
      return True
    mid = head
    tail = head
    # 找到中点
    while True:
      mid = mid.next
      if tail.next is not None:
        tail = tail.next
      else:
        break
      if tail.next is not None:
        tail = tail.next
      else:
        break
      
    temp = None
    while mid is not None:
      next = mid.next
      mid.next = temp
      temp = mid
      mid = next
    
    while tail is not None:
      if tail.val != head.val:
        return False
      tail = tail.next
      head = head.next
    return True
