from bisect import bisect_left, bisect_right
from collections import Counter
from typing import List


class Solution:
  def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
    nums.sort()
    candidates = set(nums)
    n = len(nums)
    cnt = Counter(nums)

    for i in range(1, n):
      candidates.add((nums[i] + nums[i - 1]) // 2)

    res = 0
    for c in candidates:
      l = bisect_left(nums, c - k)
      r = bisect_right(nums, c + k)

      length = r - l - cnt[c]
      res = max(res, min(length, numOperations) + cnt[c])

    return res
