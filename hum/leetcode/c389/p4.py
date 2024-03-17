from itertools import accumulate
from typing import List


class Solution:
  def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:

    tmp = "".join(map(str, nums))
    c = 0
    if tmp.find("111") != -1:
      c = 3
    elif tmp.find("11") != -1:
      c = 2
    elif tmp.find("1") != -1:
      c = 1

    if k <= c:
      return k - 1

    if maxChanges >= k - c:
      return max(c - 1, 0) + (k - c) * 2

    pos = [i for i, x in enumerate(nums) if x == 1]

    pre_sum = list(accumulate(pos, initial=0))
    n = len(pre_sum)
    res = float('inf')
    size = k - maxChanges
    for r in range(size, n):
      l = r - size
      mid = l + r >> 1
      s1 = pos[mid] * (mid - l) - (pre_sum[mid] - pre_sum[l])
      s2 = pre_sum[r] - pre_sum[mid] - pos[mid] * (r - mid)
      res = min(res, s1 + s2)
    return res + maxChanges * 2
