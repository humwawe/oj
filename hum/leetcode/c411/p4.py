from bisect import bisect_right
from itertools import accumulate
from typing import List


class Solution:
  def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
    n = len(s)
    l = [0] * n
    r = -1
    o = 0
    for i in range(n):
      while r + 1 < n and (o + int(s[r + 1]) <= k or r + 1 - i + 1 - (o + int(s[r + 1])) <= k):
        r += 1
        o += int(s[r])
      l[i] = r
      o -= int(s[i])

    cnt = [l[i] - i + 1 for i in range(n)]
    acc_cnt = list(accumulate(cnt, initial=0))

    res = []
    for i, j in queries:
      nj = bisect_right(l, j, lo=i)
      cur = acc_cnt[nj] - acc_cnt[i]

      length = j - nj + 1
      cur += length * (length + 1) // 2
      res.append(cur)
    return res
