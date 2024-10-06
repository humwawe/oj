from typing import List


class Solution:
  def kthCharacter(self, k: int, operations: List[int]) -> str:

    def dfs(idx, k):
      if k == 1:
        return 0
      mid = 1 << (idx - 1)
      if operations[idx - 1] == 1:
        if k > mid:
          return (dfs(idx - 1, k - mid) + 1) % 26
        else:
          return dfs(idx - 1, k)
      else:
        if k > mid:
          return dfs(idx - 1, k - mid)
        else:
          return dfs(idx - 1, k)

    return chr(ord('a') + dfs((k - 1).bit_length(), k))
