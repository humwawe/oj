from collections import Counter
from typing import List


class Solution:
  def medianOfUniquenessArray(self, nums: List[int]) -> int:
    n = len(nums)
    k = (n * (n + 1) // 2 + 1) // 2

    def check(mid):
      cnt = Counter()
      c = 0
      l = 0
      res = 0
      for r in range(n):
        cnt[nums[r]] += 1
        if cnt[nums[r]] == 1:
          c += 1
        while c > mid:
          cnt[nums[l]] -= 1
          if cnt[nums[l]] == 0:
            c -= 1
          l += 1
        res += r - l + 1
      return res >= k

    l, r = 1, n
    while l < r:
      mid = (l + r) // 2
      if check(mid):
        r = mid
      else:
        l = mid + 1
    return l
