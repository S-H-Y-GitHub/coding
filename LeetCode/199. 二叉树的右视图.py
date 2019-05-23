# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def rightSideView(self, root: TreeNode):
    if root is None:
      return []
    queue = [(root, 0)]
    cur = 0
    res = []
    temp = []
    while len(queue) > 0:
      node, layer = queue.pop(0)
      if cur < layer:
        assert cur == layer - 1
        res.append(temp[-1])
        temp = [node.val]
        cur = layer
      else:
        temp.append(node.val)
      if node.left is not None:
        queue.append((node.left, layer + 1))
      if node.right is not None:
        queue.append((node.right, layer + 1))
    res.append(temp[-1])
    return res
