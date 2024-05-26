from collections import Counter
from typing import List


class Solution:
  def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
    cnt = Counter()
    col = Counter()
    res = []
    for x, y in queries:
      cnt[col[x]] -= 1
      if cnt[col[x]] < 1:
        del cnt[col[x]]
      col[x] = y
      cnt[y] += 1
      res.append(len(cnt))

    return res
