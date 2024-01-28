from itertools import pairwise


class Solution:
  def countKeyChanges(self, s: str) -> int:
    s = s.lower()
    res = 0
    for x, y in pairwise(s):
      if x != y:
        res += 1
    return res
