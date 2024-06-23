from typing import List


class Solution:
  def minOperations(self, nums: List[int]) -> int:
    c = 0
    res = 0
    n = len(nums)
    for i in range(n):
      if nums[i] ^ c == 0:
        res += 1
        c ^= 1
    return res
