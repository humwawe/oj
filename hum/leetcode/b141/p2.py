from typing import List


class Solution:
  def minBitwiseArray(self, nums: List[int]) -> List[int]:
    n = len(nums)
    res = [-1] * n
    for i in range(n):
      if nums[i] == 2:
        continue
      x = ["0"] + list(bin(nums[i])[2:])
      j = len(x) - 1
      while j >= 0 and x[j] == '1':
        j -= 1
      x[j + 1] = '0'
      res[i] = int("".join(x), 2)
    return res
