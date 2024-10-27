from functools import cache
from typing import List


class Solution:
  def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
    @cache
    def dfs(c, p):
      if c == k:
        return 0
      res = 0
      for np in range(n):
        if np == p:
          res = max(res, stayScore[c][p] + dfs(c + 1, p))
        else:
          res = max(res, travelScore[p][np] + dfs(c + 1, np))
      return res

    ans = 0

    for i in range(n):
      ans = max(ans, dfs(0, i))
    return ans
