from functools import cache


class Solution:
  def waysToReachStair(self, k: int) -> int:

    @cache
    def dfs(i, jump, down):
      if i >= k + 2:
        return 0
      res = 0
      if i == k:
        res += 1

      res += dfs(i + (1 << jump), jump + 1, 0)

      if down == 0 and i > 0:
        res += dfs(i - 1, jump, 1)

      return res

    return dfs(1, 0, 0)
