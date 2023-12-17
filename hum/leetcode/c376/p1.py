from collections import Counter
from typing import List


class Solution:
  def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    cnt = Counter()
    for g in grid:
      for x in g:
        cnt[x] += 1
    n = len(grid)
    res = [0, 0]
    for i in range(0, n * n):
      if cnt[i + 1] == 2:
        res[0] = i + 1
      if i + 1 not in cnt:
        res[1] = i + 1
    return res
