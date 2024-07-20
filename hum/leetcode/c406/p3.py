import random
from functools import cache
from math import inf
from typing import List


class Solution:
  def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
    tmp = []
    for h in horizontalCut:
      tmp.append((h, 0))
    for v in verticalCut:
      tmp.append((v, 1))
    tmp.sort(key=lambda x: x[0], reverse=True)

    res = 0
    c1, c2 = 1, 1
    for v, t in tmp:
      if t == 0:
        c1 += 1
        res += c2 * v
      else:
        c2 += 1
        res += c1 * v
    return res

  def minimumCost2(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
    horizontalCut.sort(reverse=True)
    verticalCut.sort(reverse=True)

    @cache
    def dfs(c1, c2):
      if c1 == m and c2 == n:
        return 0
      res = inf
      if c1 < m:
        res = min(res, dfs(c1 + 1, c2) + c2 * horizontalCut[c1 - 1])
      if c2 < n:
        res = min(res, dfs(c1, c2 + 1) + c1 * verticalCut[c2 - 1])
      return res

    return dfs(1, 1)


s = Solution()
rd = random.Random()
n = rd.randint(1, 20)
m = rd.randint(1, 20)

h = [rd.randint(1, 100) for _ in range(n - 1)]
v = [rd.randint(1, 100) for _ in range(m - 1)]

print(s.minimumCost(n, m, h, v))
print(s.minimumCost2(n, m, h, v))
