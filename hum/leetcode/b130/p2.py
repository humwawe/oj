from collections import defaultdict
from typing import List


class Solution:
  def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
    d = defaultdict(list)
    for i, (x, y) in enumerate(points):
      d[max(abs(x), abs(y))].append(s[i])

    res = 0
    now = set()
    for k in sorted(d.keys()):
      t = set(d[k])
      if len(d[k]) != len(t):
        return res
      for c in d[k]:
        if c in now:
          return res
      for c in d[k]:
        now.add(c)
        res += 1

    return res
