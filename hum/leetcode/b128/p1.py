from itertools import pairwise


class Solution:
  def scoreOfString(self, s: str) -> int:
    res = 0
    for x, y in pairwise(s):
      res += abs(ord(x) - ord(y))
    return res
