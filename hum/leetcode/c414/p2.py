from typing import List


class Solution:
  def maxPossibleScore(self, start: List[int], d: int) -> int:
    n = len(start)
    start.sort()
    l = 0
    r = 2 * 10 ** 9

    def check(x: int) -> bool:
      cur = start[0]
      for i in range(1, n):
        if start[i] + d - cur < x:
          return False
        cur = max(start[i], cur + x)
      return True

    while l < r:
      mid = l + r + 1 >> 1
      if check(mid):
        l = mid
      else:
        r = mid - 1

    return l
