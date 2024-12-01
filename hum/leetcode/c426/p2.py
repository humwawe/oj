from collections import Counter
from math import inf
from typing import List


class Solution:
  def getLargestOutlier(self, nums: List[int]) -> int:
    n = len(nums)
    cnt = Counter(nums)
    acc = sum(nums)
    res = -inf
    for i in range(n):
      x = acc - nums[i]
      cnt[nums[i]] -= 1
      if x % 2 == 0 and cnt[x // 2]:
        res = max(res, nums[i])
      cnt[nums[i]] += 1
    return res
