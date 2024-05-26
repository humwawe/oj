from typing import List


class Solution:
  def duplicateNumbersXOR(self, nums: List[int]) -> int:
    res = 0
    cnt = [0] * 100
    for x in nums:
      cnt[x] += 1
      if cnt[x] == 2:
        res ^= x
    return res
