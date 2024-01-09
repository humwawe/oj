from functools import cache


class Solution:
  def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
    n = len(s)

    @cache
    def dfs(i, st, used):
      if i == n:
        return 1
      cur = 1 << (ord(s[i]) - ord('a'))
      nst = st | cur
      if nst.bit_count() > k:
        res = dfs(i + 1, cur, used) + 1
      else:
        res = dfs(i + 1, nst, used)

      if used:
        return res

      for j in range(26):
        nst = st | 1 << j
        if nst.bit_count() > k:
          res = max(res, dfs(i + 1, 1 << j, True) + 1)
        else:
          res = max(res, dfs(i + 1, nst, True))
      return res

    return dfs(0, 0, False)
