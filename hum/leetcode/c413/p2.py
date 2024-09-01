from typing import List

from sortedcontainers import SortedList


class Solution:
  def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
    sl = SortedList()
    res = []
    for x, y in queries:
      sl.add(abs(x) + abs(y))
      if len(sl) < k:
        res.append(-1)
      else:
        res.append(sl[k - 1])
    return res
