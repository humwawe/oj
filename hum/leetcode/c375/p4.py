from collections import defaultdict
from typing import List


class Solution:
  def numberOfGoodPartitions(self, nums: List[int]) -> int:
    n = len(nums)
    right = defaultdict(int)
    for i in range(n):
      right[nums[i]] = i

    cnt = 0
    i = 0
    while i < n:
      lim = right[nums[i]]
      j = i
      while j < lim:
        lim = max(lim, right[nums[j]])
        j += 1
      cnt += 1
      i = j + 1
    mod = 10 ** 9 + 7

    return pow(2, (cnt - 1), mod)
