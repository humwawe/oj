from typing import List


class Solution:
  def maximumTotalSum(self, maximumHeight: List[int]) -> int:
    n = len(maximumHeight)
    maximumHeight.sort(reverse=True)
    last = 10 ** 12
    res = []
    for i in range(n):
      cur = min(maximumHeight[i], last - 1)
      res.append(cur)
      last = cur
    if len(set(res)) != n or res[0] <= 0:
      return -1

    return sum(res)
