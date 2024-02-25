import heapq
from bisect import bisect_left
from typing import List


class Solution:
  def earliestSecondToMarkIndices(self, a: List[int], c: List[int]) -> int:
    n, m = len(a), len(c)
    tot = sum(a)
    s = set()
    for i in range(m):
      c[i] -= 1
      if c[i] in s or a[c[i]] == 0:
        c[i] = -1
      s.add(c[i])

    def f(mid):
      h = []
      for i in range(mid, -1, -1):
        if c[i] >= 0:
          heapq.heappush(h, a[c[i]])
          if len(h) > (mid - i + 1) // 2:
            heapq.heappop(h)
      return tot - sum(h) + n <= mid + 1 - len(h)

    res = bisect_left(range(m), True, key=f)
    return res + 1 if res < m else -1
