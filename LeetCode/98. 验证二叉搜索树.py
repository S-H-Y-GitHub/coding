# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def isValidBST(self, root: TreeNode) -> bool:
    if root is None:
      return True
    stack = [root]
    res = []
    processed = set()
    while len(stack) > 0:
      while root.left is not None and root.left not in processed:
        stack.append(root.left)
        root = root.left
      root = stack.pop()
      processed.add(root)
      res.append(root.val)
      if root.right is not None and root.right not in processed:
        stack.append(root.right)
        root = root.right
    # return res
    return all((res[i] < res[i + 1] for i in range(len(res) - 1)))
