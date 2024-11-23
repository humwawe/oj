from collections import Counter
from typing import List


class Solution:
  def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
    n = len(fruits)

    res = sum([fruits[i][i] for i in range(n)])

    cnt1 = Counter()
    cnt1[(0, n - 1)] = fruits[0][-1]
    for _ in range(n - 1):
      ncnt1 = Counter()
      for x, y in cnt1:
        for dx, dy in [(1, -1), (1, 0), (1, 1)]:
          nx, ny = x + dx, y + dy
          if nx <= ny and 0 < nx < n and 0 < ny < n:
            ncnt1[(nx, ny)] = max(ncnt1[(nx, ny)], cnt1[(x, y)] + (fruits[nx][ny] if nx != ny else 0))
      cnt1 = ncnt1
    res += cnt1[(n - 1, n - 1)]

    cnt2 = Counter()
    cnt2[(n - 1, 0)] = fruits[n - 1][0]
    for _ in range(n - 1):
      ncnt2 = Counter()
      for x, y in cnt2:
        for dx, dy in [(-1, 1), (0, 1), (1, 1)]:
          nx, ny = x + dx, y + dy
          if nx >= ny and 0 < nx < n and 0 < ny < n:
            ncnt2[(nx, ny)] = max(ncnt2[(nx, ny)], cnt2[(x, y)] + (fruits[nx][ny] if nx != ny else 0))
      cnt2 = ncnt2

    res += cnt2[(n - 1, n - 1)]

    return res
