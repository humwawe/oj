from collections import Counter
from typing import List


class Solution:
  def sumDigitDifferences(self, nums: List[int]) -> int:
    l = len(str(nums[0]))

    cnt = [Counter() for _ in range(l)]
    res = 0
    for i, num in enumerate(nums, start=1):
      t = num
      j = 0
      while t:
        a = t % 10
        res += i - 1 - cnt[j][a]
        cnt[j][a] += 1
        t = t // 10
        j += 1
    return res
