D


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


from typing import Optional


class Solution:
  def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:

    ans = []

    def dfs(u):
      if not u:
        return [1, 0, 0]
      cl = dfs(u.left)
      cr = dfs(u.right)
      res = [0, 0, 1]
      if cl[0] and cr[0] and cl[1] == cr[1]:
        res[0] = 1
        res[1] = cl[1] + 1
        res[2] += cl[2] + cr[2]
      if res[0]:
        ans.append(res[2])
      return res

    dfs(root)
    if len(ans) < k:
      return -1
    return sorted(ans, reverse=True)[k - 1]
