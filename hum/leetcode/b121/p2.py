from typing import List


class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
    tmp = 0
    for num in nums:
      tmp ^= num
    res = 0
    for i in range(24):
      if tmp >> i & 1 != k >> i & 1:
        res += 1
    return res
