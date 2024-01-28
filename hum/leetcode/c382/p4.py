from typing import List


class Solution:
  def minOrAfterOperations(self, nums: List[int], k: int) -> int:
    res = 0
    mask = 0
    for i in range(29, -1, -1):
      mask |= 1 << i
      cnt = 0
      tmp = -1
      for v in nums:
        tmp &= v & mask
        if tmp:
          cnt += 1
        else:
          tmp = -1

      if cnt > k:
        res |= 1 << i
        mask ^= 1 << i
    return res
