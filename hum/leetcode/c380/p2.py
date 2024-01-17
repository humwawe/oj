from bisect import bisect_left
from typing import List


class Solution:
  def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
    n = len(s)
    tmp = []
    for i in range(n):
      if s[i:i + len(b)] == b:
        tmp.append(i)
    res = []

    for i in range(n):
      if s[i:i + len(a)] == a:
        idx = bisect_left(tmp, i)
        if idx < len(tmp) and tmp[idx] - i <= k or idx - 1 >= 0 and i - tmp[idx - 1] <= k:
          res.append(i)

    return res
