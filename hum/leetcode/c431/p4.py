from _bisect import bisect_left
from typing import List


class Solution:
  def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
    a = [(r, l, weight, i) for i, (l, r, weight) in enumerate(intervals)]
    a.sort(key=lambda t: t[0])
    f = [[(0, []) for _ in range(5)] for _ in range(len(intervals) + 1)]
    for i, (r, l, weight, idx) in enumerate(a):
      k = bisect_left(a, (l,), hi=i)
      for j in range(1, 5):
        s2, id2 = f[k][j - 1]
        f[i + 1][j] = min(f[i][j], (s2 - weight, sorted(id2 + [idx])))
    return f[-1][4][1]
