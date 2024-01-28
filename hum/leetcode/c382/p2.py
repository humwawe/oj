from collections import Counter
from typing import List


class Solution:
  def maximumLength(self, nums: List[int]) -> int:
    cnt = Counter(nums)
    res = cnt[1] - 1 if cnt[1] % 2 == 0 else cnt[1]
    for x in sorted(cnt.keys()):
      if x == 1:
        continue
      y = x
      tmp = 0
      while cnt[y] >= 2:
        y = y * y
        tmp += 1
      if cnt[y] >= 1:
        res = max(res, tmp * 2 + 1)
      else:
        res = max(res, tmp * 2 - 1)
    return res
